import enum

from pydantic import UUID4, EmailStr, ConstrainedStr
from pydantic.types import ConstrainedInt, ConstrainedFloat
from pydantic.networks import validate_email


ID = UUID4


class ShortStr(ConstrainedStr):
    min_length = 1
    strip_whitespace = True
    max_length = 256


class LongStr(ConstrainedStr):
    min_length = 1
    strip_whitespace = True
    max_length = 2048


class FullName(ShortStr):
    pass


class UniversityEmailStr(EmailStr):
    @classmethod
    def validate(cls, value: str) -> str:
        email = validate_email(value)[1]
        # validate_university_email(email)
        return email


class RatingScore(ConstrainedInt):
    ge = 1
    le = 5


class Score(ConstrainedFloat):
    ge = 0.0
    le = 100.0


class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class StudentYear(str, enum.Enum):
    FIRST = "Freshmen"
    SECOND = "Sophomore"
    THIRD = "Junior"
    FOURTH = "Senior"


class StudentSemester(str, enum.Enum):
    FIRST = "I"
    SECOND = "II"


def validate_university_email(email: str) -> str:
    error = ValueError("value is not a SIT-given email address")

    if len(email) > 256:
        raise error

    at_index = email.index("@")
    email_domain = email[at_index:].lower()
    if email_domain != "@shibaura-it.ac.jp":
        raise error

    return email
