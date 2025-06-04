from sqlalchemy import create_engine

# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
engine = create_engine("postgresql+psycopg2://admin:admin@localhost/example_db", 
                       echo=True)
engine.connect()

print(engine)