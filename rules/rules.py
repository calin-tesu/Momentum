from state.models import UserState, RuleOutcome
from datetime import datetime, timezone


def evaluate_rules(state: UserState) -> RuleOutcome:
    """
    Evaluate user state against deterministic rules.

    Priority:
    1. Inactivity
    2. Repeated postponement
    3. Normal progress
    """

    now = datetime.now(timezone.utc)
    if state.last_interaction_at:
        days_inactive = (now - state.last_interaction_at).days
        if days_inactive >= 3:
            return RuleOutcome.INACTIVE
        
    if state.consecutive_postponements >= 3:
        return RuleOutcome.REPEATED_POSTPONEMENT
    
    return RuleOutcome.NORMAL