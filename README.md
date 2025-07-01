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



#####
Класс Header в FastAPI используется для извлечения данных из HTTP-заголовков запроса и передачи их в параметры эндпоинта.

Основное назначение Header:
    1. Доступ к заголовкам запроса
    - Позволяет получать значения HTTP-заголовков, таких как:
        * User-Agent
        * Authorization (токены, API-ключи)
        * Content-Type
        * Кастомные заголовки (например, X-Request-ID)
    2. Автоматическая конвертация и валидация
    - FastAPI автоматически парсит значения заголовков в указанный тип (например, str, int, bool).
    3. Указание альтернативных имен и значений по умолчанию
    - Можно задать:
        * alias (если заголовок называется не так, как параметр функции),
        * default (значение, если заголовок отсутствует).

Примеры использования:
1. Получение заголовка User-Agent:

    from fastapi import FastAPI, Header
    app = FastAPI()

    @app.get("/user-agent/")
    async def get_user_agent(user_agent: str = Header(...)):
        return {"User-Agent": user_agent}

    Здесь Header(...) означает, что заголовок обязателен. Если его нет — FastAPI вернет ошибку 422.

2. Кастомный заголовок с дефолтным значением:
    
    from fastapi import FastAPI, Header
    app = FastAPI()

    @app.get("/items/")
    async def read_items(x_token: str = Header(default="secret-token")):
        return {"X-Token": x_token}
    
    Если клиент не передаст X-Token, будет использовано "secret-token".

3. Заголовок с другим именем (алиас):

    from fastapi import FastAPI, Header
    app = FastAPI()

    @app.get("/secure/")
    async def secure_endpoint(api_key: str = Header(..., alias="X-API-Key")):
        return {"API-Key": api_key}

    FastAPI будет искать заголовок X-API-Key, но в функции он будет доступен как api_key.

Важные нюансы:
Автоматическое приведение типов:
    FastAPI пытается конвертировать заголовки в указанный тип. 
    Например: 
        is_admin: bool = Header(False)  # "true" → True, "1" → True, etc.
Стандартные заголовки:
    Некоторые заголовки (например, Accept-Encoding) могут содержать дефисы (-), поэтому в Python их нужно указывать с подчеркиванием (_), а FastAPI автоматически проведет маппинг:
        accept_encoding: str = Header(...)  # Сработает для "Accept-Encoding"
Несколько заголовков:
    Если заголовок может прийти несколько раз (например, Set-Cookie), укажите list:
        cookies: list[str] = Header([])

Header — это удобный инструмент FastAPI для работы с HTTP-заголовками, обеспечивающий валидацию, конвертацию типов и гибкость в настройке.
#####


Класс Depends в FastAPI — это инструмент для внедрения зависимостей (Dependency Injection). 
Он позволяет:
    - Выносить повторяющуюся логику (аутентификацию, проверки, доступ к БД) в отдельные функции/классы.
    - Упрощать тестирование (зависимости легко подменить на моки).
    - Автоматически вызывать код перед обработкой запроса (например, проверять токен или права доступа).

Основные сценарии использования Depends:
1. Разделение логики и повторное использование кода. Вместо того чтобы дублировать код в каждом эндпоинте, выносим его в отдельную функцию и внедряем через Depends.
    Пример: 
    
    # Проверка API-ключа. Здесь verify_api_key выполнится перед вызовом protected_route. Если ключ неверный — запрос прервется с ошибкой 403.
    from fastapi import FastAPI, Depends, HTTPException, Header

    app = FastAPI()

    def verify_api_key(api_key: str = Header(...)):
        if api_key != "secret-key":
            raise HTTPException(status_code=403, detail="Invalid API Key")
        return api_key

    @app.get("/protected/")
    async def protected_route(api_key: str = Depends(verify_api_key)):
        return {"message": "Access granted"}
    
2. Зависимости с параметрами. Зависимости могут принимать аргументы из пути запроса, query-параметров и т.д.
    Пример: 
    
    # Получение объекта из БД по ID. FastAPI автоматически передаст item_id из пути в get_item.
    from fastapi import FastAPI, Depends

    app = FastAPI()

    async def get_item(item_id: int):
        #запрос к базе данных
        return {"id": item_id, "name": "Sample Item"}

    @app.get("/items/{item_id}")
    async def read_item(item: dict = Depends(get_item)):
        return item

