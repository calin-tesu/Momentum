from typing import List, Optional

from state.models import UserState, TaskTemplate, AgentOutput, AgentInput, CurriculumStep, ProjectContext
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

    if not task:
        return None

    # Construct AgentInput
    # Note: CurriculumStep and ProjectContext are mocked here as they are not yet fully integrated
    agent_input = AgentInput(
        step=CurriculumStep(
            id=user_state.current_step_id,
            title="Placeholder Title",
            description="Placeholder Description",
            allowed_task_categories=[]
        ),
        strategy=decision,
        available_task_templates=[task],
        recent_task_categories=user_state.recent_task_categories,
        project_context=ProjectContext(
            project_type="android_compose",
            existing_files=[
                "MainActivity.kt",
                "MainScreen.kt",
                "Theme.kt",
                "MainViewModel.kt"
            ],
            known_components=[
                "Composable functions",
                "State hoisting",
                "ViewModel"
            ]
        )
    )

    instantiated_task = instatiator(
        system_prompt=system_prompt,
        agent_input=agent_input,
    )

    return AgentOutput(
        instantiated_task=instantiated_task,
        task_text=task.description_hint,
        selected_task_template_id=task.id,
        strategy_name=decision.name
    )