import random
from typing import List, Optional
from state.models import Strategy, TaskTemplate, TaskCategory


def select_task(strategy: Strategy, templates: List[TaskTemplate]) -> Optional[TaskTemplate]:
    """
    Select an appropriate task template based on the given strategy.

    Args:
        strategy: The intervention strategy to match.
        templates: List of available TaskTemplate objects.

    Returns:
        An appropriate TaskTemplate if found, else None.
    """

    # Filter templates based on strategy
    eligible = [
        t for t in templates
        if strategy.name in t.strategies or "All" in t.strategies
    ]
    if not eligible:
        return None
    
    # Strategy-specific selection policy
    if strategy == Strategy.REENTRY:
        # Lowest-friction, orientation tasks
        preferred_categories = {TaskCategory.INSPECT.value, TaskCategory.REFLECT.value}

    elif strategy == Strategy.SCOPE_REDUCTION:
        # Smallest possible action
        preferred_categories = {TaskCategory.MICRO_MODIFY.value, TaskCategory.PREPARE.value}

    else:
        # NORMAL or fallback
        preferred_categories = None

    if preferred_categories:
        preferred = [
            t for t in eligible if t.category in preferred_categories
        ]
        if preferred:
            return random.choice(preferred)

    return random.choice(eligible)