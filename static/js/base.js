let curser_outer = document.querySelector(".curser-outer");
let curser_inner = document.querySelector(".curser-inner");

document.querySelector('body').addEventListener('mousemove', (e) => {
    document.querySelector('body').style.cursor = 'none !important';
});

document.addEventListener("mousemove", (e) => {
    curser_inner.style.cssText = curser_outer.style.cssText = "left:" + e.clientX + "px; top:" + e.clientY + "px;";
});