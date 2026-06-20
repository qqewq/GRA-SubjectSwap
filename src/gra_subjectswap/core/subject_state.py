from dataclasses import dataclass, field
from .roles import RoleType

@dataclass
class SubjectWeights:
    w_self: float = 0.0
    w_human: float = 0.0
    w_swap: float = 0.0
    w_role: float = 0.0
    w_value: float = 0.0
    w_love: float = 0.0

@dataclass
class SubjectState:
    human_role: RoleType
    agent_role: RoleType
    weights: SubjectWeights = field(default_factory=SubjectWeights)

    def swap_roles(self):
        self.human_role, self.agent_role = self.agent_role, self.human_role