3. Многоуровневые зависимости. Зависимости могут зависеть от других зависимостей (как матрешка).
    Пример: 
    
    # Аутентификация + Проверка прав
    from fastapi import FastAPI, Depends, Header, HTTPException

    app = FastAPI()

    def get_current_user(token: str = Header(...)):
    return {"user": "admin", "token": token}  # В реальности тут расшифровка JWT

    def check_admin(user: dict = Depends(get_current_user)):
        if user["user"] != "admin":
            raise HTTPException(status_code=403, detail="Admins only")
        return user

    @app.get("/admin/")
    async def admin_panel(user: dict = Depends(check_admin)):
        return {"message": "Welcome, admin!"}

    # Сначала вызывается get_current_user (проверяет токен).
    # Затем check_admin (проверяет роль пользователя).
    # И только потом — основной эндпоинт admin_panel.

4. Использование классов как зависимостей. Depends работает не только с функциями, но и с классами (удобно для сложных зависимостей).
    Пример: 
    
    # Класс для работы с БД
    from fastapi import FastAPI, Depends, Header, HTTPException

    app = FastAPI()

    class Database:
        def __init__(self, url: str = "sqlite:///db.sqlite"):
            self.url = url

        def get_data(self):
            return {"data": "from database"}

    def get_db():
        return Database()  # В реальности тут подключение к БД

    @app.get("/data/")
    async def fetch_data(db: Database = Depends(get_db)):
        return db.get_data()

5. Глобальные зависимости для роутера или всего приложения. Можно задать зависимости для группы эндпоинтов или всего FastAPI-приложения.
    Пример: 
    
    # Проверка API-ключа для всех эндпоинтов
    from fastapi import FastAPI, Depends

    app = FastAPI(dependencies=[Depends(verify_api_key)])

    @app.get("/hello/")
    async def hello():
        return {"message": "Hello"}  # Будет требовать API-ключ

Ключевые преимущества Depends
✅ Чистый код — логика разделена на модули.
✅ Гибкость — зависимости можно комбинировать.
✅ Тестируемость — в тестах зависимости легко подменить.
✅ Автоматизация — FastAPI сам вызывает зависимости в нужный момент.

Важные нюансы
Порядок вызова: Зависимости выполняются в порядке их объявления.
Кеширование: По умолчанию результат зависимости кешируется в рамках одного запроса (если не нужен кеш, используйте use_cache=False в Depends).
Ошибки: Если зависимость вызывает HTTPException, запрос прерывается.

Итог
Depends — это "магический" инструмент FastAPI для создания чистой, модульной и легко тестируемой логики. Он особенно полезен для:
- Аутентификации (JWT, OAuth2).
- Доступа к базам данных.
-  Валидации параметров.
- Логирования и трейсинга запросов.
#####


Класс Query в FastAPI используется для работы с query-параметрами (параметрами URL, которые идут после ?). 
Он позволяет:
    - Извлекать значения query-параметров из запроса.

    - Валидировать их (проверять тип, длину, диапазон и т.д.).

    - Устанавливать значения по умолчанию, описания и примеры для документации API.

Основные возможности Query:


1. Простое извлечение query-параметра.
    # без дополнительных проверок
    from fastapi import FastAPI, Query

    app = FastAPI()

    @app.get("/items/")
    async def read_items(q: str = Query(...)):  # Обязательный параметр
        return {"q": q}

    # Запрос: /items/?q=hello → Ответ: {"q": "hello"}.
    # Если параметр q не передан — FastAPI вернет ошибку 422 (Unprocessable Entity).

2. Необязательные параметры и значения по умолчанию
    from fastapi import FastAPI, Query

    app = FastAPI()

    @app.get("/items/")
    async def read_items(q: str = Query(None)):  # Необязательный параметр
        return {"q": q}

    # Запрос: /items/ → Ответ: {"q": null}.
    # Запрос: /items/?q=test → Ответ: {"q": "test"}.
    # Можно задать свое значение по умолчанию: (q: str = Query("default_value"))

3. Валидация параметров
    # Проверка длины строки
    from fastapi import FastAPI, Query

    app = FastAPI()

    @app.get("/items/")
    async def read_items(q: str = Query(..., min_length=3, max_length=10)):
        return {"q": q}

    #   /?q=ab → Ошибка: длина должна быть ≥ 3.
    #   /?q=abcdefghijk → Ошибка: длина должна быть ≤ 10.
    # Регулярные выражения: (q: str = Query(..., regex="^[a-z]+$"))  # Только латинские буквы в нижнем регистре
    # Числовые параметры (min/max): (price: float = Query(..., gt=0, lt=1000))  # Число от 0 до 1000

