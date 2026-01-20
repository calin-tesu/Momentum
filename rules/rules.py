from state.models import UserState, RuleOutcome
from datetime import datetime, timezone


def evaluate_rules(state: UserState) -> RuleOutcome:
    """Evaluate user state against deterministic rules to detect intervention needs.

    Rules:
    - Intervention required if days inactive >= 3
    - Intervention required if consecutive postponements >= 3
    """
    now = datetime.now(timezone.utc)
    days_inactive = 0
    if state.last_interaction_at:
        days_inactive = (now - state.last_interaction_at).days

    if days_inactive >= 3:
        return RuleOutcome(intervention_required=True, reason="inactivity_detected")
    elif state.consecutive_postponements >= 3:
        return RuleOutcome(intervention_required=True, reason="repeated_postponement")
    else:
        return RuleOutcome(intervention_required=False, reason="normal_progress")