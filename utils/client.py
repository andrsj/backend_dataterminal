import socketio
from requests import Session, Request

# s = Session()
# s.auth = (u'TestUser', 'auth-key')
# s.headers.update({'key': 'qwertyuiop', 'Authorization': 'Basic TOKEN'})
# s.headers.update({'Authorization': 'Basic TOKEN'})
# sio = socketio.Client(http_session=s)


sio = socketio.Client()


@sio.event
def connect():
    print(f'Connection established with SID: {sio.get_sid()}')
    # sio.emit('message', 'Hello, server')
    # sio.start_background_task(worker)


def worker():
    print("CLIENT WORKER STARTED")
    while True:
        text = input('Message: ')
        sio.emit('message', text)
    # sec = 0
    # while True:
    #     print(f"Send message 'Client time: {sec}' from worker to server with sid:", sio.get_sid())
    #     sio.emit('clock', f'Client time: {sec}')
    #     sec += 1
    #     sio.sleep(1)


@sio.event
def message(data):
    print(f"Message received with '{data}' [SID: {sio.get_sid()}]")


# @sio.on('clock')
# def get_clock_message(data):
#     print(f"Clock: '{data}' [SID: {sio.get_sid()}]")


@sio.on('broadcast')
def event(data):
    print('Broadcast:', data)


@sio.event
def disconnect():
    print('Disconnected from server')


if __name__ == '__main__':
    # sio.connect('ws://api.dataterminal.ru/', wait_timeout=10)
    # sio.connect('ws://broadcast.dataterminal.ru', wait_timeout=10)
    # sio.connect('ws://178.250.158.79:5070/', wait_timeout=10)
    sio.connect('http://localhost:5000', auth='KekW', wait_timeout=10)
    sio.wait()
