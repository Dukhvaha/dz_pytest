import pytest

@pytest.fixture
def user_data():
    return {
        'username': 'arsamak',
        'email': 'yusupovarsamak',
        'is_active': True
    }

@pytest.fixture(params=[[1,2,3], [4,5,6], [7,8,9]])
def numbers(request):
    return request.param


@pytest.fixture(scope='module')
def open_file():
    '''Фикстура для работы с файлом'''
    file = open('test_file.txt', 'w+')
    yield file
    print('Работает финализатор')
    file.close()


@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com'