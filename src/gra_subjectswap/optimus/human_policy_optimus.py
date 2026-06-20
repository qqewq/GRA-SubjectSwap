from ..core.policies import HumanPolicy
from typing import Any, Dict

class OptimusHumanPolicy(HumanPolicy):
    def act(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Эмулирует действие человека‑тренера.
        В реальной системе здесь мог бы быть CLI/GUI или запись демонстрации.
        """
        # Возвращаем демо-действие (заглушка)
        action = {
            "object_delta": [0.0, 0.0, 0.01],  # человек двигает объект вверх
        }
        # Проверка правил (наследуется от HumanPolicy.act)
        return super().act({**state, "human_input": action})
