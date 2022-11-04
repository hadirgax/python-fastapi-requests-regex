from typing import List

from pydantic import BaseModel


class UserWebsite(BaseModel):
    website: str


class UserGeo(BaseModel):
    lat: float
    lng: float


class UserAddress(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: UserGeo


class UserCompany(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: UserAddress
    phone: str
    website: UserWebsite
    company: UserCompany


class UsersListWebsite(BaseModel):
    websites: List[UserWebsite]
