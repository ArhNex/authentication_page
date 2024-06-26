from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import BaseModel
from typing import List
from pydantic import Field
from datetime import datetime
from enum import Enum
from typing import Optional

from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.database import User
from auth.manager import get_user_manager

app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)