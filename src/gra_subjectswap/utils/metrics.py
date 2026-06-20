from typing import List, Dict
import numpy as np
from ..core.subject_state import SubjectWeights

def compute_stability(weight_history: List[SubjectWeights]) -> float:
    """Измеряет стабильность весов как обратную дисперсию."""
    if len(weight_history) < 2:
        return 1.0
    ws = np.array([[w.w_self, w.w_human, w.w_swap, w.w_role, w.w_value, w.w_love] for w in weight_history])
    var = np.var(ws, axis=0).mean()
    return 1.0 / (1.0 + var)

def subjectness_ratio(weights: SubjectWeights) -> float:
    """Доля субъектности агента относительно общей."""
    total = weights.w_self + weights.w_human + weights.w_swap + weights.w_role + weights.w_value + weights.w_love
    if total == 0:
        return 0.5
    return (weights.w_self + weights.w_swap) / total
