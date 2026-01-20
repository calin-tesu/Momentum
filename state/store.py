from state.models import InteractionType, UserState
from datetime import datetime, timezone
from state.persistence import save_user_state, load_user_state


def get_user_state() -> UserState:
    """Load the current UserState from persistence."""
    return load_user_state()


def record_task_completed() -> UserState:
    """Record that a task has been completed by the user."""
    state = load_user_state()
    now = datetime.now(timezone.utc)

    state.last_interaction_at = now
    state.last_task_outcome = InteractionType.COMPLETED
    state.last_task_completed_at = now

    # Reset postponement counters
    state.consecutive_postponements = 0
    state.postponements_current_step = 0
    save_user_state(state)
    return state


def record_task_postponed() -> UserState:
    """Record that a task has been postponed by the user."""
    state = load_user_state()
    now = datetime.now(timezone.utc)

    state.last_interaction_at = now
    state.last_task_outcome = InteractionType.POSTPONED

    # Increment postponement counters
    state.consecutive_postponements += 1
    state.postponements_current_step += 1
    save_user_state(state)
    return state