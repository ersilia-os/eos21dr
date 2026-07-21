# Antimicrobial activity prediction against Acinetobacter baumannii from public ChEMBL data

Bioactivity prediction of growth inhibition in Acinetobacter baumannii, trained as binary (active/inactive) classifiers from publicly available data in ChEMBL. Independent models are trained on multiple bioactivity datasets, corresponding to single-point (Inhibition) and dose-response (MIC) assays, among others. A ranking score is provided for each model alongside a combined consensus score.

This model was incorporated on 2026-05-15.Last packaged on 2026-07-21.

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
- **Output Dimension:** `10`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of antimicrobial activity against Acinetobacter baumannii from 9 ChEMBL-trained sub-models, plus a quality-weighted consensus score.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| consensus_score | float | high | Tanh-transformed quality-weighted consensus probability across the 9 sub-models. Recommended threshold: 0.846. |
| sp_catchall | float | high | Probability from sub-model trained on ChEMBL single-point low-data catch-all pool of 41 assays (432 compounds; predominantly Inhibition). Recommended threshold: 0.791. |
| dr_0001 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 182 assays (1937 compounds; predominantly MIC). Recommended threshold: 0.785. |
| dr_0002 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 126 assays (1236 compounds; predominantly MIC). Recommended threshold: 0.822. |
| dr_0000 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 97 assays (1010 compounds; predominantly MIC). Recommended threshold: 0.608. |
| dr_0003 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 73 assays (657 compounds; predominantly MIC). Recommended threshold: 0.616. |
| dr_0004 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 36 assays (503 compounds; predominantly MIC). Recommended threshold: 0.691. |
| dr_0005 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 35 assays (388 compounds; predominantly MIC). Recommended threshold: 0.565. |
| dr_0006 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 45 assays (233 compounds; predominantly MIC). Recommended threshold: 0.749. |
| dr_0007 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 3 assays (101 compounds; predominantly MIC). Recommended threshold: 0.723. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos21dr](https://hub.docker.com/r/ersiliaos/eos21dr)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos21dr.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos21dr.zip)

### Resource Consumption
- **Model Size (Mb):** `144`
- **Environment Size (Mb):** `7208`
- **Image Size (Mb):** `7309.15`

**Computational Performance (seconds):**
- 10 inputs: `53.61`
- 100 inputs: `45.01`
- 10000 inputs: `1311.01`

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
