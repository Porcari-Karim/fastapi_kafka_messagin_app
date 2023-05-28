from pydantic import BaseModel, EmailStr
from typing import Self
from fastapi import Form


class UserLoginInfo(BaseModel):
    e_mail: EmailStr
    password: str

    @classmethod
    def as_form(cls,
                e_mail: EmailStr = Form(),
                password: str = Form()
                ) -> Self:       
        return cls(e_mail=e_mail, password=password)
