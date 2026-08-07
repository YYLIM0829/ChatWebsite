from flask import Flask

from flask_cors import CORS

from flask_socketio import SocketIO


from auth import auth

from conversation import conversation

from message import message

from socket_handler import socket_events



app=Flask(__name__)


CORS(app)



socketio=SocketIO(

    app,

    cors_allowed_origins="*"

)



app.register_blueprint(auth)

app.register_blueprint(conversation)

app.register_blueprint(message)



socket_events(socketio)



@app.route("/")
def home():

    return "Server Running"



if __name__=="__main__":

    socketio.run(
        app,
        debug=True
    )
