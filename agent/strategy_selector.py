from state.models import RuleOutcome, Strategy


STRATEGY_MAP = {
    RuleOutcome.INACTIVE: Strategy.REENTRY_ASSIST,
    RuleOutcome.REPEATED_POSTPONEMENT: Strategy.SCOPE_REDUCTION,
    RuleOutcome.NORMAL: Strategy.NORMAL_PROGRESS,
}

def select_strategy(rule: RuleOutcome) -> Strategy:
    """
    Map rule outcome to intervention strategy.
    """
    return STRATEGY_MAP.get(rule, Strategy.NORMAL_PROGRESS)
