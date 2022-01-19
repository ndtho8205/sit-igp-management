from backend.usecases.list_all_students import list_all_students
from backend.usecases.list_all_professors import list_all_professors
from backend.usecases.update_student_info import update_student_info
from backend.usecases.delete_student_record import delete_student_record
from backend.usecases.update_professor_info import update_professor_info
from backend.usecases.verify_professor_email import verify_professor_email
from backend.usecases.delete_professor_record import delete_professor_record
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
]
