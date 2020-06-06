from flask import Blueprint, request, jsonify
from functools import wraps
from gca.middleware import *
from gca.collection.user import User
from datetime import datetime, timedelta, timezone
from gca.helpers import random_id, json_response, hash_password
from gca.service.UserService import send_activation_email, send_forgot_password_email
import jwt

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/api/user/create/', methods=['POST'])
@name_required
@email_required
@password_confirm
@password_strength
@unique_email_required
def create():
    req = request.get_json()
    user = User()
    user.name = req["name"]
    user.email = req["email"]
    user.password = hash_password(req["password"])
    user.code = random_id(64)
    user.save()
    send_activation_email(user)
    return json_response(200)


@user.route('/api/user/login/', methods=['POST'])
@email_required
@password_strength
@user_exists
def login():
    JWT_PAYLOAD = {
        'email': request.get_json()['email'],
        'exp': datetime.utcnow() + timedelta(99999)
    }

    return jwt.encode(JWT_PAYLOAD, 'secret', 'HS256')


@user.route('/user/forgot/', methods=['POST'])
@email_required
@email_exists
def forgot():
    user = User.objects.get(email=request.get_json()['email'])
    user.code = random_id(64)
    user.save()
    send_forgot_password_email(user)
    return json_response(200)


@user.route('/user/email/', methods=['POST'])
@email_required
# @unique_email_required
@password_strength
def update_email():
    req = request.get_json()
    user = User.objects.get(email=request.get_json()['email'])
    user.email = req['email']
    user.password = req['password']
    # user.save()
    return json_response(200)


@user.route('/user/change-password/', methods=['POST'])
@code_required
@password_strength
@password_confirm
def update_password():
    req = request.get_json()
    user = User.objects.get(code=req['code'])
    user.password = hash_password(req["password"])
    user.code = None
    user.save()
    return json_response(200)


@user.route('/api/user/activate/', methods=['POST'])
@code_required
def activate():
    user = User.objects.get(code=request.get_json()['code'])
    user.code = None
    user.activated = True
    user.save()
    return json_response(200)
