##### _разработка Sayfullin R.R.

Инструкция актуальна для Linux-систем.
========================================================================================================================
Используемые технологии:
    python = "^3.11.11"
    fastapi = "^0.115.12"
    PostgreSQL

Скопируйте репозиторий с помощью команды:
$ git clone https://github.com/RuslanSayfullin/FastAPI.git
Перейдите в основную директорию с помощью команды: 
$ cd FastAPI

========================================================================================================================
Создать и активировать виртуальное окружение: 
    $ python3 -m venv venv 
    $ source venv/bin/activate 
Установить зависимости из файла requirements.txt:
    (venv) $ pip install -r requirements.txt

Cоздания файла зависимостейс помощью команды:
    $ pip freeze > requirements.txt

Open the inreactive documentation: http://localhost:8000/docs

# Источник
========================================================================================================================
https://github.com/PacktPublishing/Building-Data-Science-Applications-with-FastAPI-Second-Edition
https://github.com/PacktPublishing/Building-Data-Science-Applications-with-FastAPI-Second-Edition/blob/

Building Data Science Applications with FastAPI.
================================================
Part 1: Introduction to Python and FastAPI
    1. Python Development Environment Setup
    2. Python Programming Specificities
Part 2: Building and Deploying a Complete Web Backend with FastAPI
Part 3: Building Resilient and Distributed Data Science Systems with FastAPI