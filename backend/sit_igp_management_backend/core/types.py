from pydantic import ConstrainedStr


class FullName(ConstrainedStr):
    min_length = 1
    max_length = 256
    strip_whitespace = True