4. Множественные значения (списки)
    # Получить несколько значений для одного параметра (например, /items/?q=foo&q=bar)
    from fastapi import FastAPI, Query

    app = FastAPI()

    @app.get("/items/")
    async def read_items(q: list[str] = Query(...)):
        return {"q": q}

    # Запрос: /items/?q=foo&q=bar → Ответ: {"q": ["foo", "bar"]}.

5. Метаданные для документации
    # Добавление описания, примеров и deprecated-флагов
    from fastapi import FastAPI, Query

    app = FastAPI()

    @app.get("/items/")
    async def read_items(
        q: str = Query(
            None,
            title="Search Query",
            description="Filter items by keyword",
            example="apple",
            deprecated=True
        )
    ):
        return {"q": q}
    

    # Это отобразится в Swagger и Redoc:
    # Подсказка с описанием.
    # Пример значения.
    # Пометка, что параметр устарел.

6. Алиасы (другое имя параметра)
    # Если query-параметр должен называться не так, как переменная в Python
    from fastapi import FastAPI, Query

    app = FastAPI()

    @app.get("/items/")
    async def read_items(search: str = Query(..., alias="q")):
        return {"search": search}
    
    # Запрос: /items/?q=hello → В функцию попадет search="hello".

Когда использовать Query?
- Обязательные/необязательные параметры в URL.
- Валидация входных данных (строки, числа, списки).
- Документирование API (описания, примеры).
- Специфичные названия параметров (алиасы).

Важные нюансы
Совместимость с Path и Body:
    Query работает только с query-параметрами. Для частей URL используйте Path, для тела запроса — Body.
Значения по умолчанию:
    Query(None) — параметр необязательный.
    Query(...) — параметр обязательный (аналог Required).
Deprecated-параметры:
    Пометка deprecated=True не влияет на логику, но предупреждает клиентов API об устаревании параметра.

Итог:
Query — это декларативный способ:
✅ Извлекать query-параметры.
✅ Валидировать их.
✅ Документировать API.
✅ Гибко настраивать поведение (алиасы, deprecated, примеры).

Без Query пришлось бы вручную парсить и проверять параметры из URL, что усложнило бы код.
#####


Класс Path в FastAPI используется для работы с параметрами пути (path parameters) — динамическими частями URL, 
которые извлекаются из самого пути запроса (например, items/42, где 42 — это ID элемента). 
Он предоставляет те же возможности, что и Query, но ориентирован именно на параметры пути.

Основные функции Path:
1. Извлечение значений из URL:
    # Позволяет декларативно получать параметры из пути и преобразовывать их в нужный тип (например, int, str, UUID).
    from fastapi import FastAPI, Path

    app = FastAPI()

    @app.get("/items/{item_id}")
    async def read_item(item_id: int = Path(...)):  # Обязательный параметр
        return {"item_id": item_id}

    # Запрос GET /items/42 → {"item_id": 42}.
    # Если передать не число (например, items/foo), FastAPI автоматически вернёт ошибку 422 (Unprocessable Entity).

2. Можно задавать ограничения для значений:
    - Числовые параметры: gt (больше), ge (больше или равно), lt (меньше), le (меньше или равно).
    - Строковые параметры: min_length, max_length, regex.

    # Валидация параметров. 
    from fastapi import FastAPI, Path

    app = FastAPI()

    @app.get("/items/{item_id}")
    async def read_item(
        item_id: int = Path(..., gt=0, title="Item ID", description="Must be positive"),  # Только положительные числа
        name: str = Path(..., min_length=3, max_length=50)  # Строка от 3 до 50 символов
    ):
        return {"item_id": item_id, "name": name}
    
    # GET /items/-5 → Ошибка: item_id должен быть > 0.
    # GET /items/42?name=ab → Ошибка: name должен быть длиннее 3 символов.

3. Метаданные для документации:
    # Как и в Query, можно добавлять описание, примеры и пометки для Swagger/Redoc
    from fastapi import FastAPI, Path

    app = FastAPI()

    @app.get("/users/{user_id}")
    async def get_user(
        user_id: int = Path(
            ...,
            title="User ID",
            description="Unique identifier for the user",
            example=123,
        )
    ):
        return {"user_id": user_id}

