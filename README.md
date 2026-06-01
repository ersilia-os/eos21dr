# Antimicrobial activity prediction against Acinetobacter baumannii from public ChEMBL data

Bioactivity prediction of growth inhibition in Acinetobacter baumannii, trained as binary (active/inactive) classifiers from publicly available data in ChEMBL. Independent models are trained on multiple bioactivity datasets, corresponding to single point (e.g. percent effect) and dose-response (MIC) assays. A ranking score is provided for each model alongside a combined consensus score.

This model was incorporated on 2026-05-15.Last packaged on 2026-05-29.

## Information
### Identifiers
- **Ersilia Identifier:** `eos21dr`
- **Slug:** `antimicrobial-activity-abaumannii`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`, `Pneumonia`
- **Target Organism:** `Acinetobacter baumannii`
- **Tags:** `Gram-negative bacteria`, `ESKAPE`, `Antimicrobial activity`, `ChEMBL`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `8`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of antimicrobial activity against A. baumannii from 7 ChEMBL-trained sub-models, plus a quality-weighted consensus score.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| consensus_score | float | high | Tanh-transformed quality-weighted consensus probability across the 7 sub-models. Recommended threshold: 0.885. |
| individual_inhibition | float | high | Probability from sub-model trained on ChEMBL assay CHEMBL4296188 (inhibition %; cutoff 25%; n=21494). Recommended threshold: 0.864. |
| merged_mic_decoys | float | high | Probability from sub-model trained on MIC measurements merged across 7 ChEMBL assays (cutoff 20 uM; n=1510 incl. decoys). Recommended threshold: 0.815. |
| general_single_point | float | high | Probability from sub-model trained on single-point activity measurements aggregated across 3 ChEMBL assays (n=23439). Recommended threshold: 0.948. |
| general_dose_response | float | high | Probability from sub-model trained on dose-response measurements aggregated across 7 ChEMBL assays (n=8139). Recommended threshold: 0.665. |
| general_mic | float | high | Probability from sub-model trained on MIC measurements aggregated across 2075 ChEMBL assays (cutoff 10 uM; n=7763). Recommended threshold: 0.669. |
| general_activity_decoys | float | high | Probability from sub-model trained on single-point % activity aggregated across 86 ChEMBL assays (cutoff 50%; n=580 incl. decoys). Recommended threshold: 0.858. |
| general_mic50 | float | high | Probability from sub-model trained on MIC50 measurements aggregated across 63 ChEMBL assays (cutoff 10 uM; n=127). Recommended threshold: 0.543. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos21dr](https://hub.docker.com/r/ersiliaos/eos21dr)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos21dr.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos21dr.zip)

### Resource Consumption
- **Model Size (Mb):** `161`
- **Environment Size (Mb):** `1889`
- **Image Size (Mb):** `2230.59`

**Computational Performance (seconds):**
- 10 inputs: `40.11`
- 100 inputs: `29.98`
- 10000 inputs: `560.48`

### References
- **Source Code**: [https://github.com/ersilia-os/chembl-antimicrobial-models](https://github.com/ersilia-os/chembl-antimicrobial-models)
- **Publication**: [https://github.com/ersilia-os/chembl-antimicrobial-models](https://github.com/ersilia-os/chembl-antimicrobial-models)
- **Publication Type:** `Other`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos21dr
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos21dr
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
