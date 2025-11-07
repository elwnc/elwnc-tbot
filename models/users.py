from tortoise import fields
from .base import BaseModel


class TelegramUser(BaseModel):
    telegram_id = fields.BigIntField(default=None, null=True, unique=True)

    class Meta:
        table = "elwnc_bot_telegram_users"
        unique_together = (('id', 'guid', 'telegram_id'),)
