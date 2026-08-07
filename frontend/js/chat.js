const socket =
io(
"http://localhost:5000"
);



let currentConversation=null;


const user_id =
localStorage.getItem(
"user_id"
);


const username =
localStorage.getItem(
"username"
);





function joinConversation(id){


currentConversation=id;



socket.emit(
"join_conversation",
{

conversation_id:id

}

);



loadMessages(id);


}





function sendMessage(){


let input =
document.getElementById(
"message"
);



let text=input.value;


if(!text)
return;



socket.emit(
"send_message",
{

conversation_id:
currentConversation,


sender_id:
user_id,


sender:
username,


content:
text


}

);



input.value="";


}




socket.on(
"receive_message",

data=>{


displayMessage(data);


}

);





function displayMessage(data){



let box=
document.getElementById(
"messages"
);



box.innerHTML+=`


<div class="message">


<div>
${data.content}
</div>


<div class="sender">

${data.sender}

</div>


</div>


`;



box.scrollTop=
box.scrollHeight;


}






function loadMessages(id){


fetch(
"http://localhost:5000/messages/"+id
)

.then(
res=>res.json()
)

.then(
data=>{


document.getElementById(
"messages"
).innerHTML="";


data.forEach(
msg=>{

displayMessage(msg);

}

);


}

);


}