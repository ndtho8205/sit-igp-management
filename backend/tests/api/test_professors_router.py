from starlette import status

from fastapi.testclient import TestClient


def test_create_ok(client: TestClient) -> None:
    professor = {"full_name": "Professor 1", "email": "professor1@shibaura-it.ac.jp"}

    response = client.post("/api/professors/", json=professor)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] > 0
    assert response_body["full_name"] == professor["full_name"]
    assert response_body["email"] == professor["email"]
    assert not response_body["is_verified"]
    assert not response_body["is_superuser"]
    assert not response_body["is_deleted"]


def test_create_missing_required_field(client: TestClient) -> None:
    response = client.post("/api/professors/", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "full_name"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "email"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_create_invalid_university_email(client: TestClient) -> None:
    professor = {"full_name": "Professor 2", "email": "professor2@gmail.com"}

    response = client.post("/api/professors/", json=professor)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "email"],
                "msg": "value is not a SIT-given email address",
                "type": "value_error",
            }
        ]
    }


def test_create_conflict_email(client: TestClient) -> None:
    professor1 = {"full_name": "Professor 3", "email": "professor3@shibaura-it.ac.jp"}
    professor2 = {"full_name": "Professor 4", "email": "professor3@shibaura-it.ac.jp"}

    response = client.post("/api/professors/", json=professor1)
    assert response.status_code == 200

    response = client.post("/api/professors/", json=professor2)
    assert response.status_code == status.HTTP_409_CONFLICT


def test_find_all_ok(client: TestClient) -> None:
    professors = [
        {"full_name": "Professor 5", "email": "professor5@shibaura-it.ac.jp"},
        {"full_name": "Professor 6", "email": "professor6@shibaura-it.ac.jp"},
    ]

    for professor in professors:
        client.post("/api/professors/", json=professor)

    response = client.get("/api/professors/")
    response_body = response.json()

    assert response.status_code == 200
    assert len(response_body) > 1


def test_find_one_by_id_ok(client: TestClient) -> None:
    professor = {"full_name": "Professor 7", "email": "professor7@shibaura-it.ac.jp"}
    response = client.post("/api/professors/", json=professor)
    professor_id = response.json()["id_"]

    response = client.get(f"/api/professors/{professor_id}")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == professor_id
    assert response_body["full_name"] == professor["full_name"]
    assert response_body["email"] == professor["email"]
    assert not response_body["is_verified"]
    assert not response_body["is_superuser"]
    assert not response_body["is_deleted"]


def test_find_one_by_id_not_found(client: TestClient) -> None:
    response = client.get("/api/professors/-1")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_by_id_ok(client: TestClient) -> None:
    professor = {"full_name": "Professor 8", "email": "professor8@shibaura-it.ac.jp"}
    response = client.post("/api/professors/", json=professor)
    professor_id = response.json()["id_"]

    response = client.put(
        f"/api/professors/{professor_id}",
        json={
            "full_name": "Updated Professor 8",
            "is_deleted": True,
            "is_superuser": True,
            "is_verified": True,
        },
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == professor_id
    assert response_body["full_name"] == "Updated Professor 8"
    assert response_body["email"] == professor["email"]
    assert response_body["is_deleted"]
    assert not response_body["is_verified"]
    assert not response_body["is_superuser"]


def test_update_by_id_invalid_email(client: TestClient) -> None:
    professor = {"full_name": "Professor 9", "email": "professor9@shibaura-it.ac.jp"}
    response = client.post("/api/professors/", json=professor)
    professor_id = response.json()["id_"]

    response = client.put(
        f"/api/professors/{professor_id}",
        json={"email": "professor6@\n@gmail.com"},
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_update_by_id_not_found(client: TestClient) -> None:
    response = client.put("/api/professors/-1", json={})

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_ok(client: TestClient) -> None:
    professor = {"full_name": "Professor 10", "email": "professor10@shibaura-it.ac.jp"}
    response = client.post("/api/professors/", json=professor)
    professor_id = response.json()["id_"]

    response = client.delete(f"/api/professors/{professor_id}")

    assert response.status_code == 200

    response = client.get(f"/api/professors/{professor_id}")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == professor_id
    assert response_body["is_deleted"]


def test_find_all_after_delete_ok(client: TestClient) -> None:
    professor = {"full_name": "Professor 11", "email": "professor11@shibaura-it.ac.jp"}
    response = client.post("/api/professors/", json=professor)
    professor_id = response.json()["id_"]

    n_professors_before = len(client.get("/api/professors/").json())
    client.delete(f"/api/professors/{professor_id}")
    n_professors_after = len(client.get("/api/professors/").json())

    assert n_professors_before >= 1
    assert n_professors_before - n_professors_after == 1


def test_delete_not_found(client: TestClient) -> None:
    response = client.delete("/api/professors/-1")

    assert response.status_code == status.HTTP_404_NOT_FOUND
