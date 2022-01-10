from typing import Any

from sit_igp_management_backend.api.professors.entities.professor import Professor


def create(professor: Professor) -> Any:
    return {
        "full_name": professor.full_name,
        "email": professor.email,
    }


def find_all() -> Any:
    return None


def find_one(professor_id: int) -> Any:
    return {
        "professor_id": professor_id,
    }


def update(professor_id: int, update_professor_dto: Professor) -> Any:
    return {
        "professor_id": professor_id,
        "full_name": update_professor_dto.full_name,
        "email": update_professor_dto.email,
    }


def remove(professor_id: int) -> Any:
    return {
        "professor_id": professor_id,
    }
