from flask import Blueprint,request,jsonify

from database import supabase

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


auth=Blueprint(
    "auth",
    __name__
)



@auth.route(
"/register",
methods=["POST"]
)
def register():


    data=request.json


    username=data["username"]

    email=data["email"]

    password=data["password"]



    hashed=generate_password_hash(
        password
    )


    result=supabase.table(
        "users"
    ).insert({

        "username":username,

        "email":email,

        "password":hashed

    }).execute()



    return jsonify({

        "message":"registered"

    })





@auth.route(
"/login",
methods=["POST"]
)
def login():


    data=request.json


    email=data["email"]

    password=data["password"]



    user=supabase.table(
        "users"
    ).select("*").eq(
        "email",
        email
    ).execute()



    if not user.data:

        return jsonify({

            "error":"user not found"

        }),404



    db_user=user.data[0]



    if check_password_hash(

        db_user["password"],

        password

    ):


        return jsonify({

            "success":True,

            "user_id":db_user["id"],

            "username":db_user["username"]

        })



    return jsonify({

        "error":"wrong password"

    }),401