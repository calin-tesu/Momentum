from dataclasses import dataclass
from typing import List, Optional

from state.models import UserState, TaskTemplate
from tasks.selector import select_task
from .rules import determine_strategy
from state.models import Strategy

@dataclass
class AgentResponse:
    strategy: Optional[Strategy]
    task_id: Optional[str]
    message: Optional[str]


def run_agent_cycle(user_state: UserState, task_templates: List[TaskTemplate]) -> AgentResponse:
    """
    Run a single cycle of the agent's decision-making process.
    Evaluates user state, selects strategy, and prepares response.
    """

    # Step 1 & 2: Evaluate rules and select strategy
    decision = determine_strategy(user_state)

    if decision is None:
        return AgentResponse(
            strategy=None,
            task_id=None,
            message=None
            )

    # Step 3: Select task based on strategy
    task = select_task(decision, task_templates)

    return AgentResponse(
        strategy=decision.name,
        task_id=task.id if task else None,
        message=task.description_hint if task else None
    )