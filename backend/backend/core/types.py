import enum

from pydantic import EmailStr, ConstrainedStr
from pydantic.networks import validate_email

from backend.core.validators import validate_university_email


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
