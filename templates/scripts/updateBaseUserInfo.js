async function postData() {
  var allinputs = document.querySelectorAll('.form-control');
  var tagList = document.querySelectorAll("#tagValue1");

  var token = window.sessionStorage.getItem("access_token");
  var myLength = allinputs.length;
  var input;
  var dict={"firstStepsComplete": true, "token": token};
  var ls = [];
  for (var i = 0; i < myLength; ++i) {
    input = allinputs[i];
    if (input.value) {
      
        dict[input.id] = input.value;


      }
  }
  const  myNumbersArray = [ 1,2,3,4,5];

  for(let i = 0; i < tagList.length; i++) {
    ls.push(tagList[i].textContent);
  }
  console.log(ls);

  let usr = {
    // dict[input.id] = input.value;
    UserFirstName: dict["UserFirstName"],
    UserLastName: dict["UserLastName"],
    UserNumber: dict["UserNumber"],
    token: token,

    title: dict["title"],
    description: dict["description"],
    about: dict["about"],
    tagInput: ls,
    links: dict["links"],
    firstStepsComplete: dict["firstStepsComplete"]
  };

  console.log(usr);
  const resp = await fetch('http://0.0.0.0:8085/update-user-profile', {
      method: 'PUT',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(usr)
  });
  // window.alert(tagList[0].textContent);

  window.location = "userProfile.html";

}