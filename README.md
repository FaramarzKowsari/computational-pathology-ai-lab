# Computational Pathology AI Lab

**From CNN Baselines to Foundation Models, Explainable AI, and Production MLOps**

**Current repository version: 1.0.1**

[![CI](https://github.com/FaramarzKowsari/computational-pathology-ai-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/FaramarzKowsari/computational-pathology-ai-lab/actions/workflows/ci.yml)
[![Docker Build](https://github.com/FaramarzKowsari/computational-pathology-ai-lab/actions/workflows/docker.yml/badge.svg)](https://github.com/FaramarzKowsari/computational-pathology-ai-lab/actions/workflows/docker.yml)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-2ea44f)](https://faramarzkowsari.github.io/computational-pathology-ai-lab/)
[![DOI](https://zenodo.org/badge/847122798.svg)](https://doi.org/10.5281/zenodo.21445854)
[![Archived v1.0.0 DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21445855.svg)](https://doi.org/10.5281/zenodo.21445855)
[![Book DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21444837.svg)](https://doi.org/10.5281/zenodo.21444837)
[![Google Books](https://img.shields.io/badge/Google%20Books-GGKEY%3A8ZWNQ7NFGBL-4285F4)](book/README.md)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/Software%20License-MIT-yellow.svg)](LICENSE)

> **Research and educational software only. This repository is not a medical device and has not been clinically validated for diagnosis, treatment, patient triage, prognosis, or autonomous medical decision-making.**

---

## Official project website

https://faramarzkowsari.github.io/computational-pathology-ai-lab/

## Project overview

**Computational Pathology AI Lab** is a production-oriented, research-first platform for histopathology image analysis, cancer-detection research, deep learning, explainable artificial intelligence, uncertainty estimation, whole-slide workflows, model evaluation, and reproducible MLOps.

The project connects four professional capabilities in one auditable codebase:

1. **Medical AI Research** — rigorous experimental design, leakage prevention, calibration, uncertainty, confidence intervals, error analysis, domain shift, and external-validation readiness.
2. **Machine Learning Engineering and MLOps** — packaging, configuration, automated tests, continuous integration, Docker, DVC, MLflow hooks, model-registry structure, API serving, and monitoring.
3. **Computer Vision Engineering** — convolutional neural networks, transfer learning, Vision Transformers, foundation-model adapters, tissue preprocessing, whole-slide utilities, Multiple Instance Learning, and explainability.
4. **Academic Teaching, Documentation, and Technical Authorship** — educational notebooks, methodology, research questions, architecture documentation, Model Card, Data Card, technical-report templates, and a companion book.

The repository is designed as a professional portfolio for research-engineering, machine-learning, computer-vision, MLOps, medical-AI, academic, and teaching positions.

## Quick links

| Resource | Link |
|---|---|
| Project website | [Open GitHub Pages](https://faramarzkowsari.github.io/computational-pathology-ai-lab/) |
| Source repository | [View source code](https://github.com/FaramarzKowsari/computational-pathology-ai-lab) |
| GitHub Actions | [View automated workflows](https://github.com/FaramarzKowsari/computational-pathology-ai-lab/actions) |
| Latest release | [View release v1.0.1](https://github.com/FaramarzKowsari/computational-pathology-ai-lab/releases/tag/v1.0.1) |
| Software DOI — all versions | [10.5281/zenodo.21445854](https://doi.org/10.5281/zenodo.21445854) |
| Archived software DOI — version 1.0.0 | [10.5281/zenodo.21445855](https://doi.org/10.5281/zenodo.21445855) |
| Machine-readable citation | [CITATION.cff](CITATION.cff) |
| BibTeX citation | [CITATION.bib](CITATION.bib) |
| Model Card | [MODEL_CARD.md](MODEL_CARD.md) |
| Data Card | [DATA_CARD.md](DATA_CARD.md) |
| Architecture guide | [docs/architecture.md](docs/architecture.md) |
| Reproducibility guide | [docs/reproducibility.md](docs/reproducibility.md) |
| Clinical limitations | [docs/clinical_limitations.md](docs/clinical_limitations.md) |
| Companion book | [Book directory](book/) |
| Book sample PDF | [Read or download](book/computational-pathology-engineering.pdf) |
| Book DOI | [10.5281/zenodo.21444837](https://doi.org/10.5281/zenodo.21444837) |
| Google Books identifier | `GGKEY:8ZWNQ7NFGBL` |

## Project origin: University of Colorado Boulder

This repository began as the author's **Deep Learning Cancer Detection** mini-project for a University of Colorado Boulder graduate course.

The original educational project used convolutional neural networks to classify small histopathology image patches for metastatic-cancer detection. Its original notebooks, Kaggle submission, and leaderboard evidence are preserved in:

```text
legacy/cu_boulder_original_assignment/
```

The current repository substantially extends that work into a maintainable research and software-engineering platform while preserving the historical origin of the project.

## What makes this repository different

- It combines medical-AI research with production-oriented software engineering.
- It distinguishes executed evidence from planned or unexecuted research.
- It provides synthetic, non-patient data for safe tests and CPU smoke runs.
- It supports conventional CNNs, transfer learning, Vision Transformers, and external foundation-model adapters.
- It includes whole-slide and Multiple Instance Learning building blocks.
- It implements discrimination, calibration, uncertainty, confidence intervals, error analysis, and drift utilities.
- It includes explainability methods such as Grad-CAM, Integrated Gradients, occlusion sensitivity, and attention visualization.
- It provides FastAPI serving and a Streamlit demonstration interface.
- It integrates automated tests, GitHub Actions, Docker, DVC, and MLflow hooks.
- It includes a Model Card, Data Card, reproducibility documentation, clinical limitations, and research questions.
- It connects executable research software to a separately citable companion book.
- It is permanently archived and citable through Zenodo.

## Current execution status

| Capability | Status |
|---|---|
| Synthetic patch generation | **Executable on CPU** |
| Image and label validation | **Executable** |
| Stratified dataset splitting | **Executable** |
| Group-aware splitting | **Executable** |
| Baseline CNN | **Executable** |
| Tiny Vision Transformer | **Executable** |
| ResNet support | **Executable with optional model dependencies** |
| DenseNet support | **Executable with optional model dependencies** |
| EfficientNet support | **Executable with optional model dependencies** |
| ConvNeXt support | **Executable with optional model dependencies** |
| Foundation-model interface | **Adapter architecture available; external weights are not redistributed** |
| Training pipeline | **Executable** |
| Evaluation pipeline | **Executable** |
| Medical-AI metrics | **Executable** |
| Calibration and Brier score | **Executable** |
| Bootstrap confidence intervals | **Executable** |
| Confusion-matrix analysis | **Executable** |
| Error analysis | **Executable** |
| Grad-CAM | **Executable for supported CNN models** |
| Integrated Gradients | **Executable** |
| Occlusion sensitivity | **Executable** |
| Monte Carlo Dropout | **Executable** |
| Temperature scaling | **Executable** |
| Tissue masking | **Executable for supported inputs** |
| Patch extraction | **Executable for supported inputs** |
| Multiple Instance Learning | **Executable** |
| FastAPI service | **Executable with a trained checkpoint or labeled demo predictor** |
| Streamlit interface | **Executable after optional UI dependencies are installed** |
| Docker image | **Build verified by GitHub Actions** |
| Continuous Integration | **Passing** |
| GitHub Pages | **Deployed** |
| Real Kaggle benchmark in this release | **Not Yet Benchmarked** |
| External dataset validation | **Not Performed** |
| Clinical validation | **Not Performed** |

## Supported research and engineering areas

### Medical AI research

- Patient- or slide-level leakage prevention
- Class-distribution analysis
- ROC-AUC and PR-AUC
- Sensitivity and specificity
- F1 score
- Balanced accuracy
- Matthews correlation coefficient
- Brier score
- Calibration error
- Bootstrap confidence intervals
- False-negative analysis
- Subgroup-analysis readiness
- Error analysis
- Domain shift
- Drift detection
- External-validation templates
- Human-review boundaries

### Computer vision engineering

- Patch-level image classification
- Image validation
- Data augmentation
- Stain-normalization utilities
- Baseline convolutional neural networks
- ResNet
- DenseNet
- EfficientNet
- ConvNeXt
- Vision Transformer
- Foundation-model adapters
- Tissue segmentation
- Patch extraction
- Whole-slide image utilities
- Multiple Instance Learning
- Attention-based aggregation
- Batch inference
- Heatmap-oriented workflows

### Explainable and trustworthy AI

- Grad-CAM
- Integrated Gradients
- Occlusion sensitivity
- Attention visualization
- Monte Carlo Dropout
- Predictive uncertainty
- Temperature scaling
- Calibration analysis
- Failure-case preservation
- Evidence-status labeling

### Machine Learning Engineering and MLOps

- Standard `src/` Python-package layout
- Typed and modular source code
- YAML experiment configurations
- Command-line interface
- Unit tests
- Integration tests
- Ruff static analysis
- Mypy-ready type annotations
- Pytest and coverage support
- GitHub Actions
- Docker
- Docker Compose
- DVC configuration
- MLflow integration hooks
- Model-registry structure
- Monitoring utilities
- Drift reports
- FastAPI serving
- Streamlit demonstration
- Reproducibility documentation

## Repository architecture

```text
Histology patches / Whole-Slide Images
                  |
                  v
       Validation and data audit
                  |
                  v
 Stain handling, preprocessing, augmentation
                  |
                  v
 Patient/slide-aware split and leakage controls
                  |
       +----------+----------+
       |                     |
       v                     v
Patch-level models      WSI / MIL pipeline
       |                     |
       +----------+----------+
                  |
                  v
 Training, configuration, experiment tracking
                  |
                  v
 Evaluation, calibration, uncertainty, intervals
                  |
                  v
 Explainability, error analysis, drift monitoring
                  |
                  v
       API, demo, reports, documentation
```

A visual architecture diagram is available at:

```text
docs/assets/architecture.svg
```

## Repository map

| Path | Purpose |
|---|---|
| `src/cpathlab/` | Reusable Python package |
| `src/cpathlab/data/` | Datasets, validation, preprocessing, augmentation, and splitting |
| `src/cpathlab/models/` | CNNs, transfer learning, ViT, foundation adapters, and MIL |
| `src/cpathlab/training/` | Training loop, losses, callbacks, and experiment tracking |
| `src/cpathlab/evaluation/` | Metrics, calibration, confidence intervals, and error analysis |
| `src/cpathlab/explainability/` | Grad-CAM, Integrated Gradients, occlusion, and attention tools |
| `src/cpathlab/uncertainty/` | MC Dropout and calibration utilities |
| `src/cpathlab/inference/` | Single-image and batch inference |
| `src/cpathlab/api/` | FastAPI service |
| `src/cpathlab/monitoring/` | Drift and monitoring utilities |
| `configs/` | Model and experiment YAML files |
| `scripts/` | Operational scripts and migration utilities |
| `tests/` | Unit and integration tests |
| `notebooks/` | Teaching-oriented notebooks |
| `app/` | Streamlit interface |
| `docs/` | Architecture, methodology, ethics, deployment, and reproducibility |
| `reports/` | Build reports, test reports, and benchmark templates |
| `book/` | Companion-book metadata and replaceable sample PDF |
| `website/` | GitHub Pages site and structured metadata |
| `legacy/` | Preserved University of Colorado Boulder project |
| `.github/workflows/` | CI, Docker, and GitHub Pages workflows |

## Quick start

### Clone the repository

```bash
git clone https://github.com/FaramarzKowsari/computational-pathology-ai-lab.git
cd computational-pathology-ai-lab
```

### Create a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

### Install the development environment

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### Generate and validate synthetic data

```bash
cpathlab generate-synthetic --output data/example --samples 40
cpathlab validate-data --image-dir data/example/images --labels data/example/labels.csv
```

### Run a CPU smoke-training job

```bash
cpathlab train-synthetic \
  --data-dir data/example \
  --epochs 1 \
  --output models/demo.pt
```

Windows PowerShell:

```powershell
cpathlab train-synthetic --data-dir data/example --epochs 1 --output models/demo.pt
```

### Run automated tests

```bash
pytest -q
```

### Run code-quality checks

```bash
ruff check src tests scripts
mypy src/cpathlab --ignore-missing-imports
```

## Makefile commands

```bash
make setup
make synthetic
make validate
make test
make quality
make train-smoke
make api
make demo
make build
make clean
```

## Run the API

```bash
uvicorn cpathlab.api.main:app --host 0.0.0.0 --port 8000
```

Open the interactive API documentation:

```text
http://localhost:8000/docs
```

Health endpoint:

```text
http://localhost:8000/health
```

## Run the Streamlit demonstration

```bash
streamlit run app/streamlit_app.py
```

The demonstration is intended for software testing and education. It must not be presented as a diagnostic medical application.

## Docker

Build the image:

```bash
docker build -t computational-pathology-ai-lab:1.0.0 .
```

Run the API:

```bash
docker run --rm -p 8000:8000 computational-pathology-ai-lab:1.0.0
```

Using Docker Compose:

```bash
docker compose up --build
```

The Docker build is also tested through GitHub Actions.

## Reproducibility principles

- Fix all random seeds.
- Record the software environment.
- Record dataset versions and checksums.
- Split by patient or slide before extracting patches.
- Never tune hyperparameters on the final test set.
- Record every experiment configuration.
- Preserve failed runs and failure cases.
- Report confidence intervals.
- Report calibration, not only discrimination.
- Report sensitivity and specificity at relevant thresholds.
- Preserve subgroup results.
- Separate internal validation from external validation.
- Mark all unexecuted experiments as `Not Yet Benchmarked`.
- Never publish fabricated metrics or unsupported clinical claims.

## Quality assurance

The repository includes automated workflows for:

- Python 3.11 testing
- Python 3.12 testing
- Ruff static analysis
- Pytest
- Coverage reporting
- Docker image build
- GitHub Pages deployment

Current workflow status:

- **Continuous Integration:** Passing
- **Docker Build:** Passing
- **GitHub Pages Deployment:** Passing

Verified project reports are available in:

```text
reports/TEST_REPORT.md
reports/BUILD_REPORT.md
reports/FILE_CREATION_REPORT.md
```

## Evidence and scientific limitations

This release does **not** claim:

- Clinical validity
- Regulatory approval
- Diagnostic performance
- Patient-level safety
- External generalization
- Foundation-model superiority
- Real-world deployment readiness in a clinical environment

The following items remain future research tasks:

- Re-execution on the complete licensed Kaggle dataset
- Patient- or slide-level external validation
- Comparison with modern pathology foundation models
- Whole-slide benchmarking
- Scanner and staining domain-shift experiments
- Pathologist review
- Prospective evaluation
- Regulatory and clinical validation

## Software release and permanent identifiers

### All software versions

**Concept DOI:**

[10.5281/zenodo.21445854](https://doi.org/10.5281/zenodo.21445854)

This DOI represents the software project across all current and future versions.

### Archived version 1.0.0

**Version-specific DOI:**

[10.5281/zenodo.21445855](https://doi.org/10.5281/zenodo.21445855)

Use this DOI when citing the exact archived `v1.0.0` release. For the current project and future versions, use the Concept DOI above. Zenodo assigns a new version-specific DOI after each GitHub release is archived.

### GitHub release

https://github.com/FaramarzKowsari/computational-pathology-ai-lab/releases/tag/v1.0.1

## Scientific citation

### Recommended project citation

Kowsari, F. (2026). *Computational Pathology AI Lab* (Version 1.0.1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21445854

The Concept DOI resolves to the latest archived version. To cite the original archived `v1.0.0` release exactly, use https://doi.org/10.5281/zenodo.21445855.

### BibTeX

```bibtex
@software{kowsari2026computationalpathologyailab,
  author       = {Kowsari, Faramarz},
  title        = {Computational Pathology AI Lab},
  year         = {2026},
  version      = {1.0.1},
  doi          = {10.5281/zenodo.21445854},
  url          = {https://doi.org/10.5281/zenodo.21445854},
  repository   = {https://github.com/FaramarzKowsari/computational-pathology-ai-lab},
  license      = {MIT}
}
```

Machine-readable citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)
- [`CITATION.bib`](CITATION.bib)
- [`.zenodo.json`](.zenodo.json)
- [`codemeta.json`](codemeta.json)

## Companion book

### Computational Pathology Engineering

**From Histology Patches and CNNs to Whole-Slide Foundation Models, Explainable AI, and Production MLOps**

**Author:** Faramarz Kowsari  
**Book DOI:** [10.5281/zenodo.21444837](https://doi.org/10.5281/zenodo.21444837)  
**Google Books Key:** `GGKEY:8ZWNQ7NFGBL`

The companion book and software are separate but connected research objects:

- The **book** provides the visual, educational, and conceptual architecture.
- The **software** provides executable implementations, tests, APIs, workflows, and engineering documentation.
- The book and software have separate DOI records and separate citation metadata.
- The current PDF is a clearly marked **Sample Placeholder Edition**.
- The final infographic edition will replace the file below while retaining the same filename:

```text
book/computational-pathology-engineering.pdf
```

Book resources:

| Resource | Link |
|---|---|
| Sample PDF | [Read or download](book/computational-pathology-engineering.pdf) |
| Book metadata | [book/README.md](book/README.md) |
| Book DOI | [10.5281/zenodo.21444837](https://doi.org/10.5281/zenodo.21444837) |
| Google Books identifier | `GGKEY:8ZWNQ7NFGBL` |
| Companion software — all versions | [10.5281/zenodo.21445854](https://doi.org/10.5281/zenodo.21445854) |
| Companion software — v1.0.0 | [10.5281/zenodo.21445855](https://doi.org/10.5281/zenodo.21445855) |

## Author

<p align="center">
  <a href="https://faramarzkowsari.github.io/">
    <img
      src="https://avatars.githubusercontent.com/u/105053743?v=4"
      alt="Faramarz Kowsari"
      width="220"
    >
  </a>
</p>

### Faramarz Kowsari

Faramarz Kowsari is an author, Software Engineer and AI researcher based in Istanbul. Focusing on the intersection of technology, education, and personal growth, he has published over 80 digital titles on international platforms. His areas of expertise span Artificial Intelligence, prompt engineering, modern trading strategies (Smart Money Concepts & algorithmic trading), as well as classical literature and mindfulness. In addition to writing, he develops web-based educational tools and creates specialized instructional video content.

### Official Profiles & Repositories

- Wikidata: https://www.wikidata.org/wiki/Q140389378
- ORCID: https://orcid.org/0000-0003-1692-0453
- Google Scholar: https://scholar.google.com/citations?user=G7tP5WMAAAAJ&hl=en
- GitHub: https://github.com/FaramarzKowsari
- LinkedIn: https://www.linkedin.com/in/faramarzkowsari
- Google Books: https://play.google.com/store/search?q=Faramarz_Kowsari&c=books
- Official Website: https://faramarzkowsari.github.io/
- Zenodo Records: https://zenodo.org/search?q=creators.orcid%3A%220000-0003-1692-0453%22&l=list&p=1&s=10&sort=bestmatch

## Contributing

Constructive research and engineering contributions are welcome.

Before opening a pull request:

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md).
2. Do not commit protected health information or restricted medical data.
3. Do not commit credentials, secrets, or private model weights.
4. Add or update automated tests.
5. Document data provenance and split logic.
6. Explain the research or engineering value of the change.
7. Mark unexecuted research as `Not Yet Benchmarked`.
8. Include limitations for all medical-AI claims.

## Security

Read [`SECURITY.md`](SECURITY.md) before deployment.

Never commit:

- Patient-identifiable information
- Restricted clinical images
- API keys
- Access tokens
- Private model weights
- Unlicensed datasets
- Fabricated benchmark results

## License

The repository source code is released under the [MIT License](LICENSE).

External datasets, pretrained model weights, third-party software, and the companion book retain their own licenses and terms.

---

**Repository:** https://github.com/FaramarzKowsari/computational-pathology-ai-lab  
**Project website:** https://faramarzkowsari.github.io/computational-pathology-ai-lab/  
**Software DOI — all versions:** https://doi.org/10.5281/zenodo.21445854  
**Archived software DOI — version 1.0.0:** https://doi.org/10.5281/zenodo.21445855  
**Book DOI:** https://doi.org/10.5281/zenodo.21444837  
**Google Books Key:** `GGKEY:8ZWNQ7NFGBL`
