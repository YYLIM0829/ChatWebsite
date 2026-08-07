from flask import Flask, render_template

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

    return render_template(
        "login.html"
    )

@app.route("/register")
def register_page():
    return render_template("register.html")
    
@app.route("/chat")
def chat():

    return render_template(
        "chat.html"
    )



if __name__=="__main__":

    socketio.run(
        app,
        debug=True
    )
