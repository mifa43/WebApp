
function putSettings1(){
  // document.getElementById('userSettings').innerHTML = '\
  // <div>\
  //   <label for="email">Your Email</label>\
  //   <input type="email" id="email" placeholder="alex@gmail.com">\
  // <div>\
  // ';

  document.querySelector(".nav-link1").classList.add("active");

  document.querySelector(".nav-link2").addEventListener("click",function(){
      document.querySelector(".nav-link1").classList.remove("active");
  });
  return 0;
}
function putSettings2(){
  // document.getElementById('userSettings').innerHTML = '\
  // <div>\
  //   <label for="email">Your Email</label>\
  //   <input type="email" id="email" placeholder="alex@gmail.com">\
  // <div>\
  // ';

  document.querySelector(".nav-link2").classList.add("active");

  document.querySelector(".nav-link1").addEventListener("click",function(){
      document.querySelector(".nav-link2").classList.remove("active");
  });
  return 0;
}