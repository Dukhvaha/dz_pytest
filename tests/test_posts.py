import requests
import pytest

@pytest.mark.parametrize('endpoint',[
    '/posts',
    '/users',
    '/comments'
])

def test_get_url(base_url,endpoint):
    response = requests.get(f'{base_url}{endpoint}')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_data(base_url):
    response = requests.post(f'{base_url}/posts', data={
        'username': 'arsamak'
    })
    assert response.status_code == 201

def test_create_put(base_url):
    response = requests.put(f'{base_url}/posts/1', data={
        'userId': 'Ansar'
    })
    assert response.status_code == 200


def test_delete_post(base_url):
    response = requests.delete(f'{base_url}/posts/1')
    assert response.status_code == 200