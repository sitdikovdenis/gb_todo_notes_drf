import json
from uuid import uuid4

import pytest

from library.models import Author

employee_id = uuid4()


# @pytest.fixture()
# def api_client():
#     from rest_framework.test import APIClient
#     return APIClient()


# @pytest.fixture
# def create_author_f(db):
#     def create_author():
#         return Author.objects.create(
#             first_name='test_first_name', last_name='test-last_name', birthday_year='1993', phone='+79879999999',
#             user_name='test_user_name', uuid=employee_id
#         )
#
#     return create_author


# @pytest.fixture
# def test_password():
#     return 'strong-test-pass'


# @pytest.fixture
# def create_user(db, django_user_model, test_password):
#     def make_user(**kwargs):
#         kwargs['password'] = test_password
#         if 'username' not in kwargs:
#             kwargs['username'] = str(uuid4())
#         return django_user_model.objects.create_user(**kwargs)
#
#     return make_user


# модель User: есть возможность просмотра списка и каждого пользователя в отдельности,
# можно вносить изменения, нельзя удалять и создавать;


@pytest.mark.django_db
def test_employees_list(api_client):
    response = api_client.get('/api/employees/', follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_employees_detail(api_client, create_author_f):
    author = create_author_f()
    response = api_client.get(f'/api/employees/{author.uuid}/', follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_employees_patch_unauthorized(api_client, create_author_f):
    author = create_author_f()
    response = api_client.patch(f'/api/employees/{author.uuid}/', data=json.dumps("name=123"),
                                content_type='application/json')
    assert response.status_code == 401


@pytest.mark.django_db
def test_employees_patch_authorized(api_client, create_author_f, create_user, test_password):
    user = create_user(
        is_staff=True, is_superuser=True
    )
    api_client.login(
        username=user.username, password=test_password
    )

    author = create_author_f()
    response = api_client.patch(f'/api/employees/{author.uuid}/', data='{"birthday_year":"1993"}',
                                content_type='application/json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_employees_delete(api_client, create_author_f, create_user, test_password):
    user = create_user(
        is_staff=True, is_superuser=True
    )
    api_client.login(
        username=user.username, password=test_password
    )

    author = create_author_f()
    response = api_client.delete(f'/api/employees/{author.uuid}/', follow=True)
    assert response.status_code == 405


@pytest.mark.django_db
def test_employees_create(api_client, create_author_f, create_user, test_password):
    user = create_user(
        is_staff=True, is_superuser=True
    )
    api_client.login(
        username=user.username, password=test_password
    )

    data = {
        "user_name": "test",
        "first_name": "test",
        "last_name": "test",
        "email": "test",
        "birthday_year": "null"
    }

    response = api_client.patch(f'/api/employees/', data=data,
                                content_type='application/json')
    assert response.status_code == 405
