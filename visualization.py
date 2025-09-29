import matplotlib.pyplot as plt

def plot_epitope_distribution(epitopes):
    """Simple bar chart of epitope frequencies."""
    freq = {}
    for e in epitopes:
        freq[e] = freq.get(e, 0) + 1

    plt.figure(figsize=(8, 4))
    plt.bar(freq.keys(), freq.values())
    plt.xticks(rotation=90)
    plt.title("Predicted Epitope Distribution")
    plt.tight_layout()
    plt.show()
