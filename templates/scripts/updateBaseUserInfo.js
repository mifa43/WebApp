function postData() {
    var allinputs = document.querySelectorAll('.form-control');
    var myLength = allinputs.length;
    var input;
  
    for (var i = 0; i < myLength; ++i) {
      input = allinputs[i];
      if (input.value) {
        window.alert(input.value);
        }
    }
  }
  