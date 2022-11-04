from typing import List

from pydantic import BaseModel


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


class UserWebsite(BaseModel):
    website: str


class UserSchema(UserWebsite):
    id: int
    name: str
    username: str
    email: str
    address: UserAddress
    phone: str
    company: UserCompany


class UsersList(BaseModel):
    __root__: List[UserSchema]


class UsersListWebsite(BaseModel):
    websites: List[UserWebsite]


class UserDetails(BaseModel):
    name: str
    email: str
    company: str


class UsersListDetails(BaseModel):
    users: List[UserDetails]
