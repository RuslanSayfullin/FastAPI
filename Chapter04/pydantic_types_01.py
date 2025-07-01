from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

class User(BaseModel):
    email: EmailStr
    website: HttpUrl


# Invalid email
try:
    User(email="jdoe", website="https://www.google.com")
except ValidationError as e:
    print(str(e))

# Invalid URL
try:
    User(email="jdoe@google.com", website="jdoe")
except ValidationError as e:
    print(str(e))

# Valid
user = User(eamil="jdoe@google.com", website=HttpUrl("https://www.google.com"))
print(user)