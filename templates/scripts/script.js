// function onGet() {
//     const url = "http://0.0.0.0:8081/";
//     var headers = {}
    
//     fetch(url, {
//         method : "GET",
//         mode: 'cors',
//         headers: headers
//     })
//     .then((response) => {
//         if (!response.ok) {
//             throw new Error(response.error)
//         }
//         return response.json();
        
//     })
//     .then(data => {
//         document.getElementById('messages').value = data["Health"];
//         console.log(data)
//     })
//     .catch(function(error) {
//         document.getElementById('messages').value = error;
//     });
// }
// funkcija za slanje post requesta na register-user endpoint
async function postData () {
    // async funkcija za slanje requesta na api endpoint sa json body-em
    let user = {
        UserName: document.getElementById("inputName").value,
        UserLastName: document.getElementById("inputLanme").value,
        UserPassword: document.getElementById("inputPassword").value,
        UserEmail: document.getElementById("inputEmail").value

    }
    // pokusaj slanja post requesta. py(try: except:)
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
function validate() {
    // provera da li je input veci od 3

    var UserName = document.getElementById("inputName").value;
    var UserLastName = document.getElementById("inputLanme").value;
    var UserEmail = document.getElementById("inputEmail").value;
    var UserPassword = document.getElementById("inputPassword").value;
    

    if (UserName.length < 4) {
        window.alert("user name len: "+UserName.length)
      return false; // drzimo formu submitovanu

    }
    else if (UserLastName.length < 4) {
        window.alert("user lastname len: "+UserLastName.length)
      return false; // drzimo formu submitovanu

    }
    else if (UserEmail.length < 3) {
        window.alert("user email len: "+UserEmail.length)
      return false; // drzimo formu submitovanu

    }
    else if (UserPassword.length < 6) {
        window.alert("user password len: "+UserPassword.length)
      return false; // drzimo formu submitovanu

    }
    
    // else: input je dovoljno dugacak
    // pozivamo funkciju i saljemo request
    postData()
    window.alert("bravooo")
    window.location = "index.html";
    return true;
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