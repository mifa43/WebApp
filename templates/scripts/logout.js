
async function logout(){
    // uzmi token iz local storage
    let refreshToken = {
        token: window.localStorage.getItem("refresh_token")
        
    }
    // posalji refresh token na auth a;pi
    try {
        const response = await axios.post("http://185.26.117.192:8083/logout", refreshToken);
    

        // console.log(response.data.access_token.refresh_token);
        // izbrisi token iz local storage
        window.localStorage.clear();
        
        console.log("You just logged out");
        
        return window.location.href="index.html";

    } catch (error) {
        if (error.response) {
            
            console.log(error.message);
            
            
        } else {
            console.log(error.message);
           
          
        }
    }
}
