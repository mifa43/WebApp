
function editProfile(){

  document.getElementById("saveBtn").classList.remove("hide");
  document.getElementById("editBtn").classList.add("hide");

  // dohvati tag
  let userID = document.getElementById("userID");
  let userName = document.getElementById("userName");
  let userEmail = document.getElementById("userEmail");
  let userPhone = document.getElementById("userPhone");
  let userProf = document.getElementById("userProf");
  // dodat css style
  userID.classList.add("hide");
  userName.classList.add("hide");
  userEmail.classList.add("hide");
  userPhone.classList.add("hide");
  userProf.classList.add("hide");

  // dohvati tag izbrisi klasu hide
  
  // dohvati tag
  let userIDInput = document.getElementById("userIDInput");
  let userNameInput = document.getElementById("userNameInput");
  let userEmailInput = document.getElementById("userEmailInput");
  let userPhoneInput = document.getElementById("userPhoneInput");
  let userProfInput = document.getElementById("userProfInput");
  // izbrisi klasu hide
  userIDInput.classList.remove("hide");
  userNameInput.classList.remove("hide");
  userEmailInput.classList.remove("hide");
  userPhoneInput.classList.remove("hide");
  userProfInput.classList.remove("hide");

    // dodaj vrednost iz p taga
  userIDInput.value = userID.innerText;
  userNameInput.value = userName.innerText;
  userEmailInput.value = userEmail.innerText;
  userPhoneInput.value = userPhone.innerText;
  userProfInput.value = userProf.innerText;

  

}


async function save(){

  document.getElementById("userID").classList.remove("hide");
  document.getElementById("userName").classList.remove("hide");
  document.getElementById("userEmail").classList.remove("hide");
  document.getElementById("userPhone").classList.remove("hide");
  document.getElementById("userProf").classList.remove("hide");


  document.getElementById("userIDInput").classList.add("hide");
  document.getElementById("userNameInput").classList.add("hide");
  document.getElementById("userEmailInput").classList.add("hide");
  document.getElementById("userPhoneInput").classList.add("hide");
  document.getElementById("userProfInput").classList.add("hide");


  document.getElementById("saveBtn").classList.add("hide");
  

  let user = {
    UserFirstName: document.getElementById("userNameInput").value,
    UserLastName: document.getElementById("userProfInput").value,
    UserEmail: document.getElementById("userEmailInput").value,
    UserNumber: document.getElementById("userPhoneInput").value,
    keycloakUserID: document.getElementById("userIDInput").value
    }
    const response = await axios.put("http://0.0.0.0:8085/update-user-profile", user);
    console.log(user);
  

    
    console.log(response.data);

    document.getElementById("editBtn").classList.remove("hide");
    window.location = 'userProfile.html';
 

}
// pokusaj slanja post requesta. py(try: except:)

