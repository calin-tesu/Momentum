from typing import List, Optional

from state.models import UserState, TaskTemplate, AgentOutput
from tasks.selector import select_task
from .rules import determine_strategy


def run_agent_cycle(user_state: UserState, task_templates: List[TaskTemplate]) -> Optional[AgentOutput]:
    """
    Run a single cycle of the agent's decision-making process.
    Evaluates user state, selects strategy, and prepares response.
    """

    # Step 1 & 2: Evaluate rules and select strategy
    decision = determine_strategy(user_state)

    if decision is None:
        return None

    # Step 3: Select task based on strategy
    task = select_task(decision, task_templates)

    if not task:
        return None

    return AgentOutput(
        task_text=task.description_hint,
        selected_task_template_id=task.id
    )