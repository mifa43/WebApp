async function uploadFile() {
    // polje koje uzima key: value i omogucava laksi rad multipart/form-data
    let formData = new FormData(); 

    // dodajemo uploudovani fajl
    formData.append("file", fileupload.files[0]);

    // slanje requesta, formData saljemo enkodovanu sliku = bytes, token saljemo kao header 
 
    await axios.post('http://0.0.0.0:8085/user-profile-image/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'token': window.sessionStorage.getItem("access_token")
      }
    });
    
    window.location = "userProfile.html";
}


    