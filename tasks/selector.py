import random
from typing import List, Optional
from state.models import Strategy, TaskTemplate


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

    return random.choice(eligible)