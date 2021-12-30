from flask import Flask, render_template_string, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socket_io = SocketIO(app)


@app.route('/')
def home():
    return render_template_string('''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
<script type="text/javascript" charset="utf-8">
    var socket = io({auth: {token: "123"}});
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\\'m connected!'});
    });
    socket.on('broadcast', function(data) {
        console.log(data)
        document.body.innerText = JSON.stringify(data)
    });
</script>''')


@socket_io.on('connect')
def handle_my_custom_event(c):
    print('connected', c, request)
    emit('broadcast', {'data': True})


if __name__ == '__main__':
    socket_io.run(app)
