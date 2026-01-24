from dataclasses import dataclass
from enum import Enum
from typing import List

# Defines the agent's action space.
# The AI must select ONE of these templates to instantiate.
class TaskCategory(Enum):
    INSPECT = "INSPECT"
    REFLECT = "REFLECT"
    PREPARE = "PREPARE"
    MICRO_MODIFY = "MICRO_MODIFY"

class StrategyType(str, Enum):
    ALL = "ALL"
    NORMAL = "NORMAL"
    REENTRY = "REENTRY"

@dataclass(frozen=True)
class TaskTemplate:
    """
    Static, validated task templates that define the agent's bounded action space.
    """
    id: str
    category: TaskCategory
    allowed_strategies: List[StrategyType]
    description_hint: str
    est_start_time_sec: int