from agent.rules import determine_strategy
from state.store import get_user_state, record_task_completed, record_task_postponed
from state.models import InteractionType

def main():
    """Main entry point for Momentum app."""
    while True:
        # Load persisted user state
        user_state = get_user_state()
        print(f"Loaded user state: Current step ID: {user_state.current_step_id}, Days inactive: {user_state.days_inactive}")

        # Evaluate rules
        strategy = determine_strategy(user_state)
        print(f"Selected strategy: {strategy.name}")
        print("--------------------------------")

        # TODO: Integrate strategy selection, task instantiation, and UI here
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

if __name__ == "__main__":
    main()