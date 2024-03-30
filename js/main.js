async function preloader(){
    document.getElementById("year").innerHTML = "&copy; " + new Date().getFullYear()
    await new Promise(resolve => setTimeout(resolve, 500));
    var preloader = document.getElementById('preloader');
    preloader.style.top = "-100%";
    await new Promise(resolve => setTimeout(resolve, 1000));
    preloader.style.display = "none";
}



var path = window.location.pathname;
var page = path.split("/").pop();
document.addEventListener('DOMContentLoaded', e => scrollByHash());

async function scrollByHash() {
    await new Promise(resolve => setTimeout(resolve, 500));
    let hash = window.location.hash.slice(1);
    document.querySelector(`.${hash}`).scrollIntoView();
}




var l = 0
async function language() {
    var menu = document.querySelector('.lang');
    var icon = document.getElementById('lang-arrow');
    if(window.scrollY == 0){
        menu.style.top = "70px";
    }
    else{
        menu.style.top = "50px";
    }
    if(l % 2 == 0){
        menu.style.display = "block";
        icon.innerHTML= "&#9650;"
        await new Promise(resolve => setTimeout(resolve, 5));
        menu.style.opacity = "1";
    }
    else{
        menu.style.opacity = "0";
        icon.innerHTML= "&#9660;"
        await new Promise(resolve => setTimeout(resolve, 100));
        menu.style.display = "none";
    }
    l++;
}

function navbar(){
    var nav = document.getElementById('navbar');
    if(window.scrollY > 0){
        nav.style.background = "var(--primary)";
        nav.style.boxShadow = "box-shadow: 0px 0px 4px var(--secondary);";
        nav.style.height = "60px";
    }
    else{
        nav.style.background = "none";
        nav.style.boxShadow = "none";
        if(window.innerWidth > 992){
            nav.style.height = "100px";
        }
    }
}

var n = 0;
async function mobileMenu(){
    const menu = document.getElementById('sideMenu');
    const navbar = document.getElementById('navbar')
    if(n%2==0){
        menu.style.top = "60px";
        if(window.scrollY == 0){  navbar.style.backgroundColor = "var(--primary)";}
        menu.style.display = "flex";
        await new Promise(resolve => setTimeout(resolve, 10));
        menu.style.opacity = "1";
        menu.style.transform = "translateY(0)"
    }
    else{
        navbar.style.backgroundColor = "var(--primary)";

        menu.style.opacity = "0";   
        menu.style.transform = "translateY(-200px)"
        await new Promise(resolve => setTimeout(resolve, 100));
        menu.style.display= "none";
    }
    n++;
}
async function closeMenu(){
    const menu = document.getElementById('sideMenu');
    menu.style.opacity = "0";   
    menu.style.transform = "translateY(-200px)"
    await new Promise(resolve => setTimeout(resolve, 100));
    menu.style.display= "none";
    n++; 
}