from sqladmin import ModelView
from wtforms.fields.simple import TextAreaField

from core.models import Task
from tg.helper_tg import send_task_to_chanel


class TaskViews(ModelView, model=Task):
    name = "Задание"
    name_plural = "Задания"
    icon = "fa-regular fa-note-sticky"

    can_delete = False
    can_export = False

    save_as = False
    save_as_continue = False

    column_list = [Task.id, Task.city, Task.district, Task.work, Task.price_work, Task.person, Task.fee, Task.is_active]
    column_formatters = {Task.work: lambda m, a: m.work[:20]}
    column_searchable_list = [Task.city, Task.work, Task.is_active]

    column_details_list = [Task.id, Task.city, Task.district, Task.work, Task.price_work, Task.person, Task.fee,
                           Task.phone, Task.is_active, Task.orders, Task.users]

    form_excluded_columns = [Task.users, Task.orders]

    form_overrides = dict(work=TextAreaField)

    column_sortable_list = [Task.id]
    column_default_sort = [(Task.id, True)]

    column_labels = {Task.id: "ID",
                     Task.city: "Город",
                     Task.district: "Район",
                     Task.work: "Описание работы",
                     Task.price_work: "Цена работы",
                     Task.person: "Количество рабочих",
                     Task.fee: "Комиссия",
                     Task.phone: "Телефон",
                     Task.is_active: "Активность",
                     Task.users: "Пользователи",
                     Task.orders: "Покупки"
                     }

    async def on_model_change(self, data, model, is_created, request):
        # Отправка задания в канал
        if data["is_active"] and data["person"] > 0:
            await send_task_to_chanel(city=data["city"],
                                      district=data["district"],
                                      work=data["work"],
                                      price_work=data["price_work"],
                                      person=data["person"],
                                      fee=data["fee"]
                                      )
