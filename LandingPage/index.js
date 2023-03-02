var btn = 
document.getElementById("contact")


btn.addEventListener('click', email)

function email(){
    window.location.href="mailto:anthonydinunziopr@gmail.com?subject=ProjectPotentialClient&body=%20";
}