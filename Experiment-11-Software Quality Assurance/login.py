"""Login validation for the SQA Experiment 11 project."""

USERS = {"admin": "admin123", "student": "stud@1"}


def validate_login(username, password):
    """Check credentials and return the appropriate login result."""
    if not username:
        return "Error: Username required"

    if not 6 <= len(password) <= 12:
        return "Error: Password length must be 6 to 12"

    if username in USERS and USERS[username] == password:
        return "Valid Login"

    return "Invalid Login"
