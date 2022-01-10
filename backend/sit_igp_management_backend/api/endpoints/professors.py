from typing import Any

from pydantic import BaseModel

from fastapi import APIRouter


router = APIRouter()


class Professor(BaseModel):
    """Professor."""

    full_name: str
    email: str


@router.get("/professors/{professor_id}")
def read_professor(professor_id: int) -> Any:
    return {"professor_id": professor_id}


@router.put("/professors/{professor_id")
def update_professor(professor_id: int, professor: Professor) -> Any:
    return {
        "full_name": professor.full_name,
        "professor_id": professor_id,
        "email": professor.email,
    }


@router.get("/professors/{professor_id}/students/{student_id}")
def read_professor_student(professor_id: int, student_id: int) -> Any:
    return {"professor_id": professor_id, "student_id": student_id}
