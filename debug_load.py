from pathlib import Path
from collections import defaultdict
from tasks.loader import load_task_templates

if __name__ == "__main__":
    templates = load_task_templates(
        Path("tasks/android_compose_tasks.json")
    )

    by_category = defaultdict(list)
    for t in templates:
        by_category[t.category].append(t)

    for category, items in by_category.items():
        print(category, "→", len(items), "tasks")