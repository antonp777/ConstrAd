from sqladmin import ModelView

from core.models import User


class UserViews(ModelView, model=User):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fas fa-user"

    can_delete = False
    can_export = False

    save_as = False
    save_as_continue = False

    column_list = [User.id, User.name_user, User.tg_id, User.is_active]
    column_searchable_list = [User.name_user, User.tg_id, User.is_active]

    column_details_list = [User.id, User.name_user, User.tg_id, User.is_active, User.payments, User.orders, User.tasks]

    form_columns = [User.name_user, User.tg_id, User.is_active]

    column_labels = {User.id: "ID",
                     User.name_user: "Имя пользователя",
                     User.tg_id: "ID Telegram",
                     User.is_active: "Активен",
                     User.payments: "Пополнения",
                     User.tasks: "Задания",
                     User.orders: "Покупки"}
