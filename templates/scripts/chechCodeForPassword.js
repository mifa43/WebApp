async function checkCode () {
    // async funkcija za slanje requesta na api endpoint sa json body-em
    let user = {
        code: document.getElementById("code").value,
    }
    // pokusaj slanja post requesta. py(try: except:)
    try {
        const response = await axios.post("http://0.0.0.0:8083/password-restart", user);
        console.log(user);
        // let header = document.querySelector("h5");
        // header.innerText = `password!!!!!!!!!!`;
       

        window.alert(response.data.status);

        
        console.log(response.data.status);


        // window.location = 'index.html';



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