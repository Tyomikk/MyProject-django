


function myPass() {
    var x = document.getElementById("form-pass");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function myPass_reg() {
    var x = document.getElementById("password_1");
    var y = document.getElementById("password_2");
    if (x.type === "password") {
        x.type = "text";
        y.type = "text";
    } else {
        x.type = "password";
        y.type = "password";
    }
}

function myPass_res() {
    var x = document.getElementById("password_profile_res_old");
    var y = document.getElementById("password_profile_res_1");
    var z = document.getElementById("password_profile_res_2");
    if (x.type === "password") {
        x.type = "text";
        y.type = "text";
        z.type = "text";
    } else {
        x.type = "password";
        y.type = "password";
        z.type = "password";
    }
}

//
//function showPass(id, pass-icon) {
//    if ($(id).attr('type') == 'text') {
//        $(id).attr('type', 'password');
//        $(pass-icon).attr('class', 'fas fa-eye');
//    } else {
//        $(id).attr('type', 'text');
//        $(pass-icon).attr('class', 'fas fa-eye-slash');
//    }
//}