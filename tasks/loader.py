import json
from pathlib import Path
from typing import List

from state.models import TaskTemplate, TaskCategory


class TaskTemplateValidationError(Exception):
    pass


def load_task_templates(path: Path) -> List[TaskTemplate]:
    """
    Load and validate task templates from a JSON file.

    Returns:
        List[TaskTemplate]
    """
    if not path.exists():
        raise FileNotFoundError(f"Task template file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    if "TASK_TEMPLATES" not in raw:
        raise TaskTemplateValidationError("Missing top-level key: TASK_TEMPLATES")

    all_templates: List[TaskTemplate] = []
    seen_ids = set()

    for category, entries in raw["TASK_TEMPLATES"].items():
        if not isinstance(entries, list):
            raise TaskTemplateValidationError(
                f"Category '{category}' must be a list"
            )
        
        # Validate that the JSON category matches a defined TaskCategory
        try:
            TaskCategory(category)
        except ValueError:
            raise TaskTemplateValidationError(f"Unknown category '{category}' in JSON. Must be one of {[e.value for e in TaskCategory]}")

        for entry in entries:
            template = _validate_and_build_template(
                entry=entry,
                category=category,
                seen_ids=seen_ids,
            )
            all_templates.append(template)

    return all_templates


def _validate_and_build_template(
    entry: dict,
    category: str,
    seen_ids: set,
) -> TaskTemplate:
    """
    Validate a single task template entry and build a TaskTemplate object.
    
    Args:
        entry: The JSON entry dict.
        category: The category string.
        seen_ids: Set of already seen task IDs for uniqueness check.
    
    Returns:
        TaskTemplate: The validated template.
    
    Raises:
        TaskTemplateValidationError: If validation fails.
    """
    required_fields = {"id", "strategies", "description_hint"}

    missing = required_fields - entry.keys()
    if missing:
        raise TaskTemplateValidationError(
            f"Missing fields {missing} in category '{category}'"
        )

    task_id = entry["id"]

    if not isinstance(task_id, str) or not task_id.strip():
        raise TaskTemplateValidationError("Task id must be a non-empty string")

    if task_id in seen_ids:
        raise TaskTemplateValidationError(f"Duplicate task id detected: {task_id}")

    seen_ids.add(task_id)

    strategies = entry["strategies"]
    if not isinstance(strategies, list) or not strategies:
        raise TaskTemplateValidationError(
            f"Task '{task_id}' must define at least one strategy"
        )

    if not all(isinstance(s, str) for s in strategies):
        raise TaskTemplateValidationError(
            f"All strategies for task '{task_id}' must be strings"
        )

    description_hint = entry["description_hint"]
    if not isinstance(description_hint, str) or not description_hint.strip():
        raise TaskTemplateValidationError(
            f"Task '{task_id}' has empty description_hint"
        )

    return TaskTemplate(
        id=task_id,
        category=category,
        strategies=strategies,
        description_hint=description_hint,
    )
