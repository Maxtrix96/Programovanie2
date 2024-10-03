function ulozitOtazky() {
    const vlozenePisomky = document.getElementById("zadanePisomky");
    const file = vlozenePisomky.files[0];
    
    if (file) {
        const reader = new FileReader();

        reader.onload = function(event) {
            var textInsideFile = event.target.result;
            document.getElementById()
        };

        reader.readAsText(file)

    } else {
        alert("Zvolte .txt subor")
    }

}


function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }   
}

function selectRandom(numberOfQuestions) {
    const questions = document.getElementById("obsahSuboru").innerText;
    //alert(questions)
    const container = document.getElementById("priestorOtazok")

    const selectedQuestions = questions.slice(0, numberOfQuestions);
    const testElement = document.createElement("div");
    testElement.classList.add("vybranaOtazka")
    container.appendChild(testElement)
}