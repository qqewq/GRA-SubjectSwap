import pytest
from gra_subjectswap.core.policies import HumanPolicy, AgentPolicy

class DummyModel:
    def predict_action(self, state):
        return {"move": "left"}

def test_human_policy_allowed():
    hp = HumanPolicy(allowed={"move"}, forbidden={"grab"}, required={"move"})
    with pytest.raises(ValueError):
        hp.act({"human_input": {"grab": True}})

def test_human_policy_required():
    hp = HumanPolicy(allowed={"move"}, forbidden=set(), required={"move"})
    with pytest.raises(ValueError):
        hp.act({"human_input": {"jump": True}})

def test_agent_policy():
    ap = AgentPolicy(DummyModel())
    action = ap.act({})
    assert action == {"move": "left"}
