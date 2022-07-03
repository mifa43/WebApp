
async function postData () {
    // async funkcija za slanje requesta na api endpoint sa json body-em
    let user = {
        UserEmail: document.getElementById("inputEmaill").value,
        UserPassword: document.getElementById("inputPasswordd").value
    }
    // pokusaj slanja post requesta. py(try: except:)
    try {
        const response = await axios.post("http://0.0.0.0:8083/login", user);
        console.log(user);
        let header = document.querySelector("h5");
        header.innerText = `Nice to see you are back`;
       

        window.alert(response.data.refresh_token);

        
        console.log(response.data.refresh_token	);

        window.localStorage.setItem('access_token', response.data.refresh_token);

        

        window.location.href = 'index.html';



    } catch (error) {
        if (error.response) {
            let header = document.querySelector("h6");
            console.log(error.message);
            header.innerText = error.response.data;
            
        } else {
            console.log(error.message);
            header.innerText = error.response.data;
          
        }
    }
}

// function validate() {
//     // provera da li je input veci od 3
//     let header = document.querySelector("h6");

//     var UserEmail = document.getElementById("inputEmaill").value;
    
//     var UserPassword = document.getElementById("inputPasswordd").value;


//     if (UserEmail.length < 5) {
//         header.innerText = `Email must be longer than 1 characters`;
//       return false; // drzimo formu submitovanu

//     }

//     else if (UserPassword.length < 6) {
//         header.innerText = `Password must be longer than 1 characters`;
//       return false; // drzimo formu submitovanu

//     }

//     else {
//       // else: input je dovoljno dugacak
//       // pozivamo funkciju i saljemo request
//       postData()

//       // window.alert("Uspesno registrovan korisnik")
//       // window.location = "index.html";
//       return true;
//     }
//    }
