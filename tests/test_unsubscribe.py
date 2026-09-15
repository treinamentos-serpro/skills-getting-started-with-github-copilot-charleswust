from src.app import activities


def test_student_can_remove_signup(client):
    email = "student@mergington.edu"
    activity_name = "Basketball Team"

    client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {email} from {activity_name}"
    }
    assert email not in activities[activity_name]["participants"]
