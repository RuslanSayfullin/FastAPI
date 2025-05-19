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

Building Data Science Applications with FastAPI.
================================================
Part 1: Introduction to Python and FastAPI
    1. Python Development Environment Setup
    2. Python Programming Specificities
    3. Developing a RESTful API with FastAPI
    4. Managing Pydantic Data Models in FastAPI
    5. Dependency Injection in FastAPI
Part 2: Building and Deploying a Complete Web Backend with FastAPI
    6. Databases and Asynchronous ORMs
    7. Managing Authentication and Security in FastAPI
    8. Defining WebSockets for Two-Way Interactive Communication in FastAPI
    9. Testing an API Asynchronously with pytest and HTTPX
    10. Deploying a FastAPI Project
Part 3: Building Resilient and Distributed Data Science Systems with FastAPI
    11. Introduction to Data Science in Python
    12. Creating an Efficient Prediction API Endpoint with FastAPI
    13. Implementing a Real-Time Object Detection System Using WebSockets with FastAPI
    14. Creating a Distributed Text-to-Image AI System Using the Stable Diffusion Model
    15. Monitoring the Health and Performance of a Data Science System