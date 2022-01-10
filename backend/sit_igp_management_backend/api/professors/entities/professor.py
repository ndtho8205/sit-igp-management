from pydantic import BaseModel


class Professor(BaseModel):
    """Professor."""

    full_name: str
    email: str
