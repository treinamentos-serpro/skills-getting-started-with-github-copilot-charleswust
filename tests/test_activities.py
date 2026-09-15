def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_initial_activity_data(client):
    response = client.get("/activities")

    assert response.status_code == 200

    activities = response.json()
    assert len(activities) == 9
    assert activities["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]
    assert activities["Basketball Team"]["participants"] == []
    assert all(
        {"description", "schedule", "max_participants", "participants"}
        <= activity.keys()
        for activity in activities.values()
    )
