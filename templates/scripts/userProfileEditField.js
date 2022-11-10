
function editProfile(){

  document.getElementById("saveBtn").classList.remove("hide");
  document.getElementById("editBtn").classList.add("hide");

  // dohvati tag
  let userID = document.getElementById("userID");
  let userName = document.getElementById("userName");
  let userEmail = document.getElementById("userEmail");
  let userPhone = document.getElementById("userPhone");
  let userProf = document.getElementById("userProf");
  let userDescription = document.getElementById("userDescription");

  // dodat css style userDescription
  userID.classList.add("hide");
  userName.classList.add("hide");
  userEmail.classList.add("hide");
  userPhone.classList.add("hide");
  userProf.classList.add("hide");
  userDescription.classList.add("hide");
  // dohvati tag izbrisi klasu hide
  
  // dohvati tag
  let userIDInput = document.getElementById("userIDInput");
  let userNameInput = document.getElementById("userNameInput");
  let userEmailInput = document.getElementById("userEmailInput");
  let userPhoneInput = document.getElementById("userPhoneInput");
  let userProfInput = document.getElementById("userProfInput");
  let userDescriptionInput = document.getElementById("userDescriptionInput");

  // izbrisi klasu hide
  userIDInput.classList.remove("hide");
  userNameInput.classList.remove("hide");
  userEmailInput.classList.remove("hide");
  userPhoneInput.classList.remove("hide");
  userProfInput.classList.remove("hide");
  userDescriptionInput.classList.remove("hide");

    // dodaj vrednost iz p taga
  userIDInput.value = userID.innerText;
  userNameInput.value = userName.innerText;
  userEmailInput.value = userEmail.innerText;
  userPhoneInput.value = userPhone.innerText;
  userProfInput.value = userProf.innerText;
  userDescriptionInput.value = userDescription.innerText;

  

}

//  querovanjem baze dobijamo user profile info, upisuje se u <p> tag, iz <p> taga uzimamo informazcije 
//   i ubazcujemo ih u input, smena izmedju <p> i input taga zavisi od edit i save button-a, 
//  save button salje request na nas api te se upisuje
async function save(){

  document.getElementById("userID").classList.remove("hide");
  document.getElementById("userName").classList.remove("hide");
  document.getElementById("userEmail").classList.remove("hide");
  document.getElementById("userPhone").classList.remove("hide");
  document.getElementById("userProf").classList.remove("hide");
  document.getElementById("userDescription").classList.remove("hide");


  document.getElementById("userIDInput").classList.add("hide");
  document.getElementById("userNameInput").classList.add("hide");
  document.getElementById("userEmailInput").classList.add("hide");
  document.getElementById("userPhoneInput").classList.add("hide");
  document.getElementById("userProfInput").classList.add("hide");
  document.getElementById("userDescriptionInput").classList.add("hide");


  document.getElementById("saveBtn").classList.add("hide");
  document.getElementById("editBtn").classList.remove("hide");

  var token = window.sessionStorage.getItem("access_token");

  let user = {
    UserFirstName: document.getElementById("userNameInput").value,
    UserLastName: document.getElementById("userProfInput").value,
    UserEmail: document.getElementById("userEmailInput").value,
    UserNumber: document.getElementById("userPhoneInput").value,
    token: token,
    keycloakUserID: document.getElementById("userIDInput").value,
    description: document.getElementById("userDescriptionInput").value

    }
    const response = await axios.put("http://0.0.0.0:8085/update-user-profile", user);
    console.log(user);
  

    console.log(response.data);

    window.location = 'userProfile.html';
 

}
// pokusaj slanja post requesta. py(try: except:)

