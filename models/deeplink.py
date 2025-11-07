from tortoise import fields
from .base import BaseModel


class DeeplinkModel(BaseModel):
    name = fields.CharField(max_length=16)
    b64 = fields.CharField(max_length=32)
    execute = fields.CharField(max_length=128)
    arguments = fields.JSONField()

    class Meta:
        table = "elwnc_bot_deeplink"
