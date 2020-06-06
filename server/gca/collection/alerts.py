from mongoengine import *
from mongoengine import signals
from uuid import uuid4
import datetime

class Alert(Document):
    _id = UUIDField(binary=False, default=uuid4(), required=True)
    user_id = IntField()
    name = StringField(max_length=200, required=True)
    rule = Object(max_length=200, required=True, uique=True)
    enabled = BooleanField(max_length=200, required=False, default=False)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)