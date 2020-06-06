import pdb
import json
import requests
import re
from gca.collection.user import User
from gca.helpers import verify_password
import pytest

def test_create_user(client, config):
    new_user = dict(
        name="John Doe",
        email="jon.doe@example.com",
        password="]>yR$NU5nb/4g&u<@",
        password_confirm="]>yR$NU5nb/4g&u<@"
    )

    request = json.dumps(new_user)

    response = client.post('/user/create/', data=request,
                           content_type='application/json')

    assert response.status_code == 200

    user = User.objects.get(email=new_user['email'])

    response = requests.get(config['MAILHOG_API_ENDPOINT'] +
                            '/v2/search?kind=to&query='+user['email']+'&limit=1')

    assert response.status_code == 200

    email = response.json()

    assert email['total'] == 1
    assert email['items'][0]['Content']['Headers']['Subject'][0] == "Welcome to Get Crypto Alerts!"
    assert email['items'][0]['Content']['Headers']['from'][0] == "support@getcryptoalerts.com"
    assert user.code in email['items'][0]['Content']['Body']
    assert len(user.code) == 64

    response = client.post('/user/activate/', data=json.dumps(dict(code=user.code)),
                           content_type='application/json')

    assert response.status_code == 200


def test_cant_create_user_with_invalid_name(client, config):
    new_user = json.dumps(dict(
        name="",
        email="jon.doe@example.com",
        password="]>yR$NU5nb/4g&u<@",
        password_confirm="]>yR$NU5nb/4g&u<@"
    ))

    response = client.post('/user/create/', data=new_user,
                           content_type='application/json')

    assert response.status_code == 400
    assert "invalid_name" in response.get_json()["errors"]


def test_cant_create_user_with_invalid_email(client, config):
    new_user = json.dumps(dict(
        name="John Doe",
        email="jon.doeexample.com",
        password="]>yR$NU5nb/4g&u<@",
        password_confirm="]>yR$NU5nb/4g&u<@"
    ))

    response = client.post('/user/create/', data=new_user,
                           content_type='application/json')

    assert response.status_code == 400
    assert "invalid_email" in response.get_json()["errors"]


def test_cant_create_user_with_unique_password_fields(client, config):
    new_user = json.dumps(dict(
        name="John Doe",
        email="jon.doe@gmail.com",
        password="abc",
        password_confirm="efg"
    ))

    response = client.post('/user/create/', data=new_user,
                           content_type='application/json')

    assert response.status_code == 400
    assert "password_confirm" in response.get_json()["errors"]


def test_cant_create_user_with_insecure_password(client, config):
    new_user = json.dumps(dict(
        name="John Doe",
        email="jon.doe@gmail.com",
        password="",
        password_confirm=""
    ))

    response = client.post('/user/create/', data=new_user,
                           content_type='application/json')

    assert response.status_code == 400
    assert "password_strength" in response.get_json()["errors"]


def test_cant_create_user_that_already_exists(client):
    new_user = dict(
        name="John Doe",
        email="jon.doe@example.com",
        password="]>yR$!!U5nb/4g&u<@",
        password_confirm="]>yR$!!U5nb/4g&u<@"
    )

    request = json.dumps(new_user)

    response = client.post('/user/create/', data=request,
                           content_type='application/json')

    assert response.status_code == 200

    new_user['name'] = "New Name"
    new_user['password'] = "]>yRaasdas@!!"
    new_user['password_confirm'] = "]>yRaasdas@!!"

    response = client.post('/user/create/', data=request,
                           content_type='application/json')

    assert response.status_code == 400
    assert "email_exists" in response.get_json()["errors"]


def test_invalid_activation_code(client):
    response = client.get(f'/user/activate/345345/')
    assert response.status_code == 404


def test_login(client):
    new_user = dict(
        name="John Doe",
        email="jon.doe@example.com",
        password="]>yR$!!U5nb/4g&u<@",
        password_confirm="]>yR$!!U5nb/4g&u<@"
    )

    request = json.dumps(new_user)

    response = client.post('/user/create/', data=request,
                           content_type='application/json')

    del new_user["name"]
    del new_user["password_confirm"]

    request = json.dumps(new_user)

    response = client.post('/user/login/', data=request,
                           content_type='application/json')

    regex = r"^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$"
    token = response.data.decode("utf-8")

    assert response.status_code == 200
    assert re.match(regex, token)


