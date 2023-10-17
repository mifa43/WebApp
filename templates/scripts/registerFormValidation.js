// function validate() {
//     // provera da li je input veci od 3
//     let header = document.querySelector("h6");
        
//     var UserName = document.getElementById("inputName").value;
//     var UserLastName = document.getElementById("inputLanme").value;
//     var UserEmail = document.getElementById("inputEmail").value;
//     var UserNumber = document.getElementById("phonNumber").value;
//     var UserPassword = document.getElementById("inputPassword").value;
//     var UserRepassword = document.getElementById("inputRePassword").value


//     if (UserName.length < 4) {
//         header.innerText = `User name must be longer than 4 characters`;
//       return false; // drzimo formu submitovanu

//     }
//     else if (UserLastName.length < 4) {
//         header.innerText = `Last name must be longer than 4 characters`;
//       return false; // drzimo formu submitovanu

//     }
//     else if (UserEmail.length < 5) {
//         header.innerText = `Email must be longer than 5 characters`;
//       return false; // drzimo formu submitovanu

//     }
//     else if (UserNumber.length < 9) {
//         header.innerText = `Phone Number must be longer than 9 numbers`;
//       return false; // drzimo formu submitovanu

//     }
//     else if (UserPassword.length < 6) {
//         header.innerText = `Password must be longer than 5 characters`;
//       return false; // drzimo formu submitovanu

//     }
//     else if (UserRepassword.length < 6) {
//         header.innerText = `Repeat Password must be longer than 5 characters`;
//       return false; // drzimo formu submitovanu

//     }
//     else {
//       // else: input je dovoljno dugacak
//       // pozivamo funkciju i saljemo request
//       // postData()

//       // window.alert("Uspesno registrovan korisnik")
//       // window.location = "index.html";
//       header.innerText = `greskaaaaaa`;
//       return false;
      
//     }
//    }