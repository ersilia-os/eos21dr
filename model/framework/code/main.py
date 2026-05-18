import os
import sys

import numpy as np
import pandas as pd

root        = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))
input_file  = sys.argv[1]
output_file = sys.argv[2]

# Isolate matplotlib's config/cache dir BEFORE lazyqsar import. Without
# this, matplotlib (transitively imported by lazyqsar's descriptor stack)
# writes its font cache to $HOME/.cache/matplotlib — and we set HOME below
# to point at our bundled featurizer weights, which would pollute
# model/checkpoints/featurizer_weights_home/.cache/ on every run.
import atexit, shutil, tempfile
_mpl_dir = tempfile.mkdtemp(prefix="mpl_")
os.environ["MPLCONFIGDIR"] = _mpl_dir
atexit.register(lambda: shutil.rmtree(_mpl_dir, ignore_errors=True))

# LazyQSAR locates featurizer weights via $HOME/.lazyqsar/ — point it at our bundled copy.
os.environ["HOME"] = os.path.join(checkpoints, "featurizer_weights_home")

from lazyqsar.api.classifier_predict import predict as lqsar_predict

MODEL_NAMES = [
    "individual_inhibition",
    "merged_mic_decoys",
    "general_mic",
    "general_activity_decoys",
    "general_mic50",
]
model_dir_dict = {m: os.path.join(checkpoints, "models", m) for m in MODEL_NAMES}

# One call: descriptors are shared across all 5 sub-models.
tmp_out = output_file + ".tmp"
lqsar_predict(
    model_dir=model_dir_dict,
    input_csv=input_file,
    output_csv=tmp_out,
    predict_type="rank",
)
ranks_df = pd.read_csv(tmp_out)
os.remove(tmp_out)

# Consensus (mirrors chembl-antimicrobial-models/scripts/14_consensus_scoring.py).
reports = pd.read_csv(os.path.join(checkpoints, "reports.csv")).set_index("model_name")
W_COLS = ["w1", "w2", "w3", "w4", "w5", "w6", "w7"]
W_ALL_WEIGHTS = np.ones(len(W_COLS) + 1)

prob_ranks = ranks_df[MODEL_NAMES].fillna(0.0).values
w_quality  = np.array([reports.loc[m, W_COLS].values for m in MODEL_NAMES], dtype=float)
cutoffs    = np.array([reports.loc[m, "decision_cutoff_rank"] for m in MODEL_NAMES], dtype=float)

# w8: per-compound weight — 0 at/below decision cutoff, linear 0->1 above it.
c  = np.clip(cutoffs[np.newaxis, :], 0.0, 1.0 - 1e-9)
w8 = np.where(prob_ranks <= c, 0.0, (prob_ranks - c) / (1.0 - c))

n, M = prob_ranks.shape
w_all = np.empty((n, M, len(W_ALL_WEIGHTS)))
w_all[:, :, :len(W_COLS)] = w_quality
w_all[:, :,  len(W_COLS)] = w8
w_eff = np.average(w_all, axis=-1, weights=W_ALL_WEIGHTS)

consensus_raw = (prob_ranks * w_eff).sum(axis=1) / w_eff.sum(axis=1)

# Tanh IQR-restoring transform — k depends only on number of sub-models.
_TANH_A, _TANH_TAU = 1.156, 6.47
k = 2.0 * (1.0 + _TANH_A * (1.0 - np.exp(-M / _TANH_TAU)))
consensus = 0.5 + 0.5 * np.tanh(k * (consensus_raw - 0.5)) / np.tanh(k / 2)

out = pd.DataFrame({
    "consensus_score": consensus.round(4),
    **{m: ranks_df[m].round(4).values for m in MODEL_NAMES},
})
out.to_csv(output_file, index=False)
