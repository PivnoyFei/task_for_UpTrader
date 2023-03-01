# task_for_UpTrader

[![Build Status](https://github.com/PivnoyFei/task_for_UpTrader/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/PivnoyFei/task_for_UpTrader/actions/workflows/main.yml)

<h1 align="center"><a target="_blank" href="">Тестовое задание для UpTrader</a></h1>

### Стек
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.11](https://img.shields.io/badge/3.11-blue?style=flat-square&logo=3.11)
![Django](https://img.shields.io/badge/Django-171515?style=flat-square&logo=Django)![4.1.7](https://img.shields.io/badge/4.1.7-blue?style=flat-square&logo=4.1.7)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-171515?style=flat-square&logo=PostgreSQL)![13.0](https://img.shields.io/badge/13.0-blue?style=flat-square&logo=13.0)
![SQLite](https://img.shields.io/badge/SQLite-171515?style=flat-square&logo=SQLite)

### Задание
#### Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

#### Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
#### {% draw_menu 'main_menu' %}
#### При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
gh clone https://github.com/PivnoyFei/task_for_UpTrader.git
cd task_for_UpTrader
```

#### Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```

### Запуск на локальной машине:
#### Открываем в консоли папку backend:
```bash
cd backend
```

#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate --noinput
```

#### Создайте суперпользователя Django:
```bash
python manage.py createsuperuser
```

#### Запускаем сервер:
```bash
python manage.py runserver --insecure
```

### Для запуска в Docker:
#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```

### Перед запуском сервера, необходимо создать .env файл расположенный по пути infra/.env со своими данными.
### Ниже представлены параметры по умолчанию.
```bash
SECRET_KEY='key' # Секретный ключ джанго
DEBUG='True' # Режим разработчика
ALLOWED_HOSTS='*, localhost' # Адрес

DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres' # имя БД
POSTGRES_USER='user' # логин для подключения к БД
POSTGRES_PASSWORD='password' # пароль для подключения к БД
DB_HOST='db' # название контейнера
DB_PORT='5432' # порт для подключения к БД
```

#### Чтобы сгенерировать безопасный случайный секретный ключ, используйте команду:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### Запуск docker-compose:
```bash
docker-compose up -d --build
```

#### Примените миграции:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

#### Команда для заполнения базы начальными данными (необязательно):
```bash
docker-compose exec backend python manage.py loaddata db.json
```

#### Создайте суперпользователя Django для входа в админку:
```bash
docker-compose exec backend python manage.py createsuperuser
```

#### После успешной сборки, на сервере выполните команды (только после первого деплоя):
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

#### Теперь по адресу http://localhost:8000/admin/ доступна админка.

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)
