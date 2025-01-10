from sqladmin import ModelView

from core.models import Payment


class PaymentAdminViews(ModelView, model=Payment):
    name = "Платеж"
    name_plural = "Платежи"
    icon = "fa-regular fa-credit-card"

    can_delete = False
    can_export = False

    save_as = False
    save_as_continue = False

    column_list = [Payment.id, Payment.date, Payment.sum, Payment.status_pay, Payment.user]
    column_searchable_list = [Payment.sum, Payment.date]

    column_details_list = [Payment.id, Payment.date, Payment.sum, Payment.status_pay, Payment.user]

    form_columns = [Payment.sum, Payment.user, Payment.status_pay]

    column_labels = {Payment.id: "ID",
                     Payment.date: "Дата",
                     Payment.sum: "Сумма",
                     Payment.status_pay: "Статус платежа",
                     Payment.user_id: "ID Пользователя",
                     Payment.user: "Пользователь"}
