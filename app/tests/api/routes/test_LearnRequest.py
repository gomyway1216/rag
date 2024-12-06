from fastapi.testclient import TestClient


def test_LearnRequest1(client: TestClient):
    response = client.post(
        "/learn",
        json={
            "text": "dog",
        },
    )
    assert response.status_code == 422


def test_LearnRequest2(client: TestClient):
    response = client.post(
        "/learn",
        json={
            "text": "cats",
        },
    )
    assert response.status_code == 204


def test_LearnRequest3(client: TestClient):
    response = client.post(
        "/learn",
        json={
            "text": "The family on my father's side is descended from Caspar Keller, a native of Switzerland, who settled in Maryland.",
        },
    )
    assert response.status_code == 204


def test_LearnRequest4(client: TestClient):
    response = client.post(
        "/learn",
        json={
            "text": "The family on my father's side is descended from Caspar Keller, a native of Switzerland, who settled in Maryland. One of my Swiss ancestors was the first teacher of the deaf in Zurich and wrote a book on the subject of their education—rather a singular coincidence; though it is true that there is no king who has not had a slave among his ancestors, and no slave who has not had a king among his. \n My grandfather, Caspar Keller's son, \"entered\" large tracts of land in Alabama and finally settled there. I have been told that once a year he went from Tuscumbia to Philadelphia on horseback to purchase supplies for the plantation, and my aunt has in her possession many of the letters to his family, which give charming and vivid accounts of these trips. \n My Grandmother Keller was a daughter of one of Lafayette's aides, Alexander Moore, and granddaughter of Alexander Spotswood, an early Colonial Governor of Virginia. She was also second cousin to Robert E. Lee.",
        },
    )
    assert response.status_code == 204
