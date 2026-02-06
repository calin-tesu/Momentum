from state.models import AgentInput


def fake_task_instantiator(
    *,
    system_prompt: str,
    agent_input: AgentInput,
) -> str:
    """
    Fake adapter for offline testing.

    Returns the full prompt exactly as it would be sent to the LLM,
    to allow copy-paste testing in AI Studio.
    """

    strategy = agent_input.strategy
    # In this fake adapter, we assume the first available task is the one to be instantiated
    task_template = agent_input.available_task_templates[0] if agent_input.available_task_templates else None

    user_prompt_parts = [
        f"Strategy: {strategy.name}",
    ]

    if task_template:
        user_prompt_parts.append(f"Task Template: {task_template.description_hint}")

    if agent_input.step:
        user_prompt_parts.append(f"User Context: Current step: {agent_input.step.id}")

    if agent_input.project_context:
        ctx = agent_input.project_context
        user_prompt_parts.append(f"Project Context: Type={ctx.project_type}")
        if ctx.existing_files:
            user_prompt_parts.append(f"Existing Files: {', '.join(ctx.existing_files)}")
        if ctx.known_components:
            user_prompt_parts.append(f"Known Components: {', '.join(ctx.known_components)}")

    user_prompt = "\n".join(user_prompt_parts)

    full_prompt = (
        "===== SYSTEM PROMPT =====\n"
        f"{system_prompt}\n\n"
        "===== USER PROMPT =====\n"
        f"{user_prompt}\n"
        "========================"
    )

    return full_prompt
