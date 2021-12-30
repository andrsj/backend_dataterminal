from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from api.discord.client import bot
from api.discord.utils import send_message
from api.utils.requests import exchange_code, get_current_authorization_information
from api.utils.responses import get_user_response
from api.utils.database import get_db


router = APIRouter()


@router.get('/')
async def root():
    return "Hello, discord"


@router.get('/list')
async def list_of_members():
    guild = bot.get_guild(922163223388618793)
    return {'members': [m.id for m in guild.members]}


@router.get("/msg/{channel_id}")
async def read_item(channel_id: int, msg: str):
    channel = await send_message(msg, channel_id)  # 922163233538850879
    return {"channel_id": channel.id, "msg": msg}


@router.get('/auth')
async def auth(code: str, redirect_uri: str, db: Session = Depends(get_db)):
    token = exchange_code(code, redirect_uri).get('access_token')
    result = get_current_authorization_information(token)
    user_id = result.get('user').get('id')

    return get_user_response(db, user_id)
