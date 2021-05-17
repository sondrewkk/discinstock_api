import os

def get_secret(secret_file: str):
    secret: str
    fallback_env = secret_file[:-5]

    if os.path.exists(secret_file):
      with open(secret_file, "r") as file:
        secret = file.read()
    else:
      secret = os.getenv(fallback_env)
    
    return secret
