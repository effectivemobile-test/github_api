# github_api
Автоматический тест для проверки работы с GitHub API на языке Python.

### Запуск проекта на локальной машине:

Клонировать репозиторий:
```
git clone https://github.com/effectivemobile-test/github_api.git
```
Дополнить файл .env строкой с API-токеном:
```
TOKEN_API=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
```
Cоздать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Запустить скрипт любым удобным способом:
```
python test_api.py
```