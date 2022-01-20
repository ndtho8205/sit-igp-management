from backend.usecases.list_all_students import list_all_students
from backend.usecases.delete_presentation import delete_presentation
from backend.usecases.list_all_professors import list_all_professors
from backend.usecases.update_student_info import update_student_info
from backend.usecases.delete_student_record import delete_student_record
from backend.usecases.update_professor_info import update_professor_info
from backend.usecases.list_all_presentations import list_all_presentations
from backend.usecases.verify_professor_email import verify_professor_email
from backend.usecases.create_new_presentation import create_new_presentation
from backend.usecases.delete_professor_record import delete_professor_record
from backend.usecases.update_presentation_info import update_presentation_info
from backend.usecases.create_new_student_record import create_new_student_record
from backend.usecases.create_new_professor_record import create_new_professor_record


__all__ = [
    # professors
    "verify_professor_email",
    "create_new_professor_record",
    "update_professor_info",
    "delete_professor_record",
    "list_all_professors",
    # students
    "create_new_student_record",
    "update_student_info",
    "delete_student_record",
    "list_all_students",
    # presentations
    "create_new_presentation",
    "update_presentation_info",
    "delete_presentation",
    "list_all_presentations",
]
