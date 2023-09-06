let pState = 'hide';
let rePState = 'hide';

const showPassword = (e) => {
    if (pState == 'hide') {
        document.getElementById('password').type = 'text';
        document.getElementById('password-icon').classList = 'fa-solid fa-eye password-icon';
        pState = 'show';
    } else {
        document.getElementById('password').type = 'password';
        document.getElementById('password-icon').classList = 'fa-solid fa-eye-slash password-icon';
        pState = 'hide';
    }
}

const showreenterPassword = (e) => {
    if (rePState == 'hide') {
        document.getElementById('reenterpassword').type = 'text';
        document.getElementById('repassword-icon').classList = 'fa-solid fa-eye password-icon';
        rePState = 'show';
    } else {
        document.getElementById('reenterpassword').type = 'password';
        document.getElementById('repassword-icon').classList = 'fa-solid fa-eye-slash password-icon';
        rePState = 'hide';
    }
}