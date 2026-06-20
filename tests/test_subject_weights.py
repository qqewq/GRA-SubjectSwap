from gra_subjectswap.core.subject_state import SubjectWeights, SubjectState
from gra_subjectswap.core.roles import RoleType

def test_weights_defaults():
    w = SubjectWeights()
    assert w.w_self == 0.0

def test_swap_roles():
    s = SubjectState(RoleType.INSTRUMENT, RoleType.SUBJECT)
    s.swap_roles()
    assert s.human_role == RoleType.SUBJECT
    assert s.agent_role == RoleType.INSTRUMENT
