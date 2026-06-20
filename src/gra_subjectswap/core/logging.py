import json
from typing import Any, Dict, List
from datetime import datetime

class SwapLogger:
    def __init__(self, log_file: str = None):
        self.records: List[Dict[str, Any]] = []
        self.log_file = log_file

    def log_step(
        self,
        step: int,
        env_state: Dict,
        human_action: Dict,
        agent_action: Dict,
        roles: Dict,
        weights: Any,
    ):
        record = {
            "timestamp": datetime.now().isoformat(),
            "step": step,
            "roles": roles,
            "weights": weights.__dict__ if hasattr(weights, "__dict__") else str(weights),
            "human_action": human_action,
            "agent_action": agent_action,
            "env_state": env_state,
        }
        self.records.append(record)
        if self.log_file:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
