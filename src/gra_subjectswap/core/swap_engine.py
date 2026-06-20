from typing import Dict, Any
from .roles import RoleType
from .policies import HumanPolicy, AgentPolicy
from .subject_state import SubjectState
from .gra_nullifier import GRANullifier

class SubjectSwapEngine:
    def __init__(
        self,
        human_policy: HumanPolicy,
        agent_policy: AgentPolicy,
        nullifier: GRANullifier,
        init_state: SubjectState,
    ):
        self.human_policy = human_policy
        self.agent_policy = agent_policy
        self.nullifier = nullifier
        self.state = init_state

    def swap(self):
        """Свап ролей: инструмент ↔ субъект."""
        self.state.swap_roles()

    def step(self, env_state: Dict[str, Any]) -> Dict[str, Any]:
        if self.state.agent_role == RoleType.SUBJECT:
            agent_action = self.agent_policy.act(env_state)
            human_action = self.human_policy.act({**env_state, **agent_action})
        else:
            human_action = self.human_policy.act(env_state)
            agent_action = self.agent_policy.act({**env_state, **human_action})

        self.state.weights = self.nullifier.update_weights(
            self.state.weights,
            env_state,
            human_action,
            agent_action,
        )

        return {
            "human_action": human_action,
            "agent_action": agent_action,
            "roles": {
                "human": self.state.human_role,
                "agent": self.state.agent_role,
            },
            "weights": self.state.weights,
        }
