let curser_outer = document.querySelector(".curser-outer");
let curser_inner = document.querySelector(".curser-inner");

document.querySelector('body').addEventListener('mousemove', (e) => {
    document.querySelector('body').style.cursor = 'none';
});

document.addEventListener("mousemove", (e) => {
    curser_inner.style.cssText = curser_outer.style.cssText = "left:" + e.clientX + "px; top:" + e.clientY + "px;";
});


VanillaTilt.init(document.querySelectorAll(".project-container"), {
    max: 15,
    speed: 400
});

window.addEventListener('scroll', () => {
    let reveals = document.querySelectorAll('.reveal');
    
    for (let i = 0; i < reveals.length; i++) {
        let windowHeight = window.innerHeight;
        let revealLeft = reveals[i].getBoundingClientRect().top;
        let revealPoint = 150;

        if (revealLeft < windowHeight - revealPoint) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }

    }

});



