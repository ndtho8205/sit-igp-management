from typing import Any

from fastapi import APIRouter

from sit_igp_management_backend.api.professors import professors_service
from sit_igp_management_backend.api.professors.entities.professor import Professor


router = APIRouter(prefix="/professors")


@router.post("/")
def create(professor: Professor) -> Any:
    return professors_service.create(professor)


@router.get("/")
def find_all() -> Any:
    return professors_service.find_all()


@router.get("/{professor_id}")
def find_one(professor_id: int) -> Any:
    return professors_service.find_one(professor_id)


@router.put("/{professor_id}")
def update(professor_id: int, update_professor_dto: Professor) -> Any:
    return professors_service.update(professor_id, update_professor_dto)


@router.delete("/{professor_id}")
def remove(professor_id: int) -> Any:
    return professors_service.remove(professor_id)
