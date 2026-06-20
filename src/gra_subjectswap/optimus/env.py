from typing import Any, Dict
import numpy as np

class OptimusEnv:
    """Симуляция окружения для робота Optimus."""
    def __init__(self, initial_joint_angles=None):
        self.state = {
            "joint_angles": np.zeros(6) if initial_joint_angles is None else np.array(initial_joint_angles),
            "object_position": np.array([0.0, 0.0, 0.0]),
            "gripper_open": True,
        }
        self.step_count = 0

    def reset(self) -> Dict[str, Any]:
        self.state["joint_angles"] = np.zeros(6)
        self.state["object_position"] = np.array([0.0, 0.0, 0.0])
        self.state["gripper_open"] = True
        self.step_count = 0
        return self.get_state()

    def get_state(self) -> Dict[str, Any]:
        return {
            "joint_angles": self.state["joint_angles"].copy(),
            "object_position": self.state["object_position"].copy(),
            "gripper_open": self.state["gripper_open"],
            "step": self.step_count,
        }

    def apply_robot_action(self, action: Dict[str, Any]):
        if "joint_delta" in action:
            self.state["joint_angles"] += np.array(action["joint_delta"])
        if "gripper" in action:
            self.state["gripper_open"] = action["gripper"]
        self.step_count += 1

    def apply_human_action(self, action: Dict[str, Any]):
        # В симуляции человек может корректировать объект
        if "object_delta" in action:
            self.state["object_position"] += np.array(action["object_delta"])
