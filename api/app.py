import asyncio


from fastapi import FastAPI


from api.discord.client import bot
from api.config import BOT_TOKEN
from api.routes import discord
from api.sql_app import model, database


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(bot.start(BOT_TOKEN))
    await asyncio.sleep(4)
    print(f"{bot.user} has connected to Discord! by startup FastAPI")


app.include_router(
    discord.router,
    prefix="/discord",
)

model.Base.metadata.create_all(bind=database.engine)
