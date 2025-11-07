from tortoise import models, fields
import uuid

class BaseModel(models.Model):
    id = fields.BigIntField(primary_key=True)
    guid = fields.UUIDField(default=uuid.uuid4)
    
    created_at = fields.DatetimeField(auto_now_add=True)
    uptated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True
        unique_together = (('id', 'guid'),)
        ordering = ["-created_at"]
