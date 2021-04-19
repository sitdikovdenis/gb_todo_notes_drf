import time
import datetime
import json
from rest_framework.test import APIClient
import pytest

# модель User: есть возможность просмотра списка и каждого пользователя в отдельности, можно вносить изменения,
# нельзя удалять и создавать;,
# модель Project: доступны все варианты запросов;
# модель ToDo: доступны все варианты запросов; при удалении не удалять ToDo, а выставлять признак, что оно закрыто;

# администраторы могут всё;
# разработчики имеют все права на модель ToDo, могут просматривать модели Project и User;
# владельцы проектов имеют права на просмотр модели User и все права на модель Project и ToDo.

employee_pk = 'f9be3176-67f4-4980-9a8e-3ca6409a07ff'
project_pk = 'b5dbd280-8329-4b11-899e-8c1b72d56ba7'
todo_pk = 'a90aece3-b1d1-485c-965e-c82d4a9e3644'


def get_list_status(client, url):
    response = client.get(url, follow=True)
    return response.status_code


def get_status(client, url):
    response = client.get(url, follow=True)
    return response.status_code


def delete_employee_status(client):
    response = client.delete(f'/api/employees/f9be3176-67f4-4980-9a8e-3ca6409a07ff/', follow=True)
    return response.status_code


def patch_employee_status(client):
    response = client.patch(f'/api/employees/f9be3176-67f4-4980-9a8e-3ca6409a07ff/',
                            data='{"birthday_year":"1993"}',
                            content_type='application/json')
    return response.status_code


def post_status(client, url, data):
    response = client.post(url,
                           data=data,
                           content_type='application/json')
    return response.status_code


@pytest.mark.parametrize("client, uri, status_code", [('api_client', '/api/employees/', 200),
                                                      ('admin_api_client', '/api/employees/', 200),
                                                      ('developer_api_client', '/api/employees/', 200),
                                                      ('product_owner_api_client', '/api/employees/', 200),
                                                      ('api_client', '/api/projects/', 200),
                                                      ('admin_api_client', '/api/projects/', 200),
                                                      ('developer_api_client', '/api/projects/', 200),
                                                      ('product_owner_api_client', '/api/projects/', 200),
                                                      ('api_client', '/api/todos/', 200),
                                                      ('admin_api_client', '/api/todos/', 200),
                                                      ('developer_api_client', '/api/todos/', 200),
                                                      ('product_owner_api_client', '/api/todos/', 200),
                                                      ])
def test_list_api(clients, client, uri, status_code):
    assert get_list_status(clients[client], uri) == status_code


@pytest.mark.parametrize("client, uri, status_code", [('api_client', f'/api/employees/{employee_pk}/', 200),
                                                      ('admin_api_client', f'/api/employees/{employee_pk}/', 200),
                                                      ('developer_api_client', f'/api/employees/{employee_pk}/', 200),
                                                      ('product_owner_api_client', f'/api/employees/{employee_pk}/',
                                                       200),
                                                      ('api_client', f'/api/projects/{project_pk}/', 200),
                                                      ('admin_api_client', f'/api/projects/{project_pk}/', 200),
                                                      ('developer_api_client', f'/api/projects/{project_pk}/', 200),
                                                      ('product_owner_api_client', f'/api/projects/{project_pk}/', 200),
                                                      ('api_client', f'/api/todos/{todo_pk}/', 200),
                                                      ('admin_api_client', f'/api/todos/{todo_pk}/', 200),
                                                      ('developer_api_client', f'/api/todos/{todo_pk}/', 200),
                                                      ('product_owner_api_client', f'/api/todos/{todo_pk}/', 200),
                                                      ])
def test_get_api(clients, client, uri, status_code):
    assert get_status(clients[client], uri) == status_code


@pytest.mark.parametrize("client, uri, r_data, status_code", [('api_client', '/api/employees/', 'author_data', 401),
                                                              ('admin_api_client', '/api/employees/', 'author_data',
                                                               405),
                                                              ('developer_api_client', '/api/employees/', 'author_data',
                                                               403),
                                                              ('product_owner_api_client', '/api/employees/',
                                                               'author_data', 403),
                                                              ('api_client', '/api/projects/', 'projects_data', 401),
                                                              (
                                                                      'admin_api_client', '/api/projects/',
                                                                      'projects_data', 201),
                                                              (
                                                              'developer_api_client', '/api/projects/', 'projects_data',
                                                              403),
                                                              ('product_owner_api_client', '/api/projects/',
                                                               'projects_data', 201),
                                                              ('api_client', '/api/todos/', 'todos_data', 401),
                                                              ('admin_api_client', '/api/todos/', 'todos_data', 201),
                                                              (
                                                              'developer_api_client', '/api/todos/', 'todos_data', 201),
                                                              ('product_owner_api_client', '/api/todos/', 'todos_data',
                                                               201),
                                                              ])
def test_post_api(clients, data_fixture, client, uri, r_data, status_code):
    c = clients[client]
    d = data_fixture[r_data]
    assert post_status(c, uri, d) == status_code
