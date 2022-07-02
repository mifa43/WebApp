
function logout(){
    window.localStorage.removeItem("access_token");
    console.log("You just logged out");
    window.location="index.html";
}