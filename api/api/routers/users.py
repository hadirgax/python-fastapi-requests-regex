from fastapi import APIRouter, status

from api.schemas import UsersListWebsite, UserWebsite

router = APIRouter(prefix="/api/users", tags=["Orders"])


@router.get("/websites", response_model=UsersListWebsite, status_code=status.HTTP_200_OK)
def get_users_websites():
    list_websites = UsersListWebsite(
        websites=[UserWebsite(website="test1.com"), UserWebsite(website="test2.com")], size=1
    )
    to_return = UsersListWebsite(**list_websites.dict())
    return to_return
