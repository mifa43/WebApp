function onGet() {
    const url = "http://0.0.0.0:8081/";
    var headers = {}
    
    fetch(url, {
        method : "GET",
        mode: 'cors',
        headers: headers
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(response.error)
        }
        return response.json();
        
    })
    .then(data => {
        
        document.getElementById('messages').value = data["Health"];
        console.log(data)
    })
    .catch(function(error) {
        document.getElementById('messages').value = error;
    });
}



// https://developer.okta.com/blog/2021/08/02/fix-common-problems-cors