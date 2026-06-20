from abc import ABC, abstractmethod
from typing import Any, Dict

class BasePolicy(ABC):
    @abstractmethod
    def act(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Return action dictionary given environment state."""

class HumanPolicy(BasePolicy):
    def __init__(self, allowed: set, forbidden: set, required: set):
        self.allowed = set(allowed)
        self.forbidden = set(forbidden)
        self.required = set(required)

    def act(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Возвращает действие человека как инструмента, фильтруя по правилам.
        В реальной реализации здесь будет ввод от человека или демо-файла.
        """
        # Получаем действие (здесь - заглушка, ожидаем 'action' в state или ввод)
        action = state.get("human_input", {})
        # Проверки
        for k in self.forbidden:
            if k in action:
                raise ValueError(f"Forbidden action key: {k}")
        for k in self.required:
            if k not in action:
                raise ValueError(f"Required action key missing: {k}")
        return action

class AgentPolicy(BasePolicy):
    def __init__(self, model):
        self.model = model

    def act(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return self.model.predict_action(state)
