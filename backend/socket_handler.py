from flask_socketio import join_room, emit


def socket_events(socketio):


    @socketio.on("join_conversation")
    def join_conversation(data):

        conversation_id = data["conversation_id"]

        join_room(conversation_id)



    @socketio.on("send_message")
    def send_message(data):

        conversation_id = data["conversation_id"]


        emit(
            "receive_message",
            data,
            room=conversation_id
        )
