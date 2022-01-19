from typing import Optional

from backend.usecases.inputs import ProfessorUpdateInput
from backend.entities.professor import Professor
from backend.usecases.repositories.professor_repository import ProfessorRepository


def verify_professor_email(
    professor_repository: ProfessorRepository,
    email: str,
) -> Optional[Professor]:
    professor = professor_repository.find_one_by_email(email)

    if professor is None:
        return None

    if not professor.is_verified:
        inp = ProfessorUpdateInput(is_verified=True)
        professor_repository.update(professor.id_, inp)

    return professor
