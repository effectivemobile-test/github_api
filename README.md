# github_api
Автоматический тест для проверки работы с GitHub API на языке Python.

### Запуск проекта на локальной машине:

Клонировать репозиторий:
```
git clone https://github.com/effectivemobile-test/github_api.git
```

Cоздать виртуальное окружение:
```
python3.11 -m venv venv
```
или
```
py -3.11 -m venv venv
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