from dataclasses import dataclass
from typing import Optional

from state.models import UserState
from .rules import determine_strategy
from state.models import Strategy

@dataclass
class AgentResponse:
    strategy: Optional[str]
    task_id: Optional[str]
    message: Optional[str]


def run_agent_cycle(user_state: UserState) -> AgentResponse:
    """
    Run a single cycle of the agent's decision-making process.
    Evaluates user state, selects strategy, and prepares response.
    """

    # Step 1 & 2: Evaluate rules and select strategy
    strategy = determine_strategy(user_state)
    task_id = None  # task_id is not determined by this logic path

    # Step 3: Prepare response message
    if strategy == Strategy.REENTRY_ASSIST:
        message = "It's been a while since your last interaction. Please check in!"
    elif strategy == Strategy.SCOPE_REDUCTION:
        message = "We noticed you've postponed tasks multiple times. Can we assist you?"
    else:
        # No message for NORMAL_PROGRESS to avoid being too chatty.
        # Other event-driven celebrations can be added elsewhere.
        message = None

    return AgentResponse(
        strategy=strategy.name if strategy else None,
        task_id=task_id,
        message=message
    )