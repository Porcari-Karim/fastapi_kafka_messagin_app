from fastapi import FastAPI, Depends, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from dependencies.auth_dep import requires_connected

from models.jwt_payload import JWTPayload
from routers.auth_router import auth_router
from routers.room_router import room_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(room_router)
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    load_dotenv()

@app.get("/")
async def index(request: Request, user_data: JWTPayload = Depends(requires_connected)) -> JWTPayload:
    return templates.TemplateResponse("index.html", {"request": request, "user_data": user_data, "rooms": []})
    

