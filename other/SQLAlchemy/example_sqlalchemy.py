#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///users.db")
Base = declarative_base()

class User(Base):

	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	age = Column(Float, nullable=False)

Session = sessionmaker(bind=engine)
session = Session()

user = User(name='Rafael', age=5.5)

session.add(user)
session.commit()

user = session.query(User).filter_by(name='Ruslan').first()
print(user.name)

if __name__ == "__main__":
	Base.metadata.create_all(engine)


