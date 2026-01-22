from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum


class TaskCategory(Enum):
    """Bounded set of task types the AI agent can select from.
    These define the agent's action space - no other task types are allowed."""
    INSPECT = "inspect"
    RENAME = "rename"
    MODIFY_SMALL = "modify_small"
    ADD_MINIMAL = "add_minimal"
    REFACTOR_MICRO = "refactor_micro"


class InteractionType(Enum):
    """Explicit user feedback types that drive system behavior."""
    COMPLETED = "completed"
    POSTPONED = "postponed"

class RuleOutcome(Enum):
    """Result of deterministic rule evaluation.
    Bridge between user state monitoring and strategy selection.
    No AI involvement in rule evaluation."""
    INACTIVE = "inactivity_detected"
    REPEATED_POSTPONEMENT = "repeated_postponement"
    NORMAL = "normal_progress"

class Strategy(Enum):
    """Intervention strategies that constrain AI behavior."""
    REENTRY_ASSIST = "reentry_assist"
    SCOPE_REDUCTION = "scope_reduction"
    NORMAL_PROGRESS = "normal_progress"

@dataclass
class CurriculumStep:
    """A fixed, immutable step in the learning path.
    Never modified by AI - provides context only.
    Example: "Learn Android View Binding" """
    id: str
    title: str
    description: str
    allowed_task_categories: List[TaskCategory]


@dataclass
class UserState:
    """Historical record of user behavior and progress.
    Tracks signals that trigger rule-based interventions.
    Only explicit actions, no inferred data."""
    current_step_id: str
    days_inactive: int
    consecutive_postponements: int
    last_interaction_at: Optional[datetime]
    last_task_outcome: Optional[InteractionType]
    last_task_completed_at: Optional[datetime]
    postponements_current_step: int
    recent_task_categories: List[TaskCategory]


@dataclass
class InterventionStrategy:
    """Intervention approach that constrains AI behavior.
    Defines what the AI can do, not what it should do.
    Examples: "normal_progress", "scope_reduction", "task_variation" """
    id: str
    name: str
    allowed_task_categories: List[TaskCategory]
    description: str


@dataclass
class TaskTemplate:
    """Predefined task pattern from the bounded template library.
    AI selects from these, never creates new ones.
    Example: "Inspect the MainActivity class structure" """
    id: str
    category: TaskCategory
    step_id: str
    short_description: str


@dataclass
class AgentInput:
    """Strict boundary: everything the AI agent is allowed to see.
    No additional context or external data permitted.
    This enforces the bounded AI constraint."""
    step: CurriculumStep
    strategy: Strategy
    available_task_templates: List[TaskTemplate]
    recent_task_categories: List[TaskCategory]


@dataclass
class AgentOutput:
    """Strict boundary: everything the AI agent is allowed to output.
    Only one task description, no plans or sequences.
    AI never modifies system state directly."""
    task_text: str
    selected_task_template_id: str


@dataclass
class InteractionResult:
    """Explicit user feedback that updates system state.
    Triggers rule evaluation and potential interventions.
    Only two outcomes: completed or postponed."""
    result_type: InteractionType
    task_template_id: str
    timestamp: datetime

