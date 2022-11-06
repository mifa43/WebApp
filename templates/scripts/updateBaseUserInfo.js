async function postData() {
  var allinputs = document.querySelectorAll('.form-control');
  var token = window.sessionStorage.getItem("access_token");
  var myLength = allinputs.length;
  var input;
  var dict={"firstStepsComplete": true, "token": token};

  for (var i = 0; i < myLength; ++i) {
    input = allinputs[i];
    if (input.value) {
          dict[input.id] = input.value;

      }
  }
  console.log(dict)
  const resp = await fetch('http://0.0.0.0:8085/update-user-profile', {
      method: 'PUT',
      mode: 'cors',
      headers: {
          'Content-Type': 'application/json'
      },
      body: dict
  });


}