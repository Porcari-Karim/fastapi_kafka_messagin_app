import os
import jwt

class InvalidJWTError(Exception):

    def __init__(self, invalid_jwt: str, message: str) -> None:
        self.invalid_jwt = invalid_jwt
        self.message = message
        super().__init__(message)

def create_jwt_token(payload: dict) -> str:
    key= os.getenv("JWT_ENCRYPTION_KEY")
    encoded_jwt = jwt.encode(payload, key, algorithm="HS256")
    return encoded_jwt


def get_jwt_payload(encoded_jwt: str) -> dict:
    key= os.getenv("JWT_ENCRYPTION_KEY")
    try:
        payload = jwt.decode(encoded_jwt, key, algorithms=["HS256"])
    except jwt.exceptions.DecodeError:
        raise InvalidJWTError(encoded_jwt, f"Failed to decode the jwt it may be invalid. JWT: {encoded_jwt}")
    return payload


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    payload = {
        "pay": "load"
    }
    temp_jwt = create_jwt_token(payload)
    print(temp_jwt)
    print(get_jwt_payload(temp_jwt))
    get_jwt_payload("jdbikfdjk")
    
