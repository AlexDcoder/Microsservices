def check_user_credentials(name: str, files: list):
    for user in files:
        if name == str(user["nome"]):
            password_lenght = len(user['password'])
            if 0 < password_lenght <= 8:
                return True
            return False
    return False
