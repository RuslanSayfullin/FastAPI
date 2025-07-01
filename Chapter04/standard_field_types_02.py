from datetime import date
from enum import Enum

from pydantic import BaseModel, ValidationError

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interest: list[str]


# Invalid gender
try:
    Person(
        first_name="John",
        last_name="Peterson",
        gender="INVALID_VALUE",
        birthdate="1999-01-01",
        interest=["travel", "sports"]
    )
except ValidationError as e:
    print(str(e))

# Invalid birthdate
try:
    Person(
        first_name="John",
        last_name="Doe",
        gender=Gender.MALE,
        birthdate="1991-13-42",
        interests=["travel", "sports"],
    )
except ValidationError as e:
    print(str(e))

# Valid
person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports"],
)
print(person)