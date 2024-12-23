from fastapi.testclient import TestClient


def test_bmi(client: TestClient):
    response = client.post(
        "/bmi",
        json={"height": 175, "weight": 70},
    )
    assert response.status_code == 200
    assert response.json() == {"bmi": 22.86}


def test_float_inputs(client: TestClient):
    response = client.post(
        "/bmi",
        json={"height": 162.35, "weight": 45.50},
    )
    assert response.status_code == 200
    assert response.json() == {"bmi": 17.26}


def test_negative_height(client: TestClient):
    response = client.post(
        "/bmi",
        json={"height": -152, "weight": 80},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than_equal",
                "loc": ["body", "height"],
                "msg": "Input should be greater than or equal to 0",
                "input": -152,
                "ctx": {"ge": 0.0},
            }
        ]
    }


def test_negative_weight(client: TestClient):
    response = client.post(
        "/bmi",
        json={"height": 130, "weight": -32},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than_equal",
                "loc": ["body", "weight"],
                "msg": "Input should be greater than or equal to 0",
                "input": -32,
                "ctx": {"ge": 0.0},
            }
        ]
    }


def test_negative_height_and_weight(client: TestClient):
    response = client.post(
        "/bmi",
        json={"height": -193, "weight": -80},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than_equal",
                "loc": ["body", "weight"],
                "msg": "Input should be greater than or equal to 0",
                "input": -80,
                "ctx": {"ge": 0.0},
            },
            {
                "type": "greater_than_equal",
                "loc": ["body", "height"],
                "msg": "Input should be greater than or equal to 0",
                "input": -193,
                "ctx": {"ge": 0.0},
            },
        ]
    }
