from functools import wraps
from flask import request, abort, jsonify
from gca.rules import isEmail, isFullName, isSecurePassword
from gca.collection.user import User
from gca.helpers import verify_password
from werkzeug.wrappers import Request, Response, ResponseStream
import re
import jwt


class JWT_Auth(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        for rule in [r"^\/notifications/$"]:
            if re.search(rule, environ['REQUEST_URI']):
                try:
                    token = str(Request(environ).headers.get(
                        'Authorization')).split(" ")[1]
                    email = jwt.decode(token, "secret", algorithms=[
                                       'HS256'])["email"]
                    user = User.objects.get(email=email, activated=True)
                except:
                    abort(401)
        return self.app(environ, start_response)


def name_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            name = isFullName(request.get_json()['name'])
            if not name:
                raise Exception
        except:
            return jsonify({"errors": ["invalid_name"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def email_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            email = isEmail(request.get_json()['email'])
            if not email:
                raise Exception
        except:
            return jsonify({"errors": ["invalid_email"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def unique_email_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            User.objects.get(email=request.get_json()['email'])
            return jsonify({"errors": ["email_exists"]}), 400
        except User.DoesNotExist:
            return f(*args, **kwargs)
    return decorated_function


def password_confirm(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            password = request.get_json()['password']
            password_confirm = request.get_json()['password_confirm']

            if password != password_confirm:
                raise Exception
        except:
            return jsonify({"errors": ["password_confirm"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def password_strength(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if isSecurePassword(request.get_json()['password']) is False:
            return jsonify({"errors": ["password_strength"]}), 400

        return f(*args, **kwargs)
    return decorated_function


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return True
        except:
            return jsonify({"errors": ["token"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def operator_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return True
        except:
            return jsonify({"errors": ["operator"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def coin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return True
        except:
            return jsonify({"errors": ["coin"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def notification_type(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return True
        except:
            return jsonify({"errors": ["notification_type"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def notification_interval(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return True
        except:
            return jsonify({"errors": ["notification_interval"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def code_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            User.objects.get(code=request.get_json()['code'])
            return f(*args, **kwargs)
        except User.DoesNotExist:
            abort(404)
    return decorated_function


def user_exists(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        try:
            user = User.objects.get(email=request.get_json()['email'])
            valid = verify_password(
                stored_password=user.password, provided_password=request.get_json()['password'])
            if not valid:
                raise Exception
        except:
            return jsonify({"errors": ["invalid_login"]}), 400
        return f(*args, **kwargs)
    return decorated_function


def email_exists(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            User.objects.get(email=request.get_json()['email'])
        except:
            return jsonify({"errors": ["email_exists"]}), 400
        return f(*args, **kwargs)
    return decorated_function