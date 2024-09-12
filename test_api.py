import os
import requests
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN_API = os.getenv('TOKEN_API')
REPO_NAME = os.getenv('REPO_NAME')
base_url = 'https://api.github.com'
repo_description = 'Тестовый репозиторий по заданию Effective Mobile.'


def create_repo(descr=None):
    url = f'{base_url}/user/repos'
    headers = {'Authorization': f'token {TOKEN_API}'}
    data = {'name': REPO_NAME, 'description': descr}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print('OK. Новый публичный репозиторий создан успешно.')
    else:
        print(f'ERROR. Ошибка при создании нового репозитория. Статус код: {response.status_code}.')


def check_repo():
    repos = requests.get(f'{base_url}/users/{USERNAME}/repos').json()
    repos_names = [i['name'] for i in repos]
    if REPO_NAME in repos_names:
        print('OK. Созданный репозиторий присутствует в списке репозиториев.')
    else:
        print('ERROR. Что-то пошло не так. Созданный репозиторий отсутствует в списке репозиториев.')


def delete_repo():
    url = f'{base_url}/repos/{USERNAME}/{REPO_NAME}'
    headers = {'Authorization': f'token {TOKEN_API}'}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print('OK. Созданный репозиторий успешно удален.')
    elif response.status_code == 404:
        print(f'ERROR. Репозиторий не найден или уже уделен. Статус код: {response.status_code}.')
    else:
        print(f'ERROR. Невозможно удалить репозиторий. Статус код: {response.status_code}.')


def tests():
    create_repo()
    check_repo()
    delete_repo()


if __name__ == '__main__':
    tests()
