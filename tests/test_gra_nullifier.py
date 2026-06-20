from gra_subjectswap.core.gra_nullifier import GRANullifier
from gra_subjectswap.core.subject_state import SubjectWeights

def test_update_weights_returns_weights():
    n = GRANullifier()
    w = SubjectWeights()
    new_w = n.update_weights(w, {}, {}, {})
    assert isinstance(new_w, SubjectWeights)
    assert new_w.w_swap >= w.w_swap  # заглушка увеличивает swap
