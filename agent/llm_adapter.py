import google.generativeai as genai
from state.models import AgentInput

class LLMTaskInstantiator:
    def __init__(self, model_name: str, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def instantiate_task(
        self,
        *,
        system_prompt: str,
        agent_input: AgentInput,
    ) -> str:
        """
        Instantiate a task template into a single concrete next action
        using the Gemini model.

        Returns:
            A single plain-text task instruction.
        """
        strategy = agent_input.strategy
        # We assume the first available task is the one to be instantiated
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
        full_prompt = f"{system_prompt}\n\n{user_prompt}"

        response = self.model.generate_content(full_prompt)
        return response.text
