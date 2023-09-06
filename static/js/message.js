function hideMessageBox() {
    document.getElementById('message-box').style.display = 'none';
}

try {
    const messagebox = document.getElementById('message-box');
    setTimeout("hideMessageBox()", 1000);
} catch (e) {
    console.log(e);
}


