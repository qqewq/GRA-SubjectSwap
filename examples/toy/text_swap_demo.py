"""Текстовый диалог с эмуляцией LLM."""
import sys
sys.path.insert(0, "src")
from gra_subjectswap.core.policies import HumanPolicy, AgentPolicy
from gra_subjectswap.core.swap_engine import SubjectSwapEngine
from gra_subjectswap.core.subject_state import SubjectState, SubjectWeights
from gra_subjectswap.core.roles import RoleType
from gra_subjectswap.core.gra_nullifier import GRANullifier

class LLMModel:
    def predict_action(self, state):
        return {"reply": f"Агент слышит: {state.get('user_input', '')}"}

human = HumanPolicy(allowed={"reply"}, forbidden=set(), required={"reply"})
agent = AgentPolicy(LLMModel())
engine = SubjectSwapEngine(human, agent, GRANullifier(),
                          SubjectState(RoleType.INSTRUMENT, RoleType.SUBJECT))

for i, msg in enumerate(["Привет", "Как дела?", "Что видишь?"]):
    out = engine.step({"user_input": msg})
    print(f"User: {msg}, Agent: {out['agent_action']['reply']}, Role: {out['roles']}")
