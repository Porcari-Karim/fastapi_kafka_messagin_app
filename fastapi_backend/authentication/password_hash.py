import hashlib
import os

def hash_password(password: str) -> str:
    salt = os.getenv("PASSWORD_ENCRYPTION_KEY")
    password += salt
    hashed_password = hashlib.md5(password.encode())
    return hashed_password.hexdigest()

def check_password_match(raw_password: str, hashed_password: str) -> bool:
    return hash_password(raw_password) == hashed_password


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    pwd = hash_password("MonMotDePasse")
    print(check_password_match("MonMotDePasse", pwd))

