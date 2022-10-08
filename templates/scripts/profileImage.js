async function uploadFile() {
    let formData = new FormData(); 
    formData.append("file", fileupload.files[0]);
    fetch('http://0.0.0.0:8085/user-profile-image', {
      method: "POST", 
      body: formData
    }); 
    alert('The file has been uploaded successfully.');
    }