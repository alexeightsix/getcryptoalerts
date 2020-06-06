import pytest
import requests

from gca.bootstrap.app import create_app
from mongoengine import connect

app = create_app(env="test")


@pytest.fixture(autouse=True)
def before_all():
    app.db.drop_database(app.config['DB_TEST_NAME'])
    requests.delete('http://localhost:8025/api/v1/messages')


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


@pytest.fixture
def config():
    return app.config
