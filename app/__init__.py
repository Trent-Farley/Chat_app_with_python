from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__,template_folder='templates')
#Not a 'secret key' but for development processes this will work. 
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

from app import views

