// Set the number of dots
const numberOfDots = 100;
const background = document.querySelector('.background');

// Function to create a dot element
function createDot() {
    const dot = document.createElement('div');
    dot.classList.add('dot');
    
    // Set random position
    dot.style.left = `${Math.random() * 92}%`;
    dot.style.top = `${Math.random() * 92}%`; 
    
    // Set random animation delay and duration 
    dot.style.animationDuration = `${5.0 + Math.random()*10.0}s`;
    dot.style.animationDelay = `${Math.random() * 2}s`;

    background.appendChild(dot); 
}

// Create the dots
for (let i = 0; i < numberOfDots; i++) {
    createDot();
}

/*function changeText(num){
    const referat_texty = [
        '1. Čo je to čierna diera?\nČierne diery môžeme definovať ako vysoko koncentrované hmoty s nadmerne veľkou hustotou. Najtypickejšia vlastnosť čiernych dier – nepredstaviteľne silná gravitácia – je práve výsledkom ich nadmernej hustoty.\nVýsledkom tejto gravitácie je tzv. ,,horizont udalostí, ” teda určitý priestor, resp. hranica v určitej vzdialenosti od stredu čiernej diery. Po prekročení tejto hranice je nemožné utiecť pred gravitáciou čiernej diery, dokonca aj pre svetlo, čo je – aspoň podľa dnešných znalostí – najrýchlejšia vec vo vesmíre.\n\nJe len jedna čierna diera?\n\nPoznáme viacero typov čiernych dier, ktoré delíme podľa ich veľkosti:\n\nHviezdne čierne diery\nHviezdne čierne diery vznikajú z kolabujúcich hviezd, môžu mať hmotnosť aj 20-krát väčšiu ako naše slnko, t. j. 3.9782 × 10^31 kg. Je dôležité ale si uvedomiť, že táto hmotnosť – keďže sa jedná o čiernu dieru – je doslova vtlačená do extrémne malého priestoru.\nČierna diera s rovnakou hustotou ako slnko by mala polomer iba 6km – teda niečo také ako menšie mesto – oproti slnku, ktoré má priemer cca. 1 400 000 km (zem má približne 6 374 km polomer). O týchto porovnávaniach viac v ďalšej kapitole.Supermasívne čierne dieryUž z názvu vyplýva, že tieto čierne diery sú doslova obrovské. Ich hmotnosť sa často pohybuje medzi 106 až 109 krát viac ako slnko. Typicky sa nachádzajú v centre galaxií, aj v centre mliečnej dráhy. Sagittarius A*, teda supermasívna čierna diera v centre našej galaxie, má hmotnosť cca. 4 mil. slnečných hmôt (4 mil. sĺnk) s priemerom okolo 12 mil. km, teda o niečo viac ako 31-krát vzdialenosti medzi zemou a mesiacom, alebo 12-krát menej ako vzdialenosť medzi zemou a slnkom.Čierne diery so strednou hmotnosťouV porovnaní s inými sú relatívne malé, s hmotnosťou medzi sto až tisíc slnečných hmôt. Taktiež sú vzácnejšie a je ich ťažšie nájsť. Najväčšie z nich by mali priemer približne 3000 km – Slovensko by sa do takejto čiernej diery zmestilo asi sedemkrát. Najčastejšie sa nachádzajú v hustých hviezdokopách alebo v trpasličích galaxiách.Prvotné čierne dieryHypotetické čierne diery, ktoré mohli vzniknúť po veľkom tresku. Najmenšie zo všetkých, niektoré s hmotnosťou porovnateľnou so zrnkom piesku, iné porovnateľné s asteroidmi. Prvotná čierna diera s hmotnosťou Mount Everestu (~1015 kg) by mala priemer okolo 10-12 m. Pre porovnanie, protón má veľkosť približne 10-15 m.',
        "asdbasdasdb asdasdb asdbasdas dbasdasdb as dbasdasdbasdasdb asdbasdasdbasd asdb as dbasdasdbasdasdb a sdbasdasdbasdas db asdbas dasd basdasdb asdbasdas dbasdasdb a sdbasdasd basdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb asdbasdasdbasdasdb 69420",
        "niausbdasudb"
    ]
    const element = document.getElementById("referatText")
    element.innerText = referat_texty[num-1]
    element.style.display = "none";
    element.offsetHeight; // Trigger a reflow
    element.style.display = 'flex';
}
*/

