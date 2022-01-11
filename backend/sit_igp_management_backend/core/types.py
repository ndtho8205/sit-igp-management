import enum

from pydantic import ConstrainedStr


class ShortStr(ConstrainedStr):
    min_length = 1
    max_length = 256
    strip_whitespace = True


class FullName(ConstrainedStr):
    pass


class Gender(enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
