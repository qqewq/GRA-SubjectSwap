import yaml
from typing import Dict, Any
from ..core.roles import RoleType, ActorType
from ..core.policies import HumanPolicy, AgentPolicy
from ..core.subject_state import SubjectState, SubjectWeights

def load_config(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config

def build_human_policy_from_config(config: Dict) -> HumanPolicy:
    rules = config.get("human_rules", {})
    return HumanPolicy(
        allowed=set(rules.get("allowed", [])),
        forbidden=set(rules.get("forbidden", [])),
        required=set(rules.get("required", [])),
    )

def build_subject_state_from_config(config: Dict) -> SubjectState:
    roles = config.get("initial_roles", {})
    return SubjectState(
        human_role=RoleType[roles.get("human", "INSTRUMENT")],
        agent_role=RoleType[roles.get("agent", "SUBJECT")],
        weights=SubjectWeights(**config.get("initial_weights", {})),
    )
