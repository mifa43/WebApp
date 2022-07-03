
async function logout(){
    // uzmi token iz local storage
    let refreshToken = {
        token: window.localStorage.getItem("access_token")
        
    }
    // posalji refresh token na auth a;pi
    try {
        const response = await axios.post("http://0.0.0.0:8083/logout", refreshToken);
    

        // console.log(response.data.access_token.refresh_token);
        // izbrisi token iz local storage
        window.localStorage.removeItem("access_token");
        
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