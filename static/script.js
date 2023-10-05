function Toggle() {
    if (document.getElementById("hidden").innerHTML == "Show") {
        document.getElementById("hidden").innerHTML = "Hide";
        document.getElementById("pwdtype").type = "text" ;
    }
    else {
        document.getElementById("hidden").innerHTML = "Show" ;
        document.getElementById("pwdtype").type = "password" ;
    }
}

let user ;
let pass ;
function getuser  () {return document.getElementById("usertype").value;}
function getpass  () {return document.getElementById("pwdtype").value;}

function submitusr(usr) {
    const data1 = {
        variableName: 'username',
        variableValue: usr 
}
    return data1 ;
}

function submitpwd(pwd) {
    const data2 = {
        variableName: 'password',
        variableValue: pwd 
}
    return data2 ; 
}

document.getElementById("hmidabutton").addEventListener("click", function() {
    submitpwd(pass);
    submitusr(user);
    document.getElementById("btn").href = "http://127.0.0.1:5000/create_token?username="+ getuser() + "&password=" + getpass() ;
});
 