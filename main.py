from state.store import get_user_state
from state.models import UserState

def main():
    """Main entry point for Momentum app."""
    # Load persisted user state
    user_state = get_user_state()
    print(f"Loaded user state: Current step ID: {user_state.current_step_id}, Days inactive: {user_state.days_inactive}")
    
    # TODO: Add main app logic here (e.g., rule evaluation, strategy selection, UI loop)
    # For example:
    # while True:
    #     # Evaluate rules, select strategy, present task, handle user input
    #     pass

if __name__ == "__main__":
    main()