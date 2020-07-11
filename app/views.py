from app import app, socketio
from flask import Flask, render_template
from flask_socketio import SocketIO

@app.route('/', methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')

@app.route('/', methods=['GET', 'POST'])
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

