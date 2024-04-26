import requests
from http import HTTPStatus

BASE_URL = 'http://localhost:8080'
DATA = {}


def test_get_list():
    response = requests.get(f'{BASE_URL}/items')
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json(), list)


def test_create_item():
    response = requests.post(f'{BASE_URL}/items', json={'foo': 'bar'})
    assert response.status_code == HTTPStatus.CREATED
    DATA['$oid'] = response.json().get('$oid')


def test_retrieve_item():
    response = requests.get(f'{BASE_URL}/items/{DATA.get("$oid")}')
    assert response.status_code == HTTPStatus.OK
    assert response.json().get('foo') == 'bar'


def test_update_item():
    response = requests.put(
        f'{BASE_URL}/items/{DATA.get("$oid")}', json={'foo': 'baz'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json().get('item').get('foo') == 'baz'


def test_retrieve_nonexistent_item():
    response = requests.get(f'{BASE_URL}/items/does-not-exist')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json().get('error') == 'Item not found'


def test_update_nonexistent_item():
    response = requests.put(
        f'{BASE_URL}/items/does-not-exist', json={'foo': 'baz'}
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json().get('error') == 'Item not found'
