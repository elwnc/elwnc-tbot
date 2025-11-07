from router import router
from aiogram.filters.command import CommandStart, CommandObject
from aiogram.types import Message
from models.users import TelegramUser


@router.message(CommandStart(deep_link=True))
async def welcome_deeplink_handler(m: Message, command: CommandObject):
    args = command.args

    await welcome_handler(m)


@router.message(CommandStart(deep_link=False))
async def welcome_handler(m: Message):
    _, created = await TelegramUser.get_or_create(telegram_id=m.from_user.id)
    if created:
        await m.answer("Assalomu alaykum, @elwnc ning telegram botiga xush kelibsiz.")
    else:
        await m.answer("Assalomu alaykum!")
        await m.answer("Yaxshimisiz?")
