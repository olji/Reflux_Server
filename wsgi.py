#from bm2dx import app
from bm2dx import app, socket
from flask_socketio import SocketIO

if __name__ == "__main__":
    socket.run(app)
    #app.run()
