
function putElem(){
    document.getElementById('pop123').innerHTML = '\
    <div class="subscribe-form">\
        <div class="left">\
            <img src="restart-password-img.jpg" alt="Forgot your password ilustration image " width="100%">\
        </div>\
        <div class="right">\
            <h2>let us help you!</h2>\
            <p>If you have forgotten your account password, you need to provide us with the email address you used during registration.</p>\
            <div class="formm">\
                <div id="lab1" class="inputt">\
                    <label for="email">Your Email</label>\
                    <input type="email" id="email" placeholder="alex@gmail.com">\
                </div>\
                <div id="lab2" class="button">\
                    <button id="restartPassword" onclick="restartPassword();" >Restart Password</button>\
                </div>\
            </div>\
        </div>\
        <button  class="close-btn">\
            &times;\
        </button>\
    </div>\
    ';

    document.querySelector(".subscribe-form").classList.add("active");

    document.querySelector(".subscribe-form .close-btn").addEventListener("click",function(){
        document.querySelector(".subscribe-form").classList.remove("active");
    });
    return 0;
}
