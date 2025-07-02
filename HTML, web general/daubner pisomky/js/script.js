function ulozitOtazky() {
    if (document.getElementById("priestorVsetkychOtazok").contains(document.getElementById("textCelySubor"))) { 
        document.getElementById("textCelySubor").remove(); // vymazat stary text pri pridani novej pisomky
    } 
    const vlozenePisomky = document.getElementById("zadanePisomky"); // <input> id
    const file = vlozenePisomky.files[0];
    const questionsCounter = document.getElementById("pocetOtazokID");
    
    if (file) {
        const reader = new FileReader(); // nacit FileReader
        reader.onload = function(event) {
            const textVSubore = event.target.result; 
            const textContainer = document.getElementById("priestorVsetkychOtazok");
            const extrahovanyText = document.createElement("pre");
            extrahovanyText.classList.add("textVOtazkovychRamcoch");
            extrahovanyText.id = "textCelySubor";
            extrahovanyText.textContent = textVSubore; // ulozit do prvku text
            textContainer.appendChild(extrahovanyText); // vlozit spracovany text do stranky
            questionsCounter.innerText = textVSubore.split("\n").length // vypist pocet otazok
        };

        reader.readAsText(file);

    } else {
        alert("Zvolte .txt subor");
    }   
}

function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }   
    return arr;
}

function selectRandom() {
    const container = document.getElementById("priestorVybranychOtazok"); // priestor pre vlozenie otazok
    if (container.contains(document.getElementById("textJednotliveOtazky"))) { // v pripade opakovanej generacie otazok treba zmazat predosle
        document.getElementById("textJednotliveOtazky").remove();
    }
    var numberOfQuestions = +document.getElementById("zadaniePoctuOtazok").value; // pocet otazok extrahovany z <input> elementu
    const questions = document.getElementById("textCelySubor").innerText; // ulozenie textu na spracovanie 
    const questionsArray = questions.split("\n"); // premena textu na zoznam
    // cast na generovanie nahodneho poradia
    var shuffledArray = shuffleArray(questionsArray) // nahodne zoradeny zoznam otazok
    var selectedQuestions = shuffledArray.slice(0, numberOfQuestions); 
    for (let i = 0; i < selectedQuestions.length ; i++) {
        var question = selectedQuestions[i].split("."); // zmenit na list
        question.splice(0, 1); // 0. index ma stare cislo otazky, to zmazat
        question = question.join("."); // spojit zvysok (ak sa rozdelilo aj inde ako po starom cisle otazky)
        selectedQuestions[i] = (i+1).toString() + "." + question; // vymenit staru otazku so zlym cislom za novu
    }
    var formatedQuestions = selectedQuestions.join("\n") // spojit zoznam do stringu

    // pridanie otazok do priestoru pre vygenerovanu pisomku
    const testElement = document.createElement("pre"); // vytvoreny novy prvok
    testElement.classList.add("textVOtazkovychRamcoch"); // pridanie potrebnych tried
    testElement.id = "textJednotliveOtazky";
    testElement.innerText = formatedQuestions; // vlozenie textu s otazkami
    container.appendChild(testElement); // nasledne pridanie do ramca
}

function downloadFile(regenerate) {
    const container = document.getElementById("priestorVybranychOtazok"); 
    const pisomkaNaStiahnutie = document.getElementById("textJednotliveOtazky"); // priestor drziaci text vygen. pisomiek
    if (container.contains(pisomkaNaStiahnutie)) { // ak je vygenerovana pisomka
        const textNaStiahnutie = pisomkaNaStiahnutie.innerText; // vygen. pisomka vo forme str
        const blob = new Blob([textNaStiahnutie], {type: "text/plain"}); // subor 
        
        // pripojit link a stiahnut subor
        const linkNaStiahnutie = document.createElement("a"); 
        linkNaStiahnutie.href = URL.createObjectURL(blob); 
        linkNaStiahnutie.download = "Písomka"; 
        document.body.appendChild(linkNaStiahnutie);
        linkNaStiahnutie.click();
        document.body.removeChild(linkNaStiahnutie);
    } else {
        alert("Nie je čo stiahnuť!")
    }
    if (regenerate === true){
        selectRandom()
    }
}