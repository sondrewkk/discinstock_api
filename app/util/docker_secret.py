import os


def get_secret(secret_file: str):
    path = os.getenv(secret_file)

    if not path:
        return None

    secret: str
    fallback_env = secret_file[:-5]

    if os.path.exists(path):
        with open(path, "r") as file:
            secret = file.read()
    else:
        secret = os.getenv(fallback_env)

    return secret
