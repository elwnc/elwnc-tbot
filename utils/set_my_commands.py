from aiogram import Bot
from aiogram.types.bot_command import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="⚡️ Bo'tga start bosish"),
        BotCommand(command="statistics", description="📊 Foydanuvchi sonlari bo'yicha statistika"),
        BotCommand(command="stats", description="⛓️ alias:statistics"),
    ]
    
    await bot.set_my_commands(commands)
