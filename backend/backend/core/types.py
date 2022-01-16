import enum

from pydantic import UUID4, EmailStr, ConstrainedStr
from pydantic.types import ConstrainedInt
from pydantic.networks import validate_email

from backend.core.validators import validate_university_email


ID = UUID4


class ShortStr(ConstrainedStr):
    min_length = 1
    strip_whitespace = True
    max_length = 256


class FullName(ShortStr):
    pass


class UniversityEmailStr(EmailStr):
    @classmethod
    def validate(cls, value: str) -> str:
        email = validate_email(value)[1]
        validate_university_email(email)
        return email


class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class ScoreInt(ConstrainedInt):
    ge = 1
    le = 5
