from src.epitope_predictor import predict_epitopes

def test_epitope_length():
    seq = "MKTIIALSYIFCLVFADYKDDDDK"
    epitopes = predict_epitopes(seq)
    for e in epitopes:
        assert len(e) == 9
