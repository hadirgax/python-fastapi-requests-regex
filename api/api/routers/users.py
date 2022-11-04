import requests
from fastapi import APIRouter, status

from api.schemas import (
    UserDetails,
    UsersList,
    UsersListDetails,
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
    to_return = UsersListWebsite(**list_websites.dict())
    return to_return


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
    to_return = UsersListDetails(**list_details.dict())
    return to_return
