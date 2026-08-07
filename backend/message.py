from flask import Blueprint, request, jsonify

from database import supabase

@message.route(
"/message/send",
methods=["POST"]
)
def send_message():


    data=request.json


    conversation_id=data["conversation_id"]

    sender_id=data["sender_id"]

    content=data["content"]



    result=supabase.table(
        "messages"
    ).insert({

        "conversation_id":conversation_id,

        "sender_id":sender_id,

        "content":content

    }).execute()



    return jsonify({

        "message":"sent",

        "data":result.data[0]

    })

@message.route(
"/messages/<cid>",
methods=["GET"]
)
def get_messages(cid):


    result=supabase.table(
        "messages"
    ).select(
        "*"
    ).eq(
        "conversation_id",
        cid
    ).order(
        "created_at"
    ).execute()



    return jsonify(
        result.data
    )

from flask_socketio import (
    join_room,
    leave_room,
    emit
)



def socket_events(socketio):


    @socketio.on(
        "join_conversation"
    )
    def join(data):


        conversation_id=data["conversation_id"]


        join_room(
            conversation_id
        )



    @socketio.on(
        "send_message"
    )
    def send(data):


        conversation_id=data["conversation_id"]


        emit(

            "receive_message",

            data,

            room=conversation_id

        )
        
message = Blueprint(
    "message",
    __name__
)