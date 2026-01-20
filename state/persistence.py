import json
from datetime import datetime
from typing import Optional
from state.models import UserState, InteractionType, TaskCategory


def save_user_state(state: UserState, file_path: str = "user_state.json"):
    """Save UserState to a JSON file."""
    data = {
        "current_step_id": state.current_step_id,
        "days_inactive": state.days_inactive,
        "consecutive_postponements": state.consecutive_postponements,
        "last_interaction_at": state.last_interaction_at.isoformat() if state.last_interaction_at else None,
        "last_task_outcome": state.last_task_outcome.value if state.last_task_outcome else None,
        "last_task_completed_at": state.last_task_completed_at.isoformat() if state.last_task_completed_at else None,
        "postponements_current_step": state.postponements_current_step,
        "recent_task_categories": [cat.value for cat in state.recent_task_categories],
    }
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def load_user_state(file_path: str = "user_state.json") -> UserState:
    """Load UserState from a JSON file."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        state = UserState(
            current_step_id=data.get("current_step_id", ""),
            days_inactive=data.get("days_inactive", 0),
            consecutive_postponements=data.get("consecutive_postponements", 0),
            last_interaction_at=datetime.fromisoformat(data["last_interaction_at"]) if data.get("last_interaction_at") else None,
            last_task_outcome=InteractionType(data["last_task_outcome"]) if data.get("last_task_outcome") else None,
            last_task_completed_at=datetime.fromisoformat(data["last_task_completed_at"]) if data.get("last_task_completed_at") else None,
            postponements_current_step=data.get("postponements_current_step", 0),
            recent_task_categories=[TaskCategory(cat) for cat in data.get("recent_task_categories", [])],
        )
        return state
    except FileNotFoundError:
        # Return a default state if file doesn't exist
        return UserState(
            current_step_id="",
            days_inactive=0,
            consecutive_postponements=0,
            last_interaction_at=None,
            last_task_outcome=None,
            last_task_completed_at=None,
            postponements_current_step=0,
            recent_task_categories=[],
        )