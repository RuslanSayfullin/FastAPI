import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="admin", password='admin')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаём курсор для выполнения операций с базой данных
cursor = connection.cursor()
# Создаём базу данных
cursor.execute('create database example_db_2')
# Закрываем соединение
cursor.close()
connection.close()