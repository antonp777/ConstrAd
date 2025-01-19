import aiohttp

from core import settings
from utils.date import date_time_str


async def send_task_to_chanel(city: str, district: str, work: str, price_work: int, person: int, fee: int):
    url = f"https://api.telegram.org/bot{settings.tg.token_bot}/sendMessage"

    text = (f"<code>актуально на {date_time_str()}</code>\n\n"
            f"<b>Город</b>: {city}\n"
            f"<b>Район</b>: {district}\n"
            f"<b>Работа</b>: {work}\n"
            f"<b>Цена работы</b>: {price_work} руб.\n"
            f"<b>Количество человек</b>: {person}\n"
            f"<b>Комиссия</b>: {fee} руб.\n\n")

    reply_markup = {
        "inline_keyboard": [
            [
                {
                    "text": "Забрать",
                    "url": "https://t.me/STROYKASEVBOT?start"
                },
                {
                    "text": "Разместить",
                    "url": "https://t.me/Kentstroika"
                }
            ]
        ]
    }
    data = {"chat_id": settings.tg.chanel,
            "text": text,
            "reply_markup": reply_markup,
            "parse_mode": "HTML"
            }
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=data)
