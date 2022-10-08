async function fetchData(){

    console.log("1111111111111111111111111");
    const params = {
        token: window.sessionStorage.getItem("access_token")
      };
    
    const response = await axios.get("http://0.0.0.0:8085/get-user-profile", {params} );
    console.log("2222222222222222222222222");
   


    // window.location = 'userProfile.html';
}