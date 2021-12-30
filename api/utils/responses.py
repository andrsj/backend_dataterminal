import fastapi
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from api.sql_app.repositories import UserRepository
from api.discord.client import bot
from api.config import GUILD_ID, ROLES
from api.discord.utils import get_guild_member_by_id


def get_user_response(db: Session, user_id):
    db_user = UserRepository.get_by_user_id(db, user_id)

    guild = bot.get_guild(int(GUILD_ID))
    user = get_guild_member_by_id(user_id, guild)

    print([role.id for role in user.roles], [role.name for role in user.roles])
    print([int(i) for i in ROLES])
    print(any(role.id not in [int(i) for i in ROLES] for role in user.roles))

    if not any(role.id in [int(i) for i in ROLES] for role in user.roles):
        return JSONResponse(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            content={
                'msg': "User doesn't have a required role",
            }
        )

    if db_user:
        return JSONResponse(
            status_code=fastapi.status.HTTP_200_OK,
            content={
                'msg': 'User already exists',
                'session_token': db_user.session_token
            }
        )

    new_db_user = UserRepository.add(db, user_id)
    return JSONResponse(
        status_code=fastapi.status.HTTP_201_CREATED,
        content={
            'msg': 'User was successfully created',
            'session_token': new_db_user.session_token
        }
    )
