import re

import requests
from fastapi import APIRouter, status

from api.schemas import (
    UserDetails,
    UserIdName,
    UsersList,
    UsersListDetails,
    UsersListMatchName,
    UsersListWebsite,
    UserWebsite,
)

router = APIRouter(prefix="/api/users", tags=["Users"])


def _get_users_list() -> UsersList:
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    users_list = UsersList.parse_raw(r.content)
    return users_list


@router.get("/websites", response_model=UsersListWebsite, status_code=status.HTTP_200_OK)
def get_users_websites():
    users_list = _get_users_list().__root__
    list_websites = UsersListWebsite(
        websites=[UserWebsite(website=user.website) for user in users_list]
    )
    return list_websites


@router.get("/detail", response_model=UsersListDetails, status_code=status.HTTP_200_OK)
def get_users_details():
    users_list = _get_users_list().__root__
    users_details_list = [
        UserDetails(
            name=user.name,
            email=user.email,
            company=user.company.name,
        )
        for user in users_list
    ]
    users_details_list_sorted = sorted(users_details_list, key=lambda x: x.name)
    list_details = UsersListDetails(users=users_details_list_sorted)
    return list_details


@router.get("", response_model=UsersListMatchName, status_code=status.HTTP_200_OK)
def get_users_match_name(name: str = None):
    users_list = _get_users_list().__root__
    users_list_match_name = [
        UserIdName(
            id=user.id,
            name=user.name,
        )
        for user in users_list
        if re.search(name, user.name) is not None
    ]
    users_list_match_name_sorted = sorted(users_list_match_name, key=lambda x: x.name)
    list_match_name = UsersListMatchName(users=users_list_match_name_sorted)
    return list_match_name
