import copy

import pytest

from src.app import activities

_initial_activities = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activity state before each test."""
    activities.clear()
    activities.update(copy.deepcopy(_initial_activities))
    yield
