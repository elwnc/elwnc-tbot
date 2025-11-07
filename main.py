from config import settings
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.chat_action import ChatActionMiddleware
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from tortoise.contrib.aiohttp import register_tortoise
from handlers import *
from router import router
from utils import set_bot_commands
import logging
import sys


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        f"{settings.webhook_base_url}{settings.webhook_path}",
        secret_token=settings.webhook_secret
    )
    await set_bot_commands(bot)


def main():
    dp = Dispatcher()
    
    dp.message.middleware.register(ChatActionMiddleware())

    dp.include_router(router)

    dp.startup.register(on_startup)

    bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    app = web.Application()
    
    webhook_request_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=settings.webhook_secret
    )
    webhook_request_handler.register(app, path=settings.webhook_path)
    
    setup_application(app, dp, bot=bot)
    
    register_tortoise(
        app, db_url=settings.database_url, modules={"models": ["models"]}, generate_schemas=True
    )

    web.run_app(app, host=settings.web_server_host, port=settings.web_server_port)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    main()
