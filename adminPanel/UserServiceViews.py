from sqladmin import ModelView
from starlette.requests import Request
from wtforms.fields.simple import PasswordField

from auth.auth_helper import creation_token_for_user_service
from auth.utils import hash_password
from core.models import UserService, db_helper
from crud.userService import get_user_service_by_login, update_user_service


class UserServiceViews(ModelView, model=UserService):
    name = "Администратор"
    name_plural = "Администраторы"
    icon = "fa-solid fa-user-nurse"

    can_delete = False
    can_export = False

    save_as = False
    save_as_continue = False

    column_list = [UserService.id, UserService.login, UserService.tg_id, UserService.role_user, UserService.is_active]
    column_searchable_list = [UserService.login, UserService.tg_id, UserService.is_active]

    column_details_list = [UserService.id, UserService.login, UserService.tg_id, UserService.role_user,
                           UserService.is_active]

    form_columns = [UserService.login, UserService.password, UserService.tg_id, UserService.role_user,
                    UserService.is_active]

    form_overrides = dict(password=PasswordField)

    column_labels = {UserService.id: "ID",
                     UserService.login: "Логин",
                     UserService.password: "Пароль",
                     UserService.tg_id: "ID Telegram",
                     UserService.role_user: "Роль",
                     UserService.is_active: "Активен"}

    def is_accessible(self, request: Request) -> bool:
        if request.session.get("role_user") == "SUPER_ADMIN":
            return True
        return False

    def is_visible(self, request: Request) -> bool:
        if request.session.get("role_user") == "SUPER_ADMIN":
            return True
        return False

    async def on_model_change(self, data, model, is_created, request):
        data["password"] = hash_password(data["password"])
        request.session.update({"s_login": data["login"]})

    async def after_model_change(self, data, model, is_created, request):
        if is_created:
            async with db_helper.session_factory() as session:
                user = await get_user_service_by_login(session=session, user_login=request.session.get("s_login"))
                await update_user_service(session=session, user=user, user_update=None, token_update=True)
