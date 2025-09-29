import random

def predict_epitopes(seq, method="toy"):
    """
    Toy epitope predictor.
    For now, selects random 9-mers as epitopes.
    Later: extend to ML models or IEDB API.
    """
    epitopes = []
    if len(seq) < 9:
        return epitopes

    for i in range(0, len(seq) - 9, 10):  # every 10 residues
        peptide = seq[i:i+9]
        if random.random() > 0.5:  # pretend "binding"
            epitopes.append(peptide)
    return epitopes
