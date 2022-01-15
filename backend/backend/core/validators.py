def validate_university_email(email: str) -> str:
    error = ValueError("value is not a SIT-given email address")

    if len(email) > 256:
        raise error

    at_index = email.index("@")
    email_domain = email[at_index:].lower()
    if email_domain != "@shibaura-it.ac.jp":
        raise error

    return email
