# import google.generativeai as genai

class LLMTaskInstantiator:
    def __init__(self, model_name: str, api_key: str):
        # genai.configure(api_key=api_key)
        # Remove the comment below when the generativeai package is available
        self.model = "genai.GenerativeModel(model_name)"

    # All parameters after * must be passed as keyword arguments
    def instantiate_task(
    self,
    *,
    system_prompt: str,
    # This is the only thing the model is allowed to instantiate. It must be a single action.
    task_template: str,
    # We use str not Enum here to keep the LLMAdapter decoupled from state.models
    strategy: str,
    # Optional additional context about the user
    user_context: str | None = None,
) -> str:
        """
        Instantiate a task template into a single concrete next action
        using the Gemini model.

        Returns:
            A single plain-text task instruction.
        """
        prompt = f"{system_prompt}\n\n"
        prompt += f"Strategy: {strategy}\n"
        prompt += f"Task Template: {task_template}\n"

        if user_context:
            prompt += f"User Context: {user_context}\n"

        # response = self.model.generate_content(prompt)
        # return response.text
        return prompt  # Placeholder return until generativeai package is available
