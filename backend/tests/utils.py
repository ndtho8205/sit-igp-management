import random
import string

from fastapi.testclient import TestClient

from backend.api.students.students_entities import Student
from backend.api.professors.professors_entities import Professor


def random_str() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))  # noqa: S311


def generate_professor(client: TestClient) -> Professor:
    professor_name = random_str()
    create_dto = {
        "full_name": f"Professor {professor_name}",
        "email": f"{professor_name}@shibaura-it.ac.jp",
    }
    response = client.post("/api/professors/", json=create_dto)
    return Professor(**response.json())


def generate_student(client: TestClient) -> Student:
    create_dto = {
        "full_name": "Student",
        "admission_date": "2022-12-22",
    }
    response = client.post("/api/students/", json=create_dto)
    return Student(**response.json())
