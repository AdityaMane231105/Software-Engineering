from login import validate_login


def test_valid_login():
    assert validate_login("admin", "admin123") == "Valid Login"


def test_wrong_password():
    assert validate_login("admin", "wrongpass") == "Invalid Login"


def test_unknown_user():
    assert validate_login("xyz", "123456") == "Invalid Login"


def test_empty_username():
    assert validate_login("", "admin123") == "Error: Username required"


def test_short_password():
    assert validate_login("admin", "abcde") == "Error: Password length must be 6 to 12"


def test_long_password():
    assert validate_login("admin", "abcdefghijklm") == "Error: Password length must be 6 to 12"
