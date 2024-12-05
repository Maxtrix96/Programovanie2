// Set the number of dots
const numberOfDots = 200;
const background = document.querySelector('.background');

// Function to create a dot element
function createDot() {
    const dot = document.createElement('div');
    dot.classList.add('dot');
    
    // Set random position
    dot.style.left = `${Math.random() * 99}%`;
    dot.style.top = `${Math.random() * 99}%`; 
    
    // Set random animation delay and duration 
    dot.style.animationDuration = `${5.0 + Math.random()*10.0}s`;
    dot.style.animationDelay = `${Math.random() * 2}s`;

    background.appendChild(dot); 
}

// Create the dots
for (let i = 0; i < numberOfDots; i++) {
    createDot();
}

function changeText(num){
    const referat_texty = [
        "asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb 69420",
        "niausbdasudb"
    ]
    const element = document.getElementById("referatText")
    element.innerText = referat_texty[num-1]
    element.style.display = "none";
    element.offsetHeight; // Trigger a reflow
    element.style.display = 'flex';
}

function selectRandom(array) {
    const randIndex = Math.floor(Math.random() * array.length);
    return array[randIndex];
}

function generateRandomColor() {
    const hue = Math.floor(Math.random() * 360);  // Random hue value from 0 to 360
    const saturation = 110; // You can adjust saturation (70% for a vibrant color)
    const lightness = 70; // You can adjust lightness (60% for a balanced color)
    return `hsl(${hue}, ${saturation}%, ${lightness}%)`; 
}

function randomShadowColorsForButtons() { // assign pseudo random colors to button shadows
    const textChangeButtons = document.querySelectorAll(".textChangeButton") // find all buttons
    const buttonShadowColorOptions = ["green", "blue", "cyan", "lightblue", "white", "lightpink"] // limited list for consistency (and ease of testing)
    
    textChangeButtons.forEach(element => {
        const chosenColor = selectRandom(buttonShadowColorOptions) // decide which color
        element.style.setProperty("--random-shadow-color", generateRandomColor()) // assign color to button shadow
    });
}