def test_cant_login_with_incorrect_email(client):
    new_user = dict(
        email="jon.doeexample.com",
        password="]>yR$!!U5nb/4g&u<@",
    )

    request = json.dumps(new_user)

    response = client.post('/user/login/', data=request,
                           content_type='application/json')

    assert response.status_code == 400
    assert "invalid_email" in response.get_json()["errors"]


def test_cant_login_without_a_password(client):
    new_user = dict(
        email="jon.doeexa@mple.com",
        password="",
    )

    request = json.dumps(new_user)

    response = client.post('/user/login/', data=request,
                           content_type='application/json')

    assert response.status_code == 400
    assert "password_strength" in response.get_json()["errors"]


def test_cant_login_without_valid_login(client):
    new_user = dict(
        email="jon@asdasd.com",
        password="]>yR$!!U5nb/4g&u<@",
    )
    request = json.dumps(new_user)

    response = client.post('/user/login/', data=request,
                           content_type='application/json')

    assert response.status_code == 400
    assert "invalid_login" in response.get_json()["errors"]


def test_user_forgot_password(client, config):
    new_user = dict(
        name="John Doe",
        email="jon.doe@example.com",
        password="]>yR$NU5nb/4g&u<@",
        password_confirm="]>yR$NU5nb/4g&u<@"
    )

    client.post('/user/create/', data=json.dumps(new_user),
                content_type='application/json')

    requests.delete(f"{config['MAILHOG_API_ENDPOINT']}/v1/messages")

    del new_user['name']
    del new_user['password']
    del new_user['password_confirm']

    response = client.post('/user/forgot/', data=json.dumps(new_user),
                           content_type='application/json')

    assert response.status_code == 200

    user = User.objects.get(email=new_user['email'])

    response = requests.get(config['MAILHOG_API_ENDPOINT'] +
                            '/v2/search?kind=to&query='+user['email']+'&limit=1')

    assert response.status_code == 200

    email = response.json()

    assert email['total'] == 1
    assert email['items'][0]['Content']['Headers']['Subject'][0] == "Get Crytp Alerts: Forgotten Password"
    assert email['items'][0]['Content']['Headers']['from'][0] == "support@getcryptoalerts.com"
    assert user.code in email['items'][0]['Content']['Body']
    assert len(user.code) == 64

    response = client.post('/user/change-password/', data=json.dumps(dict(
        code=user.code,
        password="]>yR$NU5nb/!!g&u<!",
        password_confirm="]>yR$NU5nb/!!g&u<!"
    )), content_type='application/json')

    user = User.objects.get(email=new_user['email'])

    assert verify_password(user.password, ']>yR$NU5nb/!!g&u<!')
    assert response.status_code == 200


def test_cant_change_password_without_valid_code(client):
    assert client.post('/user/change-password/', data=json.dumps(dict(code="asdasdsd")),
                       content_type='application/json').status_code == 404


def test_cant_change_password_without_valid_password(client):
    new_user = dict(
        name="John Doe",
        email="jon.doe@example.com",
        password="]>yR$NU5nb/4g&u<@",
        password_confirm="]>yR$NU5nb/4g&u<@"
    )

    client.post('/user/create/', data=json.dumps(new_user),
                content_type='application/json')

@pytest.mark.skip(reason="Incomplete feature")
def test_user_update_email(client):
    new_user = dict(
        name="John Doe",
        email="jon.doe@example.com",
        password="]>yR$NU5nb/4g&u<@",
        password_confirm="]>yR$NU5nb/4g&u<@"
    )

    client.post('/user/create/', data=json.dumps(new_user),
                content_type='application/json')

    user = User.objects.get(email=new_user['email'])

    client.post('/user/activate/', data=json.dumps(dict(code=user.code)),
                content_type='application/json')

    response = client.post('/user/email/', data=json.dumps(dict(
        name="Doe John",
        email="jon.NOneUNique@example.com",
        password="]>yR$NU5nb/4g&u<@"

    )),
        content_type='application/json')

    assert response.status_code == 200