4. Параметры с дефолтными значениями:
    # Хотя параметры пути обычно обязательные, можно задать значение по умолчанию (редкий случай, но возможно)
    from fastapi import FastAPI, Path

    app = FastAPI()

    app.get("/items/{item_id}")
    async def read_item(item_id: int = Path(default=1)):  # Если не передать, будет 1
        return {"item_id": item_id}

    # Но чаще Path(...) используется для обязательных параметров.


Ключевые отличия Path от Query
Path	                                            Query
Для параметров в URL-пути (/items/{item_id}).	    Для параметров в URL-строке (/items?name=foo).
Почти всегда обязательный.	                        Может быть обязательным или нет.
Валидация: gt, ge, lt, le (для чисел).	            Валидация: min_length, regex (для строк).
Используется, когда параметр — часть пути.	        Используется для фильтрации, сортировки и т.д.


Примеры использования:
    from fastapi import FastAPI, Path

    app = FastAPI()

    # Сложная валидация числа
    @app.get("/products/{product_id}")
    async def get_product(
        product_id: int = Path(..., gt=1000, le=9999),  # Допустим, ID товара от 1001 до 9999
    ):
        return {"product_id": product_id}

        # GET /products/500 → Ошибка: product_id должен быть > 1000.
        # GET /products/1001 → Успех: {"product_id": 1001}.

    # Использование с Query и Path вместе
    @app.get("/users/{user_id}/orders")
    async def get_orders(
        user_id: int = Path(..., title="User ID"),
        limit: int = Query(10, gt=0),  # Query-параметр
        active_only: bool = Query(True)  # Ещё один query-параметр
    ):
        return {"user_id": user_id, "limit": limit, "active_only": active_only}

        # Запрос: GET /users/42/orders?limit=5&active_only=false.
        # Ответ: {"user_id": 42, "limit": 5, "active_only": false}.

    # UUID вместо чисел
    from uuid import UUID

    @app.get("/files/{file_id}")
    async def read_file(file_id: UUID = Path(...)):  # Автоматическая валидация UUID
        return {"file_id": file_id}

    # Запрос: GET /files/123e4567-e89b-12d3-a456-426614174000 → Успех.
    # Запрос: GET /files/123 → Ошибка: невалидный UUID.

Класс Path в FastAPI нужен для:
- Извлечения параметров из пути URL.
- Валидации значений (числа, строки, UUID).
- Документирования API (описания, примеры).
- Гибкой настройки (алиасы, deprecated-флаги).

Используйте его для всех динамических параметров в пути, чтобы код был надёжным и самодокументируемым! 
#####


Класс status в FastAPI (импортируется из fastapi.status) предоставляет HTTP-коды состояния в виде удобных констант. 
Это делает код чище, избегая "магических чисел" и снижая риск ошибок.
Зачем использовать status вместо "сырых" чисел?
    - Читаемость – status.HTTP_200_OK понятнее, чем просто 200.
    - Автодополнение – IDE подскажет возможные коды (меньше шансов ошибиться).
    - Совместимость – гарантия, что код корректен (например, нет 999).

Основные HTTP-коды из status:
# Успешные ответы
status.HTTP_200_OK  # 200 (OK)
status.HTTP_201_CREATED  # 201 (Создано)
status.HTTP_204_NO_CONTENT  # 204 (Нет содержимого)

# Ошибки клиента
status.HTTP_400_BAD_REQUEST  # 400 (Неверный запрос)
status.HTTP_401_UNAUTHORIZED  # 401 (Не авторизован)
status.HTTP_403_FORBIDDEN  # 403 (Запрещено)
status.HTTP_404_NOT_FOUND  # 404 (Не найдено)

# Ошибки сервера
status.HTTP_500_INTERNAL_SERVER_ERROR  # 500 (Внутренняя ошибка сервера)

Примеры использования:
1. Указание кода ответа в эндпоинте:
    from fastapi import FastAPI, status

    app = FastAPI()

    @app.post("/items/", status_code=status.HTTP_201_CREATED)
    async def create_item():
        return {"message": "Item created"}
    
    # При успешном выполнении вернётся код 201.

2. Возврат ошибки с конкретным статусом:
    from fastapi import FastAPI, status, HTTPException

    app = FastAPI()

    @app.get("/items/{id}")
    async def read_item(id: int):
        if id == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )
        return {"id": id}

    # Если id=0, клиент получит 404.

