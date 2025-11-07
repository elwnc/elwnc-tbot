from router import router
from aiogram.filters.command import Command
from aiogram.types import Message
from models.users import TelegramUser
from tortoise.timezone import now
from datetime import timedelta


STATISTICS_TEMPLATE = """
📊 <b>Bot foydalanuvchilari</b>
<i>Bot ishga tushgandan beri botga {auc} ta foydalanuvchi /start buyrug'i bosgan</i>

<b>Barcha foydalanuvchi:</b> {auc}
<b>So'ngi 168 soat ichida:</b> {twuc}
<b>So'ngi 1kun ichida:</b> {tduc}
"""


A_WEEK = timedelta(days=7)
A_DAY = timedelta(days=1)


@router.message(Command(commands=['statistics', 'stats']))
async def statistics_handler(m: Message):
    today = now()

    stats = {
        'auc': await TelegramUser.all().count(),
        'twuc': await TelegramUser.filter(created_at__gte=today - A_WEEK).count(),
        'tduc': await TelegramUser.filter(created_at__gte=today - A_DAY).count()
    }
    
    await m.answer(STATISTICS_TEMPLATE.format(**stats))
