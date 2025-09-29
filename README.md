# Epitope Prediction Pipeline

This repository provides a reproducible **computational biology pipeline** for 
predicting and analyzing **B-cell and T-cell epitopes** from protein sequences.  
It combines sequence analysis, machine learning models, and visualization.

## Features
- Parse DNA/Protein FASTA sequences
- Compute basic sequence stats (GC content, codon usage, k-mer frequencies)
- Predict epitopes (using toy methods + extendable wrappers to IEDB/ML models)
- Visualize epitope distribution and sequence logos
- Example datasets + Jupyter notebooks for step-by-step learning

## Repository Layout
- `data/` – example datasets (FASTA, epitopes)
- `notebooks/` – Jupyter notebooks with tutorials
- `src/` – Python source code
- `tests/` – unit tests for reproducibility
- `requirements.txt` – Python dependencies

## Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/epitope-prediction-pipeline.git
cd epitope-prediction-pipeline
pip install -r requirements.txt
```
## Example 
Run epitope prediction on a protein sequence:

```python
from src.epitope_predictor import predict_epitopes

seq = "MKTIIALSYIFCLVFADYKDDDDK..."
epitopes = predict_epitopes(seq, method="toy")
print(epitopes)
```
## Dependencies
- Python 3.9+
- Biopython
- NumPy / Pandas
- Matplotlib / Seaborn
- scikit-learn
- Jupyter