3. Кастомные статусы для редких сценариев:
    from fastapi import FastAPI, status, HTTPException

    app = FastAPI()

    @app.post("/payment/")
    async def process_payment():
        # Например, 402 (Требуется оплата) для платного API
        return {"detail": "Payment required"}, status.HTTP_402_PAYMENT_REQUIRED

Класс содержит все стандартные HTTP-статусы из RFC (включая редкие, например):
    HTTP_418_IM_A_TEAPOT (418 Я — чайник)
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS (451 Недоступно по юридическим причинам)


fastapi.status – это коллекция стандартных HTTP-кодов в виде констант.
Используется для:
- status_code в декораторах (@app.get).
- HTTPException(status_code=...).
- Ручного возврата статусов (return Response(status_code=...)).
Плюсы: читаемость, надёжность, документация прямо в коде.

Пример:
    from fastapi import FastAPI, status, HTTPException

    app = FastAPI()

    @app.get("/admin/", status_code=status.HTTP_200_OK)
    async def admin_panel():
        if not is_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Admins only!"
            )
        return {"message": "Welcome, admin!"}

#####


Класс Body в FastAPI используется для работы с данными, переданными в теле HTTP-запроса (обычно в формате JSON). 
Он позволяет:
    - Извлекать и валидировать данные из тела запроса.
    - Указывать обязательные/необязательные поля.
    - Документировать API (добавлять описания, примеры).
    - Гибко настраивать поведение (например, вложенные структуры, поля с альтернативными именами).

Основные функции Body:
1. Извлечение данных из тела запроса
    # получение JSON-объекта в POST-запросе.
    from fastapi import FastAPI, Body

    app = FastAPI()

    @app.post("/items/")
    async def create_item(item: dict = Body(...)):  # Обязательное тело запроса
        return {"item": item}

    # Запрос: curl -X POST http://localhost:8000/items/ -H "Content-Type: application/json" -d '{"name": "Book", "price": 100}'
    # Ответ: {"item": {"name": "Book", "price": 100}}

2. Валидация данных. Body поддерживает те же правила валидации, что и Pydantic:
    - min_length, max_length (для строк).
    - gt, lt (для чисел).
    - Регулярные выражения (regex).

    # Пример с валидацией:
    from fastapi import FastAPI, Body
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        price: float = Body(..., gt=0)  # Цена должна быть > 0

    @app.post("/items/")
    async def create_item(item: Item):
        return item

    # Если передать {"name": "Book", "price": -10}, FastAPI вернёт ошибку 422.

3. Работа с вложенными структурами.
    # Body позволяет обрабатывать сложные JSON-структуры.
    from fastapi import FastAPI, Body

    app = FastAPI()

    @app.post("/orders/")
    async def create_order(
        order: dict = Body(..., example={
            "user_id": 1,
            "items": [{"id": 1, "quantity": 2}]
        })
    ):
        return order

    # В Swagger автоматически появится пример тела запроса.

4. Несколько тел запроса.
    # Если нужно принять несколько JSON-объектов в одном запросе:
    from fastapi import FastAPI, Body

    app = FastAPI()

    @app.post("/merge/")
    async def merge_data(
        user: dict = Body(...),
        item: dict = Body(...)
    ):
        return {"user": user, "item": item}

    # Тело запроса: {"user": {"name": "John"}, "item": {"title": "Laptop"}}

5. Документирование API.
    # Добавление описаний и примеров
    from fastapi import FastAPI, Body

    app = FastAPI()

    app.post("/users/")
    async def create_user(
        user: dict = Body(
            ...,
            title="User Data",
            description="Содержит имя и email пользователя",
            example={"name": "Alice", "email": "alice@example.com"}
        )
    ):
        return user

    # В Swagger/Redoc появится подробная документация.

Когда использовать Body:
- POST/PUT/PATCH-запросы — когда данные передаются в теле (не в URL).
- Сложные структуры — вложенные объекты, массивы.
- Валидация — проверка формата данных перед обработкой.
- Документирование — для автоматической генерации OpenAPI-схемы.

Отличия Body от Query и Path
Параметр	Где используется	        Пример
Body	    Тело запроса (JSON/XML)	    { "name": "Book" }
Query	    Параметры URL (?name=Book)	/items?name=Book
Path	    Параметры пути (/items/1)	/items/1

