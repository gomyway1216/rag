from fastapi.testclient import TestClient


def test_bmi(client: TestClient):
    # TODO: Add more test cases
    response = client.post(
        "/bmi",
        json={
            "height": 175,
            "weight": 70,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"bmi": 22.86}
