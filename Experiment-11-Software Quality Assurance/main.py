from login import validate_login

username = input("Username: ")
password = input("Password: ")

print(validate_login(username, password))