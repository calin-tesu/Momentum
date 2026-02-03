from state.models import Strategy, TaskTemplate


def fake_task_instantiator(
    *,
    system_prompt: str,
    strategy: Strategy,
    task_template: TaskTemplate,
    user_context: str | None = None,
) -> str:
    """
    Fake adapter for offline testing.

    Returns the full prompt exactly as it would be sent to the LLM,
    to allow copy-paste testing in AI Studio.
    """

    user_prompt_parts = [
        f"Strategy: {strategy.name}",
        f"Task Template: {task_template.description_hint}",
    ]

    if user_context:
        user_prompt_parts.append(f"User Context: {user_context}")

    user_prompt = "\n".join(user_prompt_parts)

    full_prompt = (
        "===== SYSTEM PROMPT =====\n"
        f"{system_prompt}\n\n"
        "===== USER PROMPT =====\n"
        f"{user_prompt}\n"
        "========================"
    )

    return full_prompt
