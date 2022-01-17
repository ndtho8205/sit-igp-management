from starlette import status

from fastapi.testclient import TestClient

from tests.utils import generate_student, generate_professor


def test_create_ok(client: TestClient) -> None:
    reviewer = generate_professor(client)
    presenter = generate_student(client)

    presentation = {
        "student_id": str(presenter.id_),
        "presentation_date": "2022-12-22",
        "reviewer1_id": str(reviewer.id_),
    }
    response = client.post("/api/presentations/", json=presentation)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"]
    assert response_body["student_id"] == presentation["student_id"]
    assert response_body["presentation_date"] == presentation["presentation_date"]
    assert response_body["presentation_length"] is None
    assert response_body["reviewer1_id"] == presentation["reviewer1_id"]
    assert response_body["reviewer2_id"] is None
    assert response_body["reviewer3_id"] is None
    assert response_body["reviewer4_id"] is None
    assert response_body["reviewer5_id"] is None
    assert not response_body["is_deleted"]


def test_create_missing_required_field(client: TestClient) -> None:
    response = client.post("/api/presentations/", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "student_id"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "presentation_date"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_create_student_not_found(client: TestClient, random_id: str) -> None:
    presentation = {
        "student_id": random_id,
        "presentation_date": "2022-12-22",
    }

    response = client.post("/api/presentations/", json=presentation)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "student_id"],
                "msg": "The student was not found",
                "type": "value_error",
            },
        ]
    }


def test_create_reviewers_not_found(client: TestClient, random_id: str) -> None:
    presenter = generate_student(client)

    student = {
        "student_id": str(presenter.id_),
        "presentation_date": "2022-12-22",
        "reviewer1_id": random_id,
        "reviewer2_id": random_id,
        "reviewer3_id": random_id,
        "reviewer4_id": random_id,
        "reviewer5_id": random_id,
    }

    response = client.post("/api/presentations/", json=student)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "reviewer1_id"],
                "msg": "The reviewer 1 was not found",
                "type": "value_error",
            },
            {
                "loc": ["body", "reviewer2_id"],
                "msg": "The reviewer 2 was not found",
                "type": "value_error",
            },
            {
                "loc": ["body", "reviewer3_id"],
                "msg": "The reviewer 3 was not found",
                "type": "value_error",
            },
            {
                "loc": ["body", "reviewer4_id"],
                "msg": "The reviewer 4 was not found",
                "type": "value_error",
            },
            {
                "loc": ["body", "reviewer5_id"],
                "msg": "The reviewer 5 was not found",
                "type": "value_error",
            },
        ]
    }


def test_find_all_ok(client: TestClient) -> None:
    presenter = generate_student(client)

    presentations = [
        {"student_id": str(presenter.id_), "presentation_date": "2022-12-22"},
        {"student_id": str(presenter.id_), "presentation_date": "2022-12-22"},
    ]
    for presentation in presentations:
        client.post("/api/presentations/", json=presentation)

    response = client.get("/api/presentations/")
    response_body = response.json()

    assert response.status_code == 200
    assert len(response_body) > 1


def test_find_one_by_id_ok(client: TestClient) -> None:
    presenter = generate_student(client)

    presentation = {"student_id": str(presenter.id_), "presentation_date": "2022-12-22"}
    response = client.post("/api/presentations/", json=presentation)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["student_id"] == presentation["student_id"]
    assert response_body["presentation_date"] == presentation["presentation_date"]
    assert response_body["presentation_length"] is None
    assert response_body["reviewer1_id"] is None
    assert response_body["reviewer2_id"] is None
    assert response_body["reviewer3_id"] is None
    assert response_body["reviewer4_id"] is None
    assert response_body["reviewer5_id"] is None
    assert not response_body["is_deleted"]


def test_find_one_by_id_not_found(client: TestClient, random_id: str) -> None:
    response = client.get(f"/api/presentations/{random_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_by_id_ok(client: TestClient) -> None:
    reviewer = generate_professor(client)
    presenter = generate_student(client)

    presentation = {"student_id": str(presenter.id_), "presentation_date": "2022-12-22"}
    response = client.post("/api/presentations/", json=presentation)
    presentation_id = response.json()["id_"]

    response = client.put(
        f"/api/presentations/{presentation_id}",
        json={
            "presentation_date": "3333-12-22",
            "is_deleted": True,
            "random_key": True,
            "reviewer1_id": str(reviewer.id_),
        },
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == str(presentation_id)
    assert response_body["presentation_date"] == "3333-12-22"
    assert response_body["reviewer1_id"] == str(reviewer.id_)
    assert response_body["reviewer2_id"] is None
    assert response_body["is_deleted"]
    assert "random_key" not in response_body


def test_update_by_id_reviewer_not_found(client: TestClient, random_id: str) -> None:
    presenter = generate_student(client)

    presentation = {"student_id": str(presenter.id_), "presentation_date": "2022-12-22"}
    response = client.post("/api/presentations/", json=presentation)
    presentation_id = response.json()["id_"]

    response = client.put(
        f"/api/presentations/{presentation_id}",
        json={"reviewer1_id": random_id},
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_update_by_id_not_found(client: TestClient, random_id: str) -> None:
    response = client.put(f"/api/presentations/{random_id}", json={})

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_ok(client: TestClient) -> None:
    presenter = generate_student(client)
    presentation = {"student_id": str(presenter.id_), "presentation_date": "2022-12-22"}
    response = client.post("/api/presentations/", json=presentation)
    presentation_id = response.json()["id_"]

    response = client.delete(f"/api/presentations/{presentation_id}")

    assert response.status_code == 200

    response = client.get(f"/api/presentations/{presentation_id}")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == presentation_id
    assert response_body["is_deleted"]


def test_find_all_after_delete_ok(client: TestClient) -> None:
    presenter = generate_student(client)
    presentation = {"student_id": str(presenter.id_), "presentation_date": "2022-12-22"}
    response = client.post("/api/presentations/", json=presentation)
    presentation_id = response.json()["id_"]

    n_presentations_before = len(client.get("/api/presentations/").json())
    client.delete(f"/api/presentations/{presentation_id}")
    n_presentations_after = len(client.get("/api/presentations/").json())

    assert n_presentations_before >= 1
    assert n_presentations_before - n_presentations_after == 1


def test_delete_not_found(client: TestClient, random_id: str) -> None:
    response = client.delete(f"/api/presentations/{random_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
