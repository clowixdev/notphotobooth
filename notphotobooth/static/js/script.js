var button = document.getElementsByID("change-background");
var background_div = document.getElementById("BG")
var bg = 'bg1';

button.addEventListener("click", function(){
    if (bg == 'bg1') {
        bg = 'bg2'
        background_div.style.backgroundImage = "url(../img/header_2bg.jpg)";
    }
    else if (bg == 'bg2') {
        bg = 'bg3'
        background_div.style.backgroundImage = "url(../img/header_3bg.jpg)";
    }
    else if (bg == 'bg3') {
        bg = 'bg1'
        background_div.style.backgroundImage = "url(../img/header_1bg.jpg)";
    }
});