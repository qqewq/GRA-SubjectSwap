from gra_subjectswap.core.policies import HumanPolicy, AgentPolicy
from gra_subjectswap.core.swap_engine import SubjectSwapEngine
from gra_subjectswap.core.subject_state import SubjectState, SubjectWeights
from gra_subjectswap.core.roles import RoleType
from gra_subjectswap.core.gra_nullifier import GRANullifier

class EchoModel:
    def predict_action(self, state):
        return {"echo": state.get("data", "none")}

def test_step_and_swap():
    hp = HumanPolicy(allowed={"echo"}, forbidden=set(), required={"echo"})
    ap = AgentPolicy(EchoModel())
    state = SubjectState(RoleType.INSTRUMENT, RoleType.SUBJECT, SubjectWeights())
    engine = SubjectSwapEngine(hp, ap, GRANullifier(), state)
    out = engine.step({"data": "hello"})
    assert out["agent_action"]["echo"] == "hello"
    assert out["roles"]["human"] == RoleType.INSTRUMENT
    engine.swap()
    assert state.human_role == RoleType.SUBJECT
    out2 = engine.step({"data": "world"})
    # теперь агент – инструмент, его действие может зависеть от human
    assert "echo" in out2["agent_action"]
