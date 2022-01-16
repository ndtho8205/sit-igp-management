from starlette import status

from fastapi.testclient import TestClient

from tests.utils import generate_student, generate_professor, generate_presentation


def test_create_ok(client: TestClient) -> None:
    presentation = generate_presentation(client)

    evaluation = {
        "presentation_id": str(presentation.id_),
        "reviewer_id": str(presentation.reviewer1_id),
        "score_research_goal": 5,
        "score_delivery": 5,
        "score_visual_aid": 5,
        "score_time": 5,
        "score_qa": 5,
        "comment": "this is a comment",
    }
    response = client.post("/api/presentation_evaluations/", json=evaluation)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"]
    assert response_body["presentation_id"] == evaluation["presentation_id"]
    assert response_body["reviewer_id"] == evaluation["reviewer_id"]
    assert response_body["score_research_goal"] == evaluation["score_research_goal"]
    assert response_body["score_delivery"] == evaluation["score_delivery"]
    assert response_body["score_visual_aid"] == evaluation["score_visual_aid"]
    assert response_body["score_time"] == evaluation["score_time"]
    assert response_body["score_qa"] == evaluation["score_qa"]
    assert response_body["comment"] == evaluation["comment"]


def test_create_missing_required_field(client: TestClient) -> None:
    response = client.post("/api/presentation_evaluations/", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "presentation_id"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "reviewer_id"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "score_research_goal"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "score_delivery"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "score_visual_aid"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "score_time"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "score_qa"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_create_presentation_not_found(client: TestClient, random_id: str) -> None:
    evaluation = {
        "presentation_id": random_id,
        "reviewer_id": random_id,
        "score_research_goal": 5,
        "score_delivery": 5,
        "score_visual_aid": 5,
        "score_time": 5,
        "score_qa": 5,
        "comment": "this is a comment",
    }

    response = client.post("/api/presentation_evaluations/", json=evaluation)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_reviewer_not_found(client: TestClient, random_id: str) -> None:
    presentation = generate_presentation(client)

    evaluation = {
        "presentation_id": presentation.id_,
        "reviewer_id": random_id,
        "score_research_goal": 5,
        "score_delivery": 5,
        "score_visual_aid": 5,
        "score_time": 5,
        "score_qa": 5,
        "comment": "this is a comment",
    }

    response = client.post("/api/presentation_evaluations/", json=evaluation)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "reviewer_id"],
                "msg": "The presentation's reviewer was not found",
                "type": "value_error",
            },
        ]
    }


def test_create_invalid_scores(client: TestClient) -> None:
    presentation = generate_presentation(client)

    evaluation = {
        "presentation_id": presentation.id_,
        "reviewer_id": presentation.reviewer1_id,
        "score_research_goal": -1,
        "score_delivery": 6,
        "score_visual_aid": -1,
        "score_time": 6,
        "score_qa": 0,
        "comment": "this is a comment",
    }

    response = client.post("/api/presentation_evaluations/", json=evaluation)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "ctx": {"limit_value": 1},
                "loc": ["body", "score_research_goal"],
                "msg": "ensure this value is greater than or equal to 1",
                "type": "value_error.number.not_ge",
            },
            {
                "ctx": {"limit_value": 5},
                "loc": ["body", "score_delivery"],
                "msg": "ensure this value is less than or equal to 5",
                "type": "value_error.number.not_le",
            },
            {
                "ctx": {"limit_value": 1},
                "loc": ["body", "score_visual_aid"],
                "msg": "ensure this value is greater than or equal to 1",
                "type": "value_error.number.not_ge",
            },
            {
                "ctx": {"limit_value": 5},
                "loc": ["body", "score_time"],
                "msg": "ensure this value is less than or equal to 5",
                "type": "value_error.number.not_le",
            },
            {
                "ctx": {"limit_value": 1},
                "loc": ["body", "score_qa"],
                "msg": "ensure this value is greater than or equal to 1",
                "type": "value_error.number.not_ge",
            },
        ]
    }


def test_create_conflict(client: TestClient) -> None:
    presentation = generate_presentation(client)

    evaluation = {
        "presentation_id": presentation.id_,
        "reviewer_id": presentation.reviewer1_id,
        "score_research_goal": 1,
        "score_delivery": 1,
        "score_visual_aid": 1,
        "score_time": 1,
        "score_qa": 1,
    }
    client.post("/api/presentation_evaluations/", json=evaluation)

    response = client.post("/api/presentation_evaluations/", json=evaluation)

    assert response.status_code == status.HTTP_409_CONFLICT


