from flask import Blueprint, request, jsonify

from database import supabase

@conversation.route(
"/conversation/private",
methods=["POST"]
)
def create_private():

    data=request.json


    user1=data["user1_id"]

    user2=data["user2_id"]



    # 查询双方已有聊天

    chats=supabase.table(
        "conversation_members"
    ).select(
        "conversation_id,user_id"
    ).in_(
        "user_id",
        [
            user1,
            user2
        ]
    ).execute()



    conversation_ids={}



    for item in chats.data:

        cid=item["conversation_id"]

        if cid not in conversation_ids:

            conversation_ids[cid]=0

        conversation_ids[cid]+=1



    # 两个人都存在同一个聊天

    for cid,count in conversation_ids.items():

        if count==2:


            result=supabase.table(
                "conversations"
            ).select("*").eq(
                "id",
                cid
            ).eq(
                "type",
                "private"
            ).execute()



            if result.data:

                return jsonify({

                    "conversation_id":cid

                })



    # 创建新的 private chat


    new_chat=supabase.table(
        "conversations"
    ).insert({

        "type":"private",

        "created_by":user1

    }).execute()



    cid=new_chat.data[0]["id"]



    # 加入成员

    supabase.table(
        "conversation_members"
    ).insert([

        {
        "conversation_id":cid,
        "user_id":user1
        },


        {
        "conversation_id":cid,
        "user_id":user2
        }

    ]).execute()



    return jsonify({

        "conversation_id":cid

    })

@conversation.route(
"/conversation/group",
methods=["POST"]
)
def create_group():


    data=request.json


    name=data["name"]

    owner=data["user_id"]



    group=supabase.table(
        "conversations"
    ).insert({

        "type":"group",

        "name":name,

        "created_by":owner

    }).execute()



    cid=group.data[0]["id"]



    # 创建者加入

    supabase.table(
        "conversation_members"
    ).insert({

        "conversation_id":cid,

        "user_id":owner,

        "role":"admin"

    }).execute()



    return jsonify({

        "conversation_id":cid

    })

@conversation.route(
"/conversation/join",
methods=["POST"]
)
def join_group():


    data=request.json


    cid=data["conversation_id"]

    user=data["user_id"]



    supabase.table(
        "conversation_members"
    ).insert({

        "conversation_id":cid,

        "user_id":user,

        "role":"member"

    }).execute()



    return jsonify({

        "message":"joined"

    })

@conversation.route(
"/conversations/<user_id>",
methods=["GET"]
)
def get_conversations(user_id):


    members=supabase.table(
        "conversation_members"
    ).select(
        "conversation_id"
    ).eq(
        "user_id",
        user_id
    ).execute()



    ids=[

        x["conversation_id"]

        for x in members.data

    ]



    chats=supabase.table(
        "conversations"
    ).select("*").in_(
        "id",
        ids
    ).execute()



    return jsonify(
        chats.data
    )

@conversation.route(
"/conversation/<cid>/members",
methods=["GET"]
)
def get_members(cid):


    result=supabase.table(
        "conversation_members"
    ).select(
        "user_id"
    ).eq(
        "conversation_id",
        cid
    ).execute()



    return jsonify(
        result.data
    )

conversation = Blueprint(
    "conversation",
    __name__
)