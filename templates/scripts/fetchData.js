async function fetchData(){
    // kao parametar saljem access token iz session storage-a
    const params = {
        token: window.sessionStorage.getItem("access_token")
      };
    // gadjamo profil servis
    if (params.token === null){
      window.location = 'index.html';
    }
    else{
      const response = await axios.get("http://0.0.0.0:8085/get-user-profile", {params} );

      // uzimanjevrednosti iz response objekta
      var firstName = response.data.data.query.firstName;
      var phoneNumber = response.data.data.query.phoneNumber;
      var mail = response.data.data.query.mail;
      var lastName = response.data.data.query.lastName;
      var keycloakUserID = response.data.data.query.keycloakUserID;
      var userProfileIMG = response.data.data.query.imageURL;
  
      // upisivanje vrednosti za vlasnika tokena
      document.getElementById("userID").innerText = keycloakUserID;
      document.getElementById("userName").innerText = firstName;
      document.getElementById("userPhone").innerText = phoneNumber;
      document.getElementById("userProf").innerText = lastName;    
      document.getElementById("userEmail").innerText = mail;
      if (userProfileIMG === null){
        document.getElementById("userProfileIMG").src = "https://res.cloudinary.com/dt5xxftc5/image/upload/v1666083277/webApp/photo_q4cq9t.png";
  
      }
      else{
        document.getElementById("userProfileIMG").src = userProfileIMG;
  
      }

    }






    // window.location = 'userProfile.html';
}