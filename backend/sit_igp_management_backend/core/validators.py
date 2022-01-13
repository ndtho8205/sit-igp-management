def validate_university_email(email: str) -> str:
    at_index = email.index("@")
    email_domain = email[at_index:].lower()
    if email_domain != "@shibaura-it.ac.jp":
        raise ValueError("value is not a SIT-given email address")
    return email
