from pathlib import Path
from collections import defaultdict
from agent import fake_llm_adapter
from agent.orchestrator import run_agent_cycle
from state.store import get_user_state, record_task_completed, record_task_postponed
from state.models import TaskTemplate
from tasks import loader

def main():
    """Main entry point for Momentum app."""
    # Load task templates
    # TODO: Consider moving the loader to orchestrator or another appropriate module
    templates = loader.load_task_templates(Path("tasks/android_compose_tasks.json"))

    # Load system prompt
    # Consider moving to orchestrator or another appropriate module
    system_prompt = (Path("agent") / "system_prompt_task_instantiation.txt").read_text(encoding="utf-8").strip()

    # Print summary of loaded templates
    by_category = defaultdict(list)
    for t in templates:
        by_category[t.category].append(t)

    for category, items in by_category.items():
        print(f"{category} → {len(items)} tasks")
    print()

    while True:
        # Load persisted user state
        user_state = get_user_state()
        print(f"Loaded user state: Current step ID: {user_state.current_step_id}, Days inactive: {user_state.days_inactive}")

        # Run agent cycle
        response = run_agent_cycle(user_state=user_state,
                                   task_templates= templates, 
                                   system_prompt = system_prompt, 
                                   instatiator=fake_llm_adapter.fake_task_instantiator)
        if response:
            print(f"Selected strategy: {response.strategy_name}")
            print(f"Agent Output: {response.task_text} (ID: {response.selected_task_template_id})")
        else:
            print("No task selected by agent.")

        print()
        print(response.prompt)
        print()

        # For now, simulate user action with input
        action = input("Enter 'c' to complete task, 'p' to postpone, or 'q' to quit: ").strip().lower()
        if action == 'c':
            record_task_completed()
            print("Task completed.")
        elif action == 'p':
            record_task_postponed()
            print("Task postponed.")
        elif action == 'q':
            break
        else:
            print("Invalid input.")
        
        print("================================")
        print()



if __name__ == "__main__":
    main()