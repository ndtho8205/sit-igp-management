from fastapi import status
from fastapi.testclient import TestClient


def test_api_status(client: TestClient) -> None:
    response = client.get("/api/status")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "Ok"}
