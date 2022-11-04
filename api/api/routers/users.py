import requests
from fastapi import APIRouter, status

from api.schemas import UsersList, UsersListWebsite, UserWebsite

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("/websites", response_model=UsersListWebsite, status_code=status.HTTP_200_OK)
def get_users_websites():
    users_list = _get_users_list().__root__
    list_websites = UsersListWebsite(
        websites=[UserWebsite(website=user.website) for user in users_list]
    )
    to_return = UsersListWebsite(**list_websites.dict())
    return to_return


def _get_users_list():

    r = requests.get("https://jsonplaceholder.typicode.com/users")
    users_list = UsersList.parse_raw(r.content)
    return users_list
