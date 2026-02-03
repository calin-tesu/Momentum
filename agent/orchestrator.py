from typing import List, Optional

from state.models import UserState, TaskTemplate, AgentOutput
from tasks.selector import select_task
from .rules import determine_strategy


def run_agent_cycle(
        user_state: UserState, 
        task_templates: List[TaskTemplate],
        system_prompt: str,
        instatiator,
    ) -> Optional[AgentOutput]:
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

    prompt = instatiator(
        system_prompt=system_prompt,
        strategy=decision,
        task_template=task,
        user_context=f"Current step: {user_state.current_step_id}",
    )


    if not task:
        return None

    return AgentOutput(
        prompt=prompt,
        task_text=task.description_hint,
        selected_task_template_id=task.id,
        strategy_name=decision.name
    )