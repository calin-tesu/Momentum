from rules.rules import evaluate_rules
from state.store import get_user_state
from state.models import UserState

def main():
    """Main entry point for Momentum app."""
    # Load persisted user state
    user_state = get_user_state()
    print(f"Loaded user state: Current step ID: {user_state.current_step_id}, Days inactive: {user_state.days_inactive}")
    
    # Evaluate rules
    rule_outcome = evaluate_rules(user_state)
    print(f"Rule evaluation outcome: Intervention required: {rule_outcome.intervention_required}, Reason: {rule_outcome.reason}")


   # TODO: Add main app logic here (e.g., strategy selection, UI loop)

if __name__ == "__main__":
    main()