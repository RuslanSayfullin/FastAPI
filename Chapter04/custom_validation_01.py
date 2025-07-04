from datetime import date

from pydantic import BaseModel, ValidationError, validator

class person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @validator
    def valid_birthdate(cls, v: date):
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValueError("You seem a bit too old!")
        return v