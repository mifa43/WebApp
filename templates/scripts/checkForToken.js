function checkForToken(){
    var token = window.localStorage.getItem("access_token");
    console.log(token)
    // da li token postoji local storage ? d
    if(token === null){
        // ne ! prikazi login 
        document.getElementById('authreq').innerHTML = '<li><a href="#"><i class="fa bi bi-box-arrow-in-right fa-2x"></i><span class="nav-text">Login</span></a></li></ul>';

        console.log("Token not found")
    }
    else {
        // ne ! prikazi logout sa scriptom za logout
        console.log("Token founded")

        document.getElementById('authreq').innerHTML = '<li><a href="#" onclick="logout();"><i class="fa bi bi-power fa-2x"></i><span class="nav-text">Logout</span></a></li></ul>';

    }
}