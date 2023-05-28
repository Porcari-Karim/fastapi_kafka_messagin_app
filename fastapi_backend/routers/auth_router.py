from fastapi import APIRouter, Depends, Response, Request
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from dependencies.auth_dep import requires_connected
from models.jwt_payload import JWTPayload
from models.user import User
from models.user_login_info import UserLoginInfo
from authentication.password_hash import check_password_match, hash_password
from authentication.jwt_auth import create_jwt_token
from database.mongo import connect_to_db
from fastapi.templating import Jinja2Templates


auth_router = APIRouter(prefix="/auth")

templates = Jinja2Templates(directory="templates")

@auth_router.get("/is_connected")
async def is_connected(user_payload: JWTPayload = Depends(requires_connected)) -> Response:
    if user_payload.id == 0 and user_payload.username == "Anonymous":
        return Response(status_code=401)
    return Response(status_code=200, content="Blblabma")


@auth_router.get('/register')
async def register(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("register.html", context={"request": request})



@auth_router.post("/register")
async def register_post(user_info = Depends(User.as_form)) -> RedirectResponse:
    db = await connect_to_db("messaging_app")
    #users_collection = db["users"]
    user_info.password = hash_password(user_info.password)
    db_result = await db.users.insert_one(user_info.dict(exclude={"_id"}))
    payload = JWTPayload(id=str(db_result.inserted_id), username=f"{user_info.first_name} {user_info.last_name}")
    response = RedirectResponse("/", status_code=303)
    response.set_cookie("jwt_auth", create_jwt_token(payload.dict()), httponly=True, expires=2_592_000)
    return response

@auth_router.get("/logout")
async def login(request: Request) -> RedirectResponse:
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("jwt_auth")
    response.set_cookie("jwt_auth", "", httponly=True, expires=-2_592_000)
    return response

@auth_router.get('/login')
async def register(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("login.html", context={"request": request})

@auth_router.post("/login")
async def login(request: Request, user_info = Depends(UserLoginInfo.as_form)) -> Response:
    db = await connect_to_db("messaging_app")
    db_response = await db.users.find_one({"e_mail": user_info.e_mail})
    if db_response is None:
        return templates.TemplateResponse("login.html", context={"request": request, "message": "Incorrect username or password"})
    print(db_response)
    id=str(db_response["_id"])
    db_response.pop("_id")
    db_response["id"] = id
    user = User(**db_response)
    if check_password_match(user_info.password, user.password):
        payload = JWTPayload(id=user.id, username=f"{user.first_name} {user.last_name}")
        response = RedirectResponse("/", status_code=303)
        response.set_cookie("jwt_auth", create_jwt_token(payload.dict()), httponly=True, expires=2_592_000)
        return response
    return templates.TemplateResponse("login.html", context={"request": request, "message": "Incorrect username or password"})


