import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pprint import pp


sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
socket_io_app = socketio.ASGIApp(sio, app)


list_of_SIDs = []


@sio.event
async def connect(sid, environ, auth):
    print(f"Connect: '{sid}' | Auth: '{auth}'")
    pp(environ['asgi.scope']['headers'])
    print('AUTH:', type(auth), auth)
    list_of_SIDs.append(sid)


@sio.event
async def message(sid, data):
    # await sio.send(text_of_message, room=sid)
    print(f"[SID:{sid}] Message: '{data}'")


@sio.event
async def disconnect(sid):
    print(f"Disconnect: '{sid}'")
    list_of_SIDs.remove(sid)


@sio.on('clock')
async def message_clock(sid, data):
    print(f"Message from clock[sid:{sid}]: '{data}'")


@app.get("/{text}")
async def root(text: str):
    # await sio.send(text)
    await sio.emit('broadcast', text)
    return f"Message '{text}' sent to everyone: {list_of_SIDs}"


@app.on_event("startup")
async def startup_event():
    return
    print('START background task for server')
    sio.start_background_task(worker)


async def worker():
    print("SERVER WORKER STARTED")
    sec = 0
    while True:
        print('Send message from worker to everyone:', list_of_SIDs)
        await sio.emit('clock', f'Server time: {sec}')
        sec += 1
        await sio.sleep(1)


if __name__ == '__main__':
    uvicorn.run("server:socket_io_app", host='localhost', port=5000, reload=True)
