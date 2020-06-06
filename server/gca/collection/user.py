from mongoengine import *
from mongoengine import signals
from uuid import uuid4
import datetime

class User(Document):
    _id = UUIDField(binary=False, default=uuid4(), required=True)
    name = StringField(max_length=200, required=True)
    email = EmailField(max_length=200, required=True, uique=True)
    password = StringField(max_length=200, required=True)
    activated = BooleanField(max_length=200, required=False, default=False)
    code = StringField(max_length=64, required=False)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)