// Function to add a span 
function addSpan(text, parent) {
    const span = document.createElement("span");
    span.textContent = text;
    parent.appendChild(span);
}

// Function to add a strong element for bold text
function addStrong(text, parent) {
    const strong = document.createElement("strong");
    strong.textContent = text;
    parent.appendChild(strong);
}

// Function to add a sup element for superscript
function addSup(exponent, parent) {
    const sup = document.createElement("sup");
    sup.textContent = exponent;
    parent.appendChild(sup);
}

// Function to add a line break
function addLineBreak(parent) {
    const br = document.createElement("br");
    parent.appendChild(br);
}

const referatTextContainer = document.getElementById("referatTextContainer");

function changeText1() {
    referatTextContainer.removeChild(document.getElementById("referatText"));
    const referatText = document.createElement("p");
    referatText.id = "referatText";
    referatTextContainer.append(referatText);

    addStrong('1. Čo je to čierna diera?', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan(
        'Čierne diery môžeme definovať ako vysoko koncentrované hmoty s nadmerne veľkou hustotou. Najtypickejšia vlastnosť čiernych dier – nepredstaviteľne silná gravitácia – je práve výsledkom ich nadmernej hustoty.',
        referatText
    );
    addLineBreak(referatText);
    
    addSpan(
        'Výsledkom tejto gravitácie je tzv. ,,horizont udalostí, ” teda určitý priestor, resp. hranica v určitej vzdialenosti od stredu čiernej diery. Po prekročení tejto hranice je nemožné utiecť pred gravitáciou čiernej diery, dokonca aj pre svetlo, čo je – aspoň podľa dnešných znalostí – najrýchlejšia vec vo vesmíre.',
        referatText
    );
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addStrong('Je len jedna čierna diera?', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan(
        'Poznáme viacero typov čiernych dier, ktoré delíme podľa ich veľkosti:',
        referatText
    );
    addLineBreak(referatText);
    
    addStrong('Hviezdne čierne diery', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan(
        'Hviezdne čierne diery vznikajú z rútiacich sa hviezd, môžu mať hmotnosť aj 20–krát väčšiu ako naše slnko, t. j. 3.9782 × 10',
        referatText
    );
    addSup('31', referatText);
    addSpan(' kg. Je dôležité ale si uvedomiť, že táto hmotnosť – keďže sa jedná o čiernu dieru – je doslova vtlačená do extrémne malého priestoru. Čierna diera s rovnakou hustotou ako slnko by mala polomer iba 6km – teda niečo také ako menšie mesto – oproti slnku, ktoré má priemer cca. 1 400 000 km (zem má približne 6 374 km polomer). O týchto porovnávaniach viac v ďalšej kapitole.',
        referatText
    );
    addLineBreak(referatText);
    
    addStrong('Supermasívne čierne diery', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan(
        'Už z názvu vyplýva, že tieto čierne diery sú doslova obrovské. Ich hmotnosť sa často pohybuje medzi 10',
        referatText
    );
    addSup('6', referatText);
    addSpan(' až 10', referatText);
    addSup('9', referatText);
    addSpan(' krát viac ako slnko. Typicky sa nachádzajú v centre galaxií, aj v centre mliečnej dráhy. Sagittarius A*, teda supermasívna čierna diera v centre našej galaxie, má hmotnosť cca. 4 mil. slnečných hmôt (4 mil. sĺnk) s priemerom okolo 12 mil. km, teda o niečo viac ako 31–krát vzdialenosti medzi zemou a mesiacom, alebo 12–krát menej ako vzdialenosť medzi zemou a slnkom.',
        referatText
    );
    addLineBreak(referatText);
    
    addStrong('Čierne diery so strednou hmotnosťou', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan(
        'V porovnaní s inými sú relatívne malé, s hmotnosťou medzi sto až tisíc slnečných hmôt. Taktiež sú vzácnejšie a je ich ťažšie nájsť. Najväčšie z nich by mali priemer približne 3000 km – Slovensko by sa do takejto čiernej diery zmestilo asi sedemkrát. Najčastejšie sa nachádzajú v hustých hviezdokopách alebo v trpasličích galaxiách.',
        referatText
    );
    addLineBreak(referatText);
    
    addStrong('Prvotné čierne diery', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan(
        'Hypotetické čierne diery, ktoré mohli vzniknúť po veľkom tresku. Najmenšie zo všetkých, niektoré s hmotnosťou porovnateľnou so zrnkom piesku, iné porovnateľné s asteroidmi. Prvotná čierna diera s hmotnosťou Mount Everestu (~10',
        referatText
    );
    addSup('15', referatText);
    addSpan(' kg) by mala priemer okolo 10', referatText);
    addSup('–12', referatText);
    addSpan(' m. Pre porovnanie, protón má veľkosť približne 10', referatText);
    addSup('–15', referatText);
    addSpan(' m.',
        referatText
    );
    addLineBreak(referatText);
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

function showPopUpCalculator() {
    const mainContentContainer = document.getElementById("mainContentContainer"); // main parent

    // add background
    const massCalculatorBackCover = document.createElement("div"); 
    massCalculatorBackCover.id = "massCalculatorBackCover";
    mainContentContainer.appendChild(massCalculatorBackCover); // holder of subsequent children, to close popup delete this and its children
    
    // add pop-up container box
    const massCalculatorContainer = document.createElement("div"); // container of the calculator
    massCalculatorContainer.id = "massCalculatorContainer"; 
    massCalculatorBackCover.appendChild(massCalculatorContainer);

    // add close button
    const massCalculatorCloseButton = document.createElement("button");
    massCalculatorCloseButton.id = "massCalculatorCloseButton";
    massCalculatorCloseButton.onclick = closeMassCalculator; // close on clicking outside the box
    massCalculatorContainer.appendChild(massCalculatorCloseButton);

    // add text container for used constants
    const massCalculatorUsedValues = document.createElement("p");
    massCalculatorUsedValues.id = "massCalculatorUsedValues";
    massCalculatorContainer.appendChild(massCalculatorUsedValues);

    // add text for used constants
    addSpan('Použité hodnoty:', massCalculatorUsedValues);
    addLineBreak(massCalculatorUsedValues);

    addSpan('G = 6,674 × 10', massCalculatorUsedValues);
    addSup('-12', massCalculatorUsedValues);
    addSpan(' m', massCalculatorUsedValues);
    addSup('3', massCalculatorUsedValues);
    addSpan('kg', massCalculatorUsedValues);
    addSup('-1', massCalculatorUsedValues);
    addSpan('s', massCalculatorUsedValues);
    addSup('-1', massCalculatorUsedValues);
    addLineBreak(massCalculatorUsedValues);

    addSpan('c = 3 × 10', massCalculatorUsedValues);
    addSup('8', massCalculatorUsedValues);
    addSpan(' ms', massCalculatorUsedValues);
    addSup('-1', massCalculatorUsedValues);
    addLineBreak(massCalculatorUsedValues);

    // add input box
    const massCalculatorUserInput = document.createElement("input");
    massCalculatorUserInput.id = "massCalculatorUserInput";
    massCalculatorContainer.appendChild(massCalculatorUserInput);

}

function closeMassCalculator() { // close calculator on click outside the box
    const massCalculatorBackCover = document.getElementById("massCalculatorBackCover");
    const mainContentContainer = document.getElementById("mainContentContainer");
    mainContentContainer.removeChild(massCalculatorBackCover);
}
