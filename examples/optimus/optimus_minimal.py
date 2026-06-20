"""Минимальный пример SubjectSwap с заглушками."""
import sys
sys.path.insert(0, "src")

from gra_subjectswap.core.roles import RoleType
from gra_subjectswap.core.policies import HumanPolicy, AgentPolicy
from gra_subjectswap.core.subject_state import SubjectState, SubjectWeights
from gra_subjectswap.core.swap_engine import SubjectSwapEngine
from gra_subjectswap.core.gra_nullifier import GRANullifier

class DummyModel:
    def predict_action(self, state):
        return {"action": "move_forward"}

human_pol = HumanPolicy(allowed={"action"}, forbidden={}, required={"action"})
agent_pol = AgentPolicy(DummyModel())
nullifier = GRANullifier()
state = SubjectState(RoleType.INSTRUMENT, RoleType.SUBJECT, SubjectWeights())
engine = SubjectSwapEngine(human_pol, agent_pol, nullifier, state)

for i in range(5):
    env = {"step": i}
    out = engine.step(env)
    print(out["roles"], out["weights"])
    if i == 2:
        engine.swap()
