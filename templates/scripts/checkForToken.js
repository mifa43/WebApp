
function checkForToken(){
    var token = window.localStorage.getItem("access_token");
    console.log(token)
    if(token === null){
        document.getElementById('authreq').innerHTML = '<li><a href="#"><i class="fa bi bi-box-arrow-in-right fa-2x"></i><span class="nav-text">Login</span></a></li></ul>';

        console.log("Token not found")
    }
    else {
        console.log("Token founded")

        document.getElementById('authreq').innerHTML = '<li><a href="#"><i class="fa bi bi-power fa-2x"></i><span class="nav-text">Logout</span></a></li></ul>';

    }
}