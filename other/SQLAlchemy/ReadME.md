SQLAlchemy — это библиотека Python для работы с реляционными базами данных. С ее помощью можно работать с PostgreSQL, MySQL, SQLite и другими СУБД.
Библиотека SQLAlchemy предоставляет инструменты Core и ORM для работы с базами данных.
SQLAlchemy Core — низкоуровневый API для работы напрямую с SQL. 
SQLAlchemy ORM (Object-Relational Mapping) — высокоуровневый инструмент, абстрагирующий от прямого написания SQL-запросов. Работает через объекты Python, представляющие строки таблиц.

Установка PostgreSQL:
    $ sudo apt update
    $ sudo apt install postgresql postgresql-client
Запуск сервера:
    $ sudo systemctl start postgresql
    $ sudo systemctl enable postgresql
Статус службы:
    $ systemctl status postgresql
Проверка установки PostgreSQL:
    $ dpkg -l | grep postgresql
Проверка версии PostgreSQL:
    $ psql --version
Проверка порта (по умолчанию 5432):
    $ ss -tulnp | grep 5432

Установка SQLAlchemy:
    $ pip install sqlalchemy
Установка драйвера и зависимостей для сборки:
    $ sudo apt install -y python3-dev libpq-dev postgresql-server-dev-all gcc
    $ pip install --upgrade pip setuptools wheel
    $ pip install psycopg2


Создание новой базы данных в PostgreSQL (Linux)Шаг 1. Переключитесь на пользователя postgres:
    $ sudo -u postgres psql
Создайте базу данных:
    # CREATE DATABASE example_db;
Создайте пользователя и назначьте права:
    # CREATE USER admin WITH PASSWORD 'admin';
    # GRANT ALL PRIVILEGES ON DATABASE example_db TO admin;
Выйдите из psql:
    # \q
Проверка списка баз данных;
    $ sudo -u postgres psql -l
Подключение к новой БД:
    $ psql -U admin -d example_db -h 127.0.0.1
