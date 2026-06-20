"""Свап ролей в рое из нескольких агентов."""
import sys
sys.path.insert(0, "src")
from gra_subjectswap.core.policies import HumanPolicy, AgentPolicy
from gra_subjectswap.core.swap_engine import SubjectSwapEngine
from gra_subjectswap.core.subject_state import SubjectState, SubjectWeights
from gra_subjectswap.core.roles import RoleType
from gra_subjectswap.core.gra_nullifier import GRANullifier

class SwarmModel:
    def predict_action(self, state):
        return {"formation": "V-shape"}

# Несколько агентов могут разделять одну политику
agent = AgentPolicy(SwarmModel())
human = HumanPolicy(allowed={"formation"}, forbidden=set(), required={"formation"})
engine = SubjectSwapEngine(human, agent, GRANullifier(),
                          SubjectState(RoleType.INSTRUMENT, RoleType.SUBJECT))

for t in range(5):
    out = engine.step({"obstacles": t})
    print(f"Tick {t}: {out['roles']}")
    if t == 2:
        engine.swap()
