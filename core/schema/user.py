from pydantic import BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    id: int
    email: str
    password: str


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=7)


class SigninUserSchema(BaseModel):
    email: str
    access_token: str

