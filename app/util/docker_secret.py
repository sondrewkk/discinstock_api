import os


def get_secret(secret_file: str):
    path = os.getenv(secret_file)

    if path and os.path.exists(path):
        with open(path, "r") as file:
            secret = file.read()
    else:
        fallback_env = secret_file[:-5]
        secret = os.getenv(fallback_env)

    return secret
