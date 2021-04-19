import datetime
import pytest
import uuid

from rest_framework.test import APIClient
from django.core import management

from todo_app.models import Project, TODO
from library.models import Author


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(autouse=True)
def initial_data(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        management.call_command('loaddata', 'fixtures/initial_data.json')


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def admin_api_client():
    client = APIClient()
    client.login(username='admin', password='1Qwertyu')
    return client


@pytest.fixture
def developer_api_client():
    client = APIClient()
    client.login(username='developer', password='1Qwertyu2Qwertyu')
    return client


@pytest.fixture
def product_owner_api_client():
    client = APIClient()
    client.login(username='ProductOwner', password='1Qwertyu3Qwertyu')
    return client


@pytest.fixture
def clients(
        api_client,
        admin_api_client,
        developer_api_client,
        product_owner_api_client
):
    return {
        'api_client': api_client,
        'admin_api_client': admin_api_client,
        'developer_api_client': developer_api_client,
        'product_owner_api_client': product_owner_api_client
    }


@pytest.fixture
def author_data():
    return (
        '''{
            "first_name": "Денdddис",
            "last_name": "Ситдиков",
            "birthday_year": 2011,
            "email": "lifelesssss@gmail.com",
            "phone": "89872785354",
            "user_name": "ass33asa",
            "uuid": "f9be3176-67f4-4980-9a8e-3ca6409a07f4"
        }'''
    )


@pytest.fixture
def projects_data():
    return (
        '''{
            "name": "dfdsfgdfg",
            "repository_url": "https://vk.com/playpirates",
            "users": [
                "f9be3176-67f4-4980-9a8e-3ca6409a07ff"
            ]
        }'''
    )


@pytest.fixture
def todos_data():
    return (
        '''{
            "project": "b5dbd280-8329-4b11-899e-8c1b72d56ba7",
            "text": "testrfusadhfd",
            "created_at": "2021-03-12",
            "updated_at": "2021-03-12T20:08:50Z",
            "author": "f9be3176-67f4-4980-9a8e-3ca6409a07ff",
            "state": "C"
        }'''
    )


@pytest.fixture
def data_fixture(
        author_data,
        projects_data,
        todos_data
):
    return {
        'author_data': author_data,
        'projects_data': projects_data,
        'todos_data': todos_data
    }