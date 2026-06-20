from ..core.policies import AgentPolicy
from typing import Any, Dict
import numpy as np

class DummyRobotModel:
    """Заглушка модели управления роботом."""
    def predict_action(self, state: Dict[str, Any]) -> Dict[str, Any]:
        # Простой контроллер: двигаемся к объекту
        obj_pos = state.get("object_position", np.zeros(3))
        return {
            "joint_delta": [0.0, 0.0, 0.0, 0.0, obj_pos[2] * 0.1, 0.0],
            "gripper": True,
        }

class OptimusRobotPolicy(AgentPolicy):
    def __init__(self, model=None):
        if model is None:
            model = DummyRobotModel()
        super().__init__(model)
