from app import app, socketio
from flask import Flask, render_template
from flask_socketio import SocketIO

@app.route('/', methods=['GET', 'POST'])
def sessions():
    return render_template('index.html') #Flask auto looks in the /templates folder, this is 
    #Where this template is.

@app.route('/', methods=['GET', 'POST'])
def messageReceived(methods=['GET', 'POST']):
    print('Callback hit, this would typically be used for processing\n\
        but I don\'t have anything to process')

@socketio.on('my event')
def handle_event(json, methods=['GET', 'POST']):
    socketio.emit('my response', json, callback=messageReceived)

