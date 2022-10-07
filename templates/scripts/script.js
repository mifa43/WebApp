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

// function postData () {
//     // async funkcija za slanje requesta na api endpoint sa json body-em
//     let user = {
//         UserName: document.getElementById("inputName").value,
//         UserLastName: document.getElementById("inputLanme").value,
//         UserEmail: document.getElementById("inputEmail").value,
//         UserNumber: document.getElementById("phonNumber").value,
//         UserPassword: document.getElementById("inputPassword").value,
//         UserRePassword: document.getElementById("inputRePassword").value

//     }
//     // pokusaj slanja post requesta. py(try: except:)
//     try {
//         const response = axios.post("http://0.0.0.0:8081/register-user", user)
//         console.log(user)
//         let header = document.querySelector("h6");
//         header.innerText = `Account created !`;
        
//         window.alert("You have successfully created an account and now we will send you an email verification!");

//         window.location.href = 'index.html';



//     } catch (error) {
//         if (error.response) {
//             let header = document.querySelector("h6");
//             console.log(error.message);
//             header.innerText = error.response.data.detail;
            
//         } else {
//             console.log(error.message);
//             header.innerText = error.response.data.detail;
          
//         }
//     }
// }
async function validate() {
    // provera da li je input veci od 3
    let header = document.querySelector("h6");
        
    var UserName = document.getElementById("inputName").value;
    var UserLastName = document.getElementById("inputLanme").value;
    var UserEmail = document.getElementById("inputEmail").value;
    var UserNumber = document.getElementById("phonNumber").value;
    var UserPassword = document.getElementById("inputPassword").value;
    var UserRepassword = document.getElementById("inputRePassword").value


    if (UserName.length < 4) {
        header.innerText = `User name must be longer than 4 characters`;
      return false; // drzimo formu submitovanu

    }
    else if (UserLastName.length < 4) {
        header.innerText = `Last name must be longer than 4 characters`;
      return false; // drzimo formu submitovanu

    }
    else if (UserEmail.length < 5) {
        header.innerText = `Email must be longer than 5 characters`;
      return false; // drzimo formu submitovanu

    }
    else if (UserNumber.length < 9) {
        header.innerText = `Phone Number must be longer than 9 numbers`;
      return false; // drzimo formu submitovanu

    }
    else if (UserPassword.length < 6) {
        header.innerText = `Password must be longer than 5 characters`;
      return false; // drzimo formu submitovanu

    }
    else if (UserRepassword.length < 6) {
        header.innerText = `Repeat Password must be longer than 5 characters`;
      return false; // drzimo formu submitovanu

    }
    else {
      // else: input je dovoljno dugacak
      // pozivamo funkciju i saljemo request
      // postData()

      // window.alert("Uspesno registrovan korisnik")
      // window.location = "index.html";
      let user = {
          UserName: document.getElementById("inputName").value,
          UserLastName: document.getElementById("inputLanme").value,
          UserEmail: document.getElementById("inputEmail").value,
          UserNumber: document.getElementById("phonNumber").value,
          UserPassword: document.getElementById("inputPassword").value,
          UserRePassword: document.getElementById("inputRePassword").value

      }
      // pokusaj slanja post requesta. py(try: except:)
      try {
          const response = await axios.post("http://0.0.0.0:8081/register-user", user)
          console.log(user)
          if (response.status == '200'){
            let header = document.querySelector("h6");
            header.innerText = `Account created !`;
            
            // window.alert(response.status);
            // "You have successfully created an account and now we will send you an email verification!"

            window.location.href = 'index.html';
          }
          



      } catch (error) {
          if (error.response) {
              let header = document.querySelector("h6");
              console.log(error.message);
              header.innerText = error.response;
              
          } else {
              console.log(error.message);
              header.innerText = error.response;
            
          }
      }
    }
   }




// https://developer.okta.com/blog/2021/08/02/fix-common-problems-cors
