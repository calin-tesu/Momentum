from state.models import UserState, Strategy
from datetime import datetime, timezone


def determine_strategy(state: UserState) -> Strategy:
    """
    Evaluate user state against deterministic rules to determine an intervention strategy.

    Priority:
    1. Inactivity -> REENTRY_ASSIST
    2. Repeated postponement -> SCOPE_REDUCTION
    3. Normal progress -> NORMAL_PROGRESS
    """

    now = datetime.now(timezone.utc)
    if state.last_interaction_at:
        days_inactive = (now - state.last_interaction_at).days
        if days_inactive >= 3:
            return Strategy.REENTRY_ASSIST

    if state.consecutive_postponements >= 3:
        return Strategy.SCOPE_REDUCTION

    return Strategy.NORMAL_PROGRESS