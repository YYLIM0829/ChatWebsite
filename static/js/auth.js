const API =
"";



function register(){


fetch(
API+"/register",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

username:
document.getElementById("username").value,

email:
document.getElementById("email").value,

password:
document.getElementById("password").value


})

}

)
.then(
res=>res.json()
)
.then(
data=>{

alert(
"Registered"
);

location.href="login.html";


}
);


}




function login(){


fetch(
API+"/login",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

email:
document.getElementById("email").value,


password:
document.getElementById("password").value


})

}

)
.then(
res=>res.json()
)
.then(
data=>{


localStorage.setItem(
"user_id",
data.user_id
);


localStorage.setItem(
"username",
data.username
);


location.href="chat.html";


}
);


}
