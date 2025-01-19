from datetime import datetime


def date_time():
    now = datetime.now()
    now_str = now.strftime("%d.%m.%Y %H:%M")
    return datetime.strptime(now_str, "%d.%m.%Y %H:%M")


def date_time_str():
    now = datetime.now()
    return now.strftime("%d.%m.%Y %H:%M")