def test_find_all_evaluations_per_presentation_ok(client: TestClient) -> None:
    presenter = generate_student(client)
    reviewer1 = generate_professor(client)
    reviewer2 = generate_professor(client)
    reviewer3 = generate_professor(client)
    reviewer4 = generate_professor(client)
    reviewer5 = generate_professor(client)
    presentation = {
        "student_id": str(presenter.id_),
        "reviewer1_id": str(reviewer1.id_),
        "reviewer2_id": str(reviewer2.id_),
        "reviewer3_id": str(reviewer3.id_),
        "reviewer4_id": str(reviewer4.id_),
        "reviewer5_id": str(reviewer5.id_),
        "presentation_date": "2022-12-22",
    }
    response = client.post("/api/presentations/", json=presentation)
    presentation_id = response.json()["id_"]

    for reviewer in [reviewer1, reviewer2, reviewer3, reviewer4, reviewer5]:
        evaluation = {
            "presentation_id": str(presentation_id),
            "reviewer_id": str(reviewer.id_),
            "score_research_goal": 1,
            "score_delivery": 1,
            "score_visual_aid": 1,
            "score_time": 1,
            "score_qa": 1,
        }
        client.post("/api/presentation_evaluations/", json=evaluation)

    response = client.get(f"/api/presentation_evaluations/{presentation_id}")
    response_body = response.json()

    assert response.status_code == 200
    assert len(response_body) == 5


def test_find_one_by_id_ok(client: TestClient) -> None:
    presentation = generate_presentation(client)

    evaluation = {
        "presentation_id": str(presentation.id_),
        "reviewer_id": str(presentation.reviewer1_id),
        "score_research_goal": 1,
        "score_delivery": 1,
        "score_visual_aid": 1,
        "score_time": 1,
        "score_qa": 1,
    }
    client.post("/api/presentation_evaluations/", json=evaluation)

    response = client.get(
        "/api/presentation_evaluations/"
        f"?presentation_id={presentation.id_}&reviewer_id={presentation.reviewer1_id}"
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"]
    assert response_body["presentation_id"] == evaluation["presentation_id"]
    assert response_body["reviewer_id"] == evaluation["reviewer_id"]


def test_find_one_by_id_not_found(client: TestClient, random_id: str) -> None:
    response = client.get(
        "/api/presentation_evaluations/"
        f"?presentation_id={random_id}&reviewer_id={random_id}"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_by_id_ok(client: TestClient) -> None:
    presentation = generate_presentation(client)
    evaluation = {
        "presentation_id": str(presentation.id_),
        "reviewer_id": str(presentation.reviewer1_id),
        "score_research_goal": 1,
        "score_delivery": 1,
        "score_visual_aid": 1,
        "score_time": 1,
        "score_qa": 1,
    }

    response = client.post("/api/presentation_evaluations/", json=evaluation)
    evaluation_id = response.json()["id_"]

    response = client.put(
        f"/api/presentation_evaluations/{evaluation_id}",
        json={"score_research_goal": 2},
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == str(evaluation_id)
    assert response_body["score_research_goal"] == 2
    assert not response_body["is_deleted"]


def test_update_by_id_not_found(client: TestClient, random_id: str) -> None:
    response = client.put(f"/api/presentation_evaluations/{random_id}", json={})

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_ok(client: TestClient) -> None:
    presentation = generate_presentation(client)
    evaluation = {
        "presentation_id": str(presentation.id_),
        "reviewer_id": str(presentation.reviewer1_id),
        "score_research_goal": 1,
        "score_delivery": 1,
        "score_visual_aid": 1,
        "score_time": 1,
        "score_qa": 1,
    }

    response = client.post("/api/presentation_evaluations/", json=evaluation)
    evaluation_id = response.json()["id_"]

    response = client.delete(f"/api/presentation_evaluations/{evaluation_id}")

    assert response.status_code == 200

    response = client.get(
        "/api/presentation_evaluations/"
        f"?presentation_id={presentation.id_}&reviewer_id={presentation.reviewer1_id}"
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id_"] == evaluation_id
    assert response_body["is_deleted"]


def test_find_all_evaluations_per_presentation_after_delete_ok(
    client: TestClient,
) -> None:
    presentation = generate_presentation(client)
    evaluation = {
        "presentation_id": str(presentation.id_),
        "reviewer_id": str(presentation.reviewer1_id),
        "score_research_goal": 1,
        "score_delivery": 1,
        "score_visual_aid": 1,
        "score_time": 1,
        "score_qa": 1,
    }

    response = client.post("/api/presentation_evaluations/", json=evaluation)
    evaluation_id = response.json()["id_"]

    n_presentation_evaluations_before = len(
        client.get(f"/api/presentation_evaluations/{presentation.id_}").json()
    )
    client.delete(f"/api/presentation_evaluations/{evaluation_id}")
    n_presentation_evaluations_after = len(
        client.get(f"/api/presentation_evaluations/{presentation.id_}").json()
    )

    assert n_presentation_evaluations_before >= 1
    assert n_presentation_evaluations_before - n_presentation_evaluations_after == 1


def test_delete_not_found(client: TestClient, random_id: str) -> None:
    response = client.delete(f"/api/presentation_evaluations/{random_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
