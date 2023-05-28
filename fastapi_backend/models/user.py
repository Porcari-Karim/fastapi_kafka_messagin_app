from pydantic import BaseModel, EmailStr, Field
from typing import Self
from fastapi import Form




class User(BaseModel):
    id: str | None
    first_name: str
    last_name: str
    e_mail: EmailStr
    password: str

    @classmethod
    def as_form(cls, 
    first_name: str = Form(),
    last_name: str = Form(),
    e_mail: EmailStr = Form(),
    password: str = Form(),
    ) -> Self:
        return cls(
            id=None,
            first_name=first_name,
            last_name=last_name,
            e_mail=e_mail,
            password=password)

    