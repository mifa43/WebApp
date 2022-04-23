function onGet() {
    const url = "http://0.0.0.0:8081/";
    var headers = {}
    
    fetch(url, {
        method : "GET",
        mode: 'cors',
        headers: headers
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(response.error)
        }
        return response.json();
        
    })
    .then(data => {
        
        document.getElementById('messages').value = data["Health"];
        console.log(data)
    })
    .catch(function(error) {
        document.getElementById('messages').value = error;
    });
}

async function postData () {
    let user = {
        UserName: document.getElementById("inputName").value,
        UserLastName: document.getElementById("inputLanme").value,
        UserPassword: document.getElementById("inputPassword").value,
        UserEmail: document.getElementById("inputEmail").value

    }
    try {
        const response = await axios.post("http://0.0.0.0:8081/register-user", user)
        console.log(user)
    } catch (error) {
        if (error.response) {
            console.log(error.reponse.status)
        } else {
            console.log(error.message)
        }
    }
}
 

// (async function postData(){
    

//     const rawResponse = await fetch('http://0.0.0.0:8081/register-user', {
        

//         method: 'POST',
//         headers: {
//             'Accept': 'application/json',
//             'Content-Type': 'application/json'
//         },
        
//         body: JSON.stringify({  
//             "UserName": "asdsd",
//             "UserLastName": "string",
//             "UserPassword": "string",
//             "UserEmal": "string"})
//     });
    
//     const content = await rawResponse.json();
    
//     window.alert("uspelo je");

//     console.log(content);
//     return false;

// })();


// https://developer.okta.com/blog/2021/08/02/fix-common-problems-cors