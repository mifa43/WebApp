async function fetchData(){
    // kao parametar saljem access token iz session storage-a
    const params = {
        token: window.sessionStorage.getItem("access_token")
      };
    // gadjamo profil servis
    const response = await axios.get("http://0.0.0.0:8085/get-user-profile", {params} );

    // uzimanjevrednosti iz response objekta
    var firstName = response.data.data.firstName;
    var phoneNumber = response.data.data.phoneNumber;
    var mail = response.data.data.mail;
    var lastName = response.data.data.lastName;
    var keycloakUserID = response.data.data.keycloakUserID;
    var userProfileIMG = response.data.data.imageURL;

    // upisivanje vrednosti za vlasnika tokena
    document.getElementById("userID").innerText = keycloakUserID;
    document.getElementById("userName").innerText = firstName;
    document.getElementById("userPhone").innerText = phoneNumber;
    document.getElementById("userProf").innerText = lastName;    
    document.getElementById("userEmail").innerText = mail;
    document.getElementById("userProfileIMG").src = userProfileIMG;



    // window.location = 'userProfile.html';
}