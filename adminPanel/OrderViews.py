from sqladmin import ModelView

from core.models import Order


class OrderViews(ModelView, model=Order):
    name = "Покупка"
    name_plural = "Покупки"
    icon = "fa-solid fa-cart-shopping"

    can_delete = False
    can_export = False

    save_as = False
    save_as_continue = False

    column_list = [Order.id, Order.date, Order.task_fee, Order.task_person, Order.user, Order.task]
    column_searchable_list = [Order.user, Order.task, Order.date]

    column_details_list = [Order.id, Order.date, Order.task_fee, Order.task_person, Order.user, Order.task]

    form_columns = [Order.date, Order.task_fee, Order.task_person, Order.user, Order.task]

    column_sortable_list = [Order.id, Order.date]
    column_default_sort = [(Order.date, True)]

    column_formatters = {Order.date: lambda m, a: m.date.strftime('%d.%m.%Y %H:%M')}



    column_labels = {Order.id: "ID",
                     Order.date: "Дата",
                     Order.task_fee: "Комиссия",
                     Order.task_person: "Количество рабочих",
                     Order.user: "Пользователь",
                     Order.task: "Задание"}
