from authentication.jwt_auth import get_jwt_payload, InvalidJWTError
from models.jwt_payload import JWTPayload
from fastapi import Request, Depends, HTTPException



async def is_user_connected(request: Request) -> JWTPayload | None:
    raw_jwt = request.cookies.get("jwt_auth", None)
    if raw_jwt is None:
        return None
    try:
        payload = get_jwt_payload(raw_jwt)
    except InvalidJWTError:
        return None
    
    return JWTPayload(**payload)


async def requires_connected(user_info = Depends(is_user_connected)) -> JWTPayload:
    if user_info is None:
        raise HTTPException(status_code=401, detail="Access Denied")
    return user_info

