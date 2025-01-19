from sqladmin import ModelView

from core.models import Payment


class PaymentViews(ModelView, model=Payment):

    name = "Платеж"
    name_plural = "Платежи"
    icon = "fa-regular fa-credit-card"

    can_delete = False
    can_export = False

    save_as = False
    save_as_continue = False

    column_list = [Payment.id, Payment.date, Payment.sum, Payment.comment, Payment.status_pay, Payment.user]
    column_searchable_list = [Payment.comment, Payment.sum, Payment.date]

    column_details_list = [Payment.id, Payment.date, Payment.sum, Payment.status_pay, Payment.user]

    form_columns = [Payment.sum, Payment.user, Payment.status_pay]

    column_sortable_list = [Payment.id, Payment.date]
    column_default_sort = [(Payment.date, True)]

    column_formatters = {Payment.date: lambda m, a: m.date.strftime('%d.%m.%Y %H:%M')}

    column_labels = {Payment.id: "ID",
                     Payment.date: "Дата",
                     Payment.sum: "Сумма",
                     Payment.comment: "Комментарий",
                     Payment.status_pay: "Статус платежа",
                     Payment.user_id: "ID Пользователя",
                     Payment.user: "Пользователь"}


