from fastapi.testclient import TestClient


def test_home(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
