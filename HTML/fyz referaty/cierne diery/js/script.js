// Set the number of dots
const numberOfDots = 400;
const background = document.querySelector('.background');

// Function to create a dot element
function createDot() {
    const dot = document.createElement('div');
    dot.classList.add('dot');
    
    // Set random position
    dot.style.left = `${Math.random() * 99}%`;
    dot.style.top = `${Math.random() * 99}%`; 
    
    // Set random animation delay and duration 
    dot.style.animationDuration = `${2.0 + Math.random()*2}s`;
    dot.style.animationDelay = `${Math.random() * 2}s`;

    background.appendChild(dot); 
}

// Create the dots
for (let i = 0; i < numberOfDots; i++) {
    createDot();
}
