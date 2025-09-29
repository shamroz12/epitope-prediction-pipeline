from Bio import SeqIO

def parse_fasta(filepath):
    """Parse FASTA file and return list of sequences (as strings)."""
    sequences = []
    for record in SeqIO.parse(filepath, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def gc_content(seq):
    """Compute GC content of a DNA sequence."""
    g = seq.count("G") + seq.count("g")
    c = seq.count("C") + seq.count("c")
    return round((g + c) / len(seq) * 100, 2)
