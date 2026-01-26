from pathlib import Path
from tasks.loader import load_task_templates

if __name__ == "__main__":
    templates = load_task_templates(
        Path("tasks/android_compose_tasks.json")
    )

    for category, items in templates.items():
        print(category, "→", len(items), "tasks")