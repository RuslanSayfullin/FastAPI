from pydantic import BaseModel, ValidationError

class UserProfile(BaseModel):
    nickname: str
    location: str | None = None
    subscribed_newsletter: bool = True

# Valid
try:
    profile = UserProfile(
        nickname="CryptoLis",
        location="Ufa",
        subscribed_newsletter=False,
    )
    print(profile)
except ValidationError as e:
    print(str(e))