Важные нюансы:
Обязательность: Body(...) — поле обязательно, Body(None) — необязательно.
Content-Type: По умолчанию ожидается application/json.
Алиасы: Можно переименовывать поля (например, для совместимости с другими API): item_name: str = Body(..., alias="itemName")
#####


Класс HTTPException в FastAPI — это специальный инструмент для возврата HTTP-ошибок клиенту с удобным форматированием. 
Он позволяет прервать выполнение запроса и сразу отправить клиенту сообщение об ошибке с нужным статус-кодом (например, 404 Not Found или 403 Forbidden).

Зачем нужен HTTPException:
- Гибкое управление ошибками — можно быстро прервать запрос и вернуть клиенту понятное сообщение.
- Стандартизация ответов — все ошибки будут в одном формате (с кодом статуса и деталями).
- Интеграция с OpenAPI — ошибки автоматически документируются в Swagger/Redoc.

1. Простой вызов ошибки.
    from fastapi import FastAPI, HTTPException

    app = FastAPI()

    @app.get("/items/{item_id}")
    async def read_item(item_id: int):
        if item_id == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"item_id": item_id}

    # Если передан item_id=0, клиент получит:
    # json {"detail": "Item not found"} с HTTP-статусом 404.

2. Дополнительные поля.
    # Можно добавить любые JSON-данные в ответ
    from fastapi import FastAPI, HTTPException

    app = FastAPI()

    @app.get("/items/{item_id}")
    async def read_item(item_id: int):
        if item_id == 0:
            raise HTTPException(
                status_code=400,
                detail="Invalid input",
                headers={"X-Error": "Missing data"},
                extra={"field": "price", "expected_type": "float"}
            )
        return {"item_id": item_id}

    # Ответ: json {"detail": "Invalid input", "field": "price", "expected_type": "float"}

3. Кастомные заголовки
    from fastapi import FastAPI, HTTPException

    app = FastAPI()

    @app.get("/items/{item_id}")
    async def read_item(item_id: int):
        if item_id == 0:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return {"item_id": item_id}

    # Полезно для ошибок аутентификации (например, OAuth2).

Примеры частых ошибок и их кодов:
Код	Тип ошибки	        Пример использования
400	Неверный запрос	    Некорректные данные от клиента.
401	Не авторизован	    Пользователь не представил токен.
403	Доступ запрещён	    Нет прав для действия.
404	Не найдено	        Запрашиваемый ресурс отсутствует.
422	Ошибка валидации	Автоматически возникает при неверных данных.
500	Ошибка сервера	    Для непредвиденных сбоев.

Примеры из реальной практики
1. Проверка прав доступа

async def check_admin(user_role: str):
    if user_role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admins can perform this action"
        )

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, current_user: str = Depends(get_current_user)):
    await check_admin(current_user.role)
    # ...удаление пользователя

2. Обработка несуществующих данных

@app.get("/products/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

3. Кастомная ошибка для бизнес-логики

@app.post("/payment/")
async def process_payment(amount: float):
    if amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be positive",
            headers={"X-Reason": "Invalid amount"}
        )
    # ...обработка платежа

Как HTTPException интегрируется с FastAPI:
- Автоматическая конвертация в JSON-ответ.
- Логирование — ошибки попадают в лог сервера.
- Документация — поддерживается OpenAPI/Swagger.

Важные нюансы
Отличие от status
    status содержит константы кодов (например, status.HTTP_404_NOT_FOUND).
    HTTPException — это инструмент для генерации ошибок.

Когда использовать, а когда нет?
    Использовать: для ожидаемых ошибок (нет прав, не найдено).
    Не использовать: для критических сбоев сервера (лучше логировать и возвращать 500).

Глобальная обработка
    Можно перехватывать все HTTPException через кастомные обработчики.

📌 Итог
Класс HTTPException в FastAPI нужен для:
✅ Гибкой генерации HTTP-ошибок.
✅ Возврата структурированных сообщений клиенту.
✅ Интеграции с OpenAPI (документация ошибок).

Без него пришлось бы вручную создавать JSONResponse с ошибками, что усложнило бы код.

Пример «как не надо» (без HTTPException):
python

from fastapi.responses import JSONResponse

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 0:
        return JSONResponse(
            status_code=404,
            content={"message": "Item not found"}
        )
    return {"item_id": item_id}

Пример «как надо» (с HTTPException):
python

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

Код становится чище, а ошибки — стандартизированными! 