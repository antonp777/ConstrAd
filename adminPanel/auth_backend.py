from typing import Annotated, Union

from fastapi import Depends
from sqladmin.authentication import AuthenticationBackend
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import RedirectResponse

from core.models import db_helper
from crud.userService import get_token_by_login_password, get_user_service_by_login


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        login, password = form["username"], form["password"]

        # Validate username/password credentials
        # And update session

        async with db_helper.session_factory() as session:
            token = await get_token_by_login_password(session=session, login=login, password=password)
            user = await get_user_service_by_login(session=session, user_login=login)
        request.session.update({"token": token, "role_user": user.role_user.value})
        print(user.role_user.value)
        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Union[bool, RedirectResponse]:
        token = request.session.get("token")

        if not token:

            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="...")