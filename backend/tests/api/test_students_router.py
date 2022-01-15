from starlette import status

from fastapi.testclient import TestClient


def test_create_ok(client: TestClient) -> None:
    supervisor = {
        "full_name": "Supervisor 1",
        "email": "supervisor1@shibaura-it.ac.jp",
    }
    response = client.post("/api/professors/", json=supervisor)
    supervisor_id = response.json()["id_"]

    student = {
        "full_name": "Student 1",
        "admission_date": "2022-12-22",
        "email": "student1@shibaura-it.ac.jp",
        "supervisor_id": supervisor_id,
    }

    response = client.post("/api/students/", json=student)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] > 0
    assert response_body["full_name"] == student["full_name"]
    assert response_body["email"] == student["email"]
    assert response_body["admission_date"] == student["admission_date"]
    assert response_body["supervisor_id"] is supervisor_id
    assert response_body["gender"] is None
    assert response_body["area_of_study"] is None
    assert response_body["advisor1_id"] is None
    assert response_body["advisor2_id"] is None
    assert not response_body["is_deleted"]


def test_create_missing_required_field(client: TestClient) -> None:
    response = client.post("/api/students/", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "full_name"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "admission_date"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_create_invalid_admission_date_and_university_email(client: TestClient) -> None:
    student = {
        "full_name": "Student 2",
        "admission_date": "2022-22-22",
        "email": "student2@gmail.com",
    }

    response = client.post("/api/students/", json=student)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "email"],
                "msg": "value is not a SIT-given email address",
                "type": "value_error",
            },
            {
                "loc": ["body", "admission_date"],
                "msg": "invalid date format",
                "type": "value_error.date",
            },
        ]
    }


def test_create_conflict_email(client: TestClient) -> None:
    student1 = {
        "full_name": "Student 3",
        "admission_date": "2022-12-22",
        "email": "student3@shibaura-it.ac.jp",
    }
    student2 = {
        "full_name": "Student 4",
        "admission_date": "2022-12-22",
        "email": "student3@shibaura-it.ac.jp",
    }

    response = client.post("/api/students/", json=student1)
    assert response.status_code == 200

    response = client.post("/api/students/", json=student2)
    assert response.status_code == status.HTTP_409_CONFLICT


def test_create_supervisor_not_found(client: TestClient) -> None:
    student = {
        "full_name": "Student 5",
        "admission_date": "2022-12-22",
        "supervisor_id": -1,
        "advisor1_id": -1,
        "advisor2_id": -1,
    }

    response = client.post("/api/students/", json=student)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_find_all_ok(client: TestClient) -> None:
    students = [
        {"full_name": "Student 6", "admission_date": "2022-12-22"},
        {"full_name": "Student 7", "admission_date": "2022-12-22"},
    ]

    for student in students:
        client.post("/api/students/", json=student)

    response = client.get("/api/students/")
    response_body = response.json()

    assert response.status_code == 200
    assert len(response_body) > 1


def test_find_one_by_id_ok(client: TestClient) -> None:
    student = {"full_name": "Student 8", "admission_date": "2022-12-22"}
    response = client.post("/api/students/", json=student)
    student_id = response.json()["id_"]

    response = client.get(f"/api/students/{student_id}")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] > 0
    assert response_body["full_name"] == student["full_name"]
    assert response_body["email"] is None
    assert response_body["admission_date"] == student["admission_date"]
    assert response_body["gender"] is None
    assert response_body["area_of_study"] is None
    assert response_body["supervisor_id"] is None
    assert response_body["advisor1_id"] is None
    assert response_body["advisor2_id"] is None
    assert not response_body["is_deleted"]


def test_find_one_by_id_not_found(client: TestClient) -> None:
    response = client.get("/api/students/-1")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_by_id_ok(client: TestClient) -> None:
    student = {"full_name": "Student 9", "admission_date": "2022-12-22"}
    response = client.post("/api/students/", json=student)
    student_id = response.json()["id_"]

    response = client.put(
        f"/api/students/{student_id}",
        json={
            "full_name": "Updated Student 9",
            "is_deleted": True,
            "random_key": True,
        },
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == student_id
    assert response_body["full_name"] == "Updated Student 9"
    assert response_body["email"] is None
    assert response_body["is_deleted"]


def test_update_by_id_supervisor_not_found(client: TestClient) -> None:
    student = {"full_name": "Student 10", "admission_date": "2022-12-22"}
    response = client.post("/api/students/", json=student)
    student_id = response.json()["id_"]

    response = client.put(
        f"/api/students/{student_id}",
        json={"supervisor_id": -1},
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_update_by_id_not_found(client: TestClient) -> None:
    response = client.put("/api/students/-1", json={})

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_ok(client: TestClient) -> None:
    student = {"full_name": "Student 11", "admission_date": "2022-12-22"}
    response = client.post("/api/students/", json=student)
    student_id = response.json()["id_"]

    response = client.delete(f"/api/students/{student_id}")

    assert response.status_code == 200

    response = client.get(f"/api/students/{student_id}")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == student_id
    assert response_body["is_deleted"]


def test_find_all_after_delete_ok(client: TestClient) -> None:
    student = {"full_name": "Student 12", "admission_date": "2022-12-22"}
    response = client.post("/api/students/", json=student)
    student_id = response.json()["id_"]

    n_students_before = len(client.get("/api/students/").json())
    client.delete(f"/api/students/{student_id}")
    n_students_after = len(client.get("/api/students/").json())

    assert n_students_before >= 1
    assert n_students_before - n_students_after == 1


def test_delete_not_found(client: TestClient) -> None:
    response = client.delete("/api/students/-1")

    assert response.status_code == status.HTTP_404_NOT_FOUND
