import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = {
        name: {**activity, "participants": activity["participants"].copy()}
        for name, activity in activities.items()
    }

    yield

    activities.clear()
    activities.update(original_activities)
