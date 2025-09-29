from src.sequence_utils import gc_content

def test_gc_content():
    seq = "ATGC"
    assert gc_content(seq) == 50.0
