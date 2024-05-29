function say_hello() {
    alert("Hello world!");
}

function changeCock() {
    var pElement = document.getElementById("cock");
    var imgElement = document.createElement("cockImage");
    imgElement.src = "../../img/rooster.png";
    imgElement.alt = "Image";
    pElement.parentNode.replaceChild(imgElement, pElement);
}

function changeText() {
    var pElement = document.getElementById("cock")
    if (pElement.textContent === "cock") {
        pElement.innerHTML = "SUPER COCK!";
        var red = 230;
        var green = 230;
        var blue = 0;
        var color = 'rgb(' + red + ',' + green + ',' + blue + ')';
        pElement.style.color = color;
    }
    else {
        pElement.innerHTML = "cock"
        var red = 231;
        var green = 111;
        var blue = 117;
        var color = 'rgb(' + red + ',' + green + ',' + blue + ')';
        pElement.style.color = color;
    }
    var linkedButton = document.getElementById("cockChangeColorButton");

    if (linkedButton.textContent === "OH NO! THE COCK IS TOO COOL! CLICK ME TO SAVE YOURSELF!") {
        linkedButton.innerHTML = "Click me to make the cock cool!"
    }
    else {
        linkedButton.innerHTML = "OH NO! THE COCK IS TOO COOL! CLICK ME TO SAVE YOURSELF!";
    }
}