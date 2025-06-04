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

// Function to add a span 
function addSpan(text, parent, elementClass="") {
    const span = document.createElement("span");
    span.textContent = text;
    if (!elementClass.length === 0){
        span.classList.add(elementClass);
    }
    parent.appendChild(span);
}

// Function to add a strong element for bold text
function addStrong(text, parent, elementClass="") {
    const strong = document.createElement("strong");
    strong.textContent = text;
    strong.classList.add("strongTextTitle")
    if (!elementClass.length === 0){
        strong.classList.add(elementClass);
    }
    parent.appendChild(strong);
}

// Function to add a sup element for superscript
function addSup(exponent, parent, elementClass="") {
    const sup = document.createElement("sup");
    sup.textContent = exponent;
    if (!elementClass.length === 0){
        sup.classList.add(elementClass);
    }
    parent.appendChild(sup);
}

// Function to add a sub element for subscript
function addSub(text, parent) {
    const sub = document.createElement("sub");
    sub.textContent = text;
    parent.appendChild(sub);
}

// Function to add a line break
function addLineBreak(parent) {
    const br = document.createElement("br");
    parent.appendChild(br);
}

const referatTextContainer = document.getElementById("referatTextContainer");

function changeText(num) {
    referatTextContainer.removeChild(document.getElementById("referatText"));
    const referatText = document.createElement("p");
    referatText.id = "referatText";
    referatTextContainer.appendChild(referatText);

    const respectiveFunctions = [changeText0, changeText1, changeText2, changeText3, changeText4]; // list of functions with text
    respectiveFunctions[num](); // call the correct function depending on user selection
}

function changeText0() {
    const referatText = document.getElementById("referatText");

    addStrong('1. Čo je to čierna diera?', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Čierne diery môžeme definovať ako oblasti vysoko koncentrovanej hmoty s nadmerne veľkou hustotou. Najtypickejšia vlastnosť čiernych dier – nepredstaviteľne silná gravitácia – je práve výsledkom ich nadmernej hustoty v porovnaní s ich hmotnosťou. Gravitácia samozrejme stále závisí od samotnej hmotnosti objektu, t. j. čierna diera s hmotnosťou slnka by mala rovnako silnú gravitáciu, ale bola by oveľa menšia.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Výsledkom tejto gravitácie je tzv. ,,horizont udalostí, ” teda určitý priestor, resp. hranica v určitej vzdialenosti od stredu čiernej diery. Po prekročení tejto hranice je nemožné utiecť pred gravitáciou čiernej diery, dokonca aj pre svetlo, čo je – aspoň podľa dnešných znalostí – najrýchlejšia vec vo vesmíre.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addStrong('Je len jedna čierna diera?', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Poznáme viacero typov čiernych dier, ktoré delíme podľa ich veľkosti:', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addStrong('Hviezdne čierne diery', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Hviezdne čierne diery vznikajú z rútiacich sa hviezd, môžu mať hmotnosť aj 20–krát väčšiu ako naše slnko, t. j. 3.9782 × 10', referatText);
    addSup('31', referatText);
    addSpan(' kg. Je dôležité ale si uvedomiť, že táto hmotnosť – keďže sa jedná o čiernu dieru – je doslova vtlačená do extrémne malého priestoru. Čierna diera s rovnakou hustotou ako slnko by mala polomer iba 6km – teda niečo také ako menšie mesto – oproti slnku, ktoré má priemer cca. 1 400 000 km (Zem má približne 6 374 km polomer). O týchto porovnávaniach viac v ďalšej kapitole.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addStrong('Supermasívne čierne diery', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Už z názvu vyplýva, že tieto čierne diery sú doslova obrovské. Ich hmotnosť sa často pohybuje medzi 10', referatText);
    addSup('6', referatText);
    addSpan(' až 10', referatText);
    addSup('9', referatText);
    addSpan(' krát viac ako slnko. Typicky sa nachádzajú v centre galaxií, aj v centre mliečnej dráhy. Sagittarius A*, teda supermasívna čierna diera v centre našej galaxie, má hmotnosť cca. 4 mil. slnečných hmôt (4 mil. sĺnk) s priemerom okolo 12 mil. km, teda o niečo viac ako 31–krát vzdialenosti medzi Zemou a mesiacom, alebo 12–krát menej ako vzdialenosť medzi Zemou a slnkom.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addStrong('Čierne diery so strednou hmotnosťou', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('V porovnaní s inými sú relatívne malé, s hmotnosťou medzi sto až tisíc slnečných hmôt. Taktiež sú vzácnejšie a je ich ťažšie nájsť. Najväčšie z nich by mali priemer približne 3000 km – Slovensko by sa do takejto čiernej diery zmestilo asi sedemkrát. Najčastejšie sa nachádzajú v hustých hviezdokopách alebo v trpasličích galaxiách.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addStrong('Prvotné čierne diery', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Hypotetické čierne diery, ktoré mohli vzniknúť po veľkom tresku. Najmenšie zo všetkých, niektoré s hmotnosťou porovnateľnou so zrnkom piesku, iné porovnateľné s asteroidmi. Prvotná čierna diera s hmotnosťou Mount Everestu (~10', referatText);
    addSup('15', referatText);
    addSpan(' kg) by mala priemer okolo 10', referatText);
    addSup('–12', referatText);
    addSpan(' m. Pre porovnanie, protón má veľkosť približne 10', referatText);
    addSup('–15', referatText);
    addSpan(' m. Teoretizuje sa, že by mohli byť výsledkom alebo dôkazom temnej hmoty, či pôvodom supermasívnych čiernych dier.', referatText);
    addLineBreak(referatText);
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

    addSpan('G = 6.6743015208 × 10', massCalculatorUsedValues);
    addSup('-11', massCalculatorUsedValues);
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
    massCalculatorUserInput.placeholder = "Zadajte hmotnosť v kg";
    // event listener for enter, incase user doesn't like using mouse
    massCalculatorUserInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
          CalculateMassFromUserInput();
        }
    });
    massCalculatorContainer.appendChild(massCalculatorUserInput);
    
    // add confirm button
    const massCalculatorUserInputSubmitButton = document.createElement("button");
    massCalculatorUserInputSubmitButton.id = "massCalculatorUserInputSubmitButton";
    massCalculatorUserInputSubmitButton.classList.add("textChangeButton");
    massCalculatorUserInputSubmitButton.textContent = "Vypočítať";
    massCalculatorUserInputSubmitButton.onclick = CalculateMassFromUserInput;
    massCalculatorContainer.appendChild(massCalculatorUserInputSubmitButton);

    // add output box for calculated radius
    const massCalculatorRadiusOutput = document.createElement("p");
    massCalculatorRadiusOutput.id = "massCalculatorRadiusOutput";
    massCalculatorRadiusOutput.textContent = 'Ako desatiná čiarka je použitá bodka "."'
    massCalculatorContainer.appendChild(massCalculatorRadiusOutput)
}

function closeMassCalculator() { // close calculator on click outside the box
    const massCalculatorBackCover = document.getElementById("massCalculatorBackCover");
    const mainContentContainer = document.getElementById("mainContentContainer");
    mainContentContainer.removeChild(massCalculatorBackCover);
}

function CalculateMassFromUserInput() {
    const massCalculatorUserInput = document.getElementById("massCalculatorUserInput");
    const submitted_text = massCalculatorUserInput.value;
    const massCalculatorRadiusOutput = document.getElementById("massCalculatorRadiusOutput");
    if (isDigit(submitted_text)){
        var result = calculateSchwarzschildRadius(submitted_text);
        toString(result);
        massCalculatorRadiusOutput.textContent = `${result} m`;
    }
    else{
        massCalculatorRadiusOutput.textContent = 'Zadali ste zlú hodnotu. Ako desatiná čiarka je použitá bodka "."';
    }
}

function isDigit(input) {
    return !isNaN(input) && input.trim() !== ''; // check if input is a number
}

function calculateSchwarzschildRadius(M){
    const G = 6.6743015208e-11; // grav. constant in m3kg-1s-2
    const c = 3e8; // sol in m/s
    const Rs = ((2*G*M)/(Math.pow(c, 2))); // result in m
    const rounded = Rs.toExponential(5) // rounded to 5 decimal places
    return rounded;
}

function changeText1() {
    const referatText = document.getElementById("referatText");

    addStrong('Ako vznikne čierna diera?', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan('Tento proces je rozličný pre rôzne typy čiernych dier.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addStrong('Vznik Hviezdnej čiernej diery', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan('Takéto čierne diery vzniknú na konci života dostatočne veľkých hviezd. V procese života hviezda ,,využíva palivo” – prvky ako vodík, hélium a iné. Tento proces, jadrová fúzia, je potrebná pre hviezdu, pretože bez neho by nedokázala zdolať svoju vlastnú gravitáciu, čo je presne čo sa stane po vyčerpaní svojho ,,paliva.” Čo sa deje ďalej závisí od hmotnosti hviezdy.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan('Hviezdy s dostatočne veľkou hmotnosťou sa zrútia a ich jadro sa stlačí do singularity – bodu nekonečnej hustoty.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan('Zvyšok hviezdy je potom vyhodený von do vesmíru, čo sa nazýva supernova.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan('Ak nevznikne singularita, vzniká buď neutrónová hviezda, alebo hviezdna čierna diera.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addStrong('Vznik iných čiernych dier', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan('Väčšina čiernych dier vzniká kolapsom obrovského množstva hmoty, či už je to hviezda, extrémne hustý plyn, nárazom hviezd alebo galaxií.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);
    
    addSpan('Ďalšia možnosť je zlúčenie dvoch a viac čiernych dier, pričom vzniká nová, väčšia čierna diera a mnoho gravitačných vĺn. Takéto gravitačné vlny už dokonca boli skúmané observatóriami, ako napr. Virgo v Taliansku.', referatText);
    addLineBreak(referatText);

}

function changeText2() {
    const referatText = document.getElementById("referatText");

    addStrong('Ako tesne treba stlačiť hmotu pre vytvorenie čiernej diery?', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Teoreticky je možné vytvoriť čiernu dieru z akéhokoľvek malého či veľkého množstva hmoty. Na vypočítanie výsledného priemeru takejto extrémne stlačenej hmoty sa používa rovnica Schwarzschildovho polomeru: ', referatText);
    // add Rs=(2GM/c^2) as a fraction
    /*const formulaContainer = document.createElement("span"); // main container for formula
    formulaContainer.id = "formulaContainer";
    const leftSideContainer = document.createElement("span"); // container for left side of equation
    leftSideContainer.id = "leftSideContainer";
    leftSideContainer.textContent = "r";
    formulaContainer.appendChild(leftSideContainer);

    const leftSideSub = document.createElement("sub"); // subscript s 
    leftSideSub.innerText = "S";
    leftSideSub.style.fontSize = "10px";
    leftSideContainer.appendChild(leftSideSub);

    const equalsSign = document.createElement("span"); // "=" sign
    equalsSign.textContent = " = ";
    leftSideContainer.appendChild(equalsSign);

    const fractionContainer = document.createElement("span"); // container for fraction
    fractionContainer.classList.add("fracNumerator"); // styling
    const fractionNumerator = document.createElement("span"); // numerator content
    fractionNumerator.textContent = "2GM";
    fractionContainer.appendChild(fractionNumerator);

    const fractionDenominatorContainer = document.createElement("span"); // denominator container + c
    fractionDenominatorContainer.classList.add("fracDenominator");
    fractionDenominatorContainer.textContent = "c";
    fractionContainer.appendChild(fractionDenominatorContainer);

    const fractionDenominatorExponent = document.createElement("sup"); // exponent ^2
    fractionDenominatorExponent.textContent = "2";
    fractionDenominatorContainer.appendChild(fractionDenominatorExponent);
    // finalize
    formulaContainer.appendChild(fractionContainer); // add the formula to the container
    referatText.appendChild(formulaContainer); // add everything to whole text box */

    const formulaContainer = document.createElement("span");
    formulaContainer.innerHTML = `<span class="fractionContainer">
    r<sub>s</sub> = <span class="rightSideContainer" id="SRadiusRightSide">
        <span>2GM</span>
        <hr class="fractionLine">
        <span>c<sup class="formulaExponent">2</sup></span>
    </span>
</span>

`;
    referatText.appendChild(formulaContainer);

    // add button to open calculator
    const massCalculatorOpenButton = document.createElement("button");
    massCalculatorOpenButton.classList.add("textChangeButton");
    massCalculatorOpenButton.id = "massCalculatorOpenButton";
    massCalculatorOpenButton.textContent = "Otvoriť kalkulačku";
    massCalculatorOpenButton.onclick = showPopUpCalculator;
    referatText.appendChild(massCalculatorOpenButton);
}

function changeText3() {
    addStrong('Prekročenie horizontu udalostí', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Povedzme, že astronaut sa rozhodne preskúmať čiernu dieru, nazvime ho Jozef. Vonkajšiemu pozorovateľovi by sa zdalo akoby sa Jozef pohyboval čoraz pomalšie pri približovaní k horizontu udalostí. Po nejakom čase by sa Jozef javil akoby zamrazený v mieste a čase. Tento efekt je spôsobený silnou časovou dilatáciou spôsobenou gravitáciou čiernej diery. Jozef by však nezostal zamrazený naveky, časom by jeho svetlo podliehalo stmaveniu a červenému posunu (červenelo by), čím by sa časom stal akoby neviditeľným.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Jozef by si však časovú dilatáciu počas celého procesu nevšimol, preňho by sa čas pohyboval normálnou rýchlosťou. Pred prekročením horizontu udalostí by bol relatívne ,,ok,” no po prekročení by začal proces špagetizácie', referatText);
    addSpan('. Kvôli rozdielu sily gravitácie medzi jeho nohami a hornou časťou tela by z jeho pohľadu začal vyzerať ako nešťastná špageta (za predpokladu že by ešte bol schopný vidieť) – natiahol by sa. V prípade supermasívnej čiernej diery by trvalo možno trochu dlhšie kým by tento proces začal, no nie je možné mu uniknúť, keďže ani svetlo nedokáže uniknúť pred gravitáciou čiernej diery po prekročení horizontu udalostí.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Eventuálne by sa dostal ku singularite, kde sú jeho smrť a absolútne zničenie garantované. Kvôli ohybe časopriestoru vnútri čiernej diery všetky možné cesty vedú do singularity, čiže by tomuto nemal ako predísť.', referatText);
    addLineBreak(referatText);
}

function changeText4() {
    const referatText = document.getElementById("referatText");

    addStrong('Hawkingovo žiarenie', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Teória Stephena Hawkinga tvrdí, že kvôli kvantovým mechanickým efektom čierne diery sa časom odparujú.', referatText);
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Používa pritom princíp kvantových fluktuácií. Podľa kvantovej fyziky vákuum nie je naozaj prázdno, ale neustále produkuje páry virtuálnych častíc a antičastíc, ktoré sa neustále objavujú a zanikajú. Tieto častice sa takmer ihneď zničia. Za normálnych okolností tento proces nič neruší, no nepredstaviteľná gravitácia čiernej diery na jej horizonte udalostí môže teoreticky spôsobiť to, že čierna diera jednu častice pohltí, no druhej sa podarí prežiť. Táto častica teda ,,ukradne” miniatúrne množstvo energie čiernej diery, vďaka ktorej sa jej môže podariť uniknúť do vesmíru.', referatText);
    addLineBreak(referatText);

    addSpan('Častica, ktorá prenikne do čiernej diery má negatívnu energiu relatívne k vonkajšiemu vesmíru kvôli ohybu časopriestoru. Kombinácia prijatia tejto negatívnej častice a vypustenia malého množstva svojej vlastnej energie spôsobí, že čierna diera stratí malé množstvo svojej hmoty cez Einsteinovu rovnicu E = mc', referatText);
    addSup('2', referatText);  
    addLineBreak(referatText);
    addLineBreak(referatText);

    addSpan('Výsledkom tohto procesu je odparovanie čiernej diery. Toto odparovanie je však pomalšie pre väčšie čierne diery. Najväčšej čiernej diere o ktorej vieme, TON 618, by trval tento proces 7,64 * 10', referatText);
    addSup('98', referatText);  
    addSpan(' rokov. Pre porovnanie, odhadovaný vek nášho vesmíru je 1,38 * 10', referatText);
    addSup('10', referatText);  
    addSpan(' rokov.', referatText);
    addLineBreak(referatText);
}

function BHAnatomyOpenPopUp() {
    const mainContentContainer = document.getElementById("mainContentContainer"); 
    const BHAnatomyContentContainer = document.createElement("div"); 
    const massCalculatorBackCover = document.createElement("div");
    const massCalculatorCloseButton = document.createElement("button");
    const BHAnatomyTextContainer = document.createElement("p");
    const BHAnatomyImageContainer = document.createElement("div");

    massCalculatorBackCover.id = "massCalculatorBackCover"; // add back cover and main parent
    mainContentContainer.appendChild(massCalculatorBackCover);

    BHAnatomyContentContainer.id = "BHAnatomyContentContainer"; // add container for content
    massCalculatorBackCover.appendChild(BHAnatomyContentContainer)

    massCalculatorCloseButton.id = "massCalculatorCloseButton"; // add close button
    massCalculatorCloseButton.onclick = () => {
        mainContentContainer.removeChild(massCalculatorBackCover);
    }
    BHAnatomyContentContainer.appendChild(massCalculatorCloseButton);

    BHAnatomyTextContainer.id = "BHAnatomyTextContainer"; // add space for text
    BHAnatomyTextContainer.classList.add("textContainer");
    BHAnatomyContentContainer.appendChild(BHAnatomyTextContainer);

    BHAnatomyImageContainer.id = "BHAnatomyImageContainer";
    BHAnatomyContentContainer.appendChild(BHAnatomyImageContainer);
}

function BHAnatomyTextEventHorizon() {
    // initialize
    BHAnatomyOpenPopUp();
    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Horizont udalostí', textParent);
    addLineBreak(textParent);
    addLineBreak(textParent);

    addSpan('Môžeme si ho predstaviť ako ,,povrch” čiernej diery. V prípade nerotujúcej čiernej diery má guľový tvar. Je to skôr hranica než doslovný povrch, ktorá sa dá nazvať aj ako bod, odkiaľ niet návratu. Gravitácia presne v oblasti horizontu udalostí je tak silná, že rýchlosť potrebná pre únik z nej je rovný rýchlosti svetla. Ak objekt prenikne hlbšie do čiernej diery, nebude možné preň uniknúť.', textParent);
    addLineBreak(textParent);

    // add image(s)
    const blackHolePicture = document.createElement("img");
    blackHolePicture.classList.add("BHAnatomyPicture");
    blackHolePicture.src = "../images/Black-hole-M87-centre-evidence-supermassive-black.webp";
    blackHolePicture.style.backgroundColor = "orange";
    imgParent.appendChild(blackHolePicture);
}

function BHAnatomyTextAccretionDisk() {
    // initialize
    BHAnatomyOpenPopUp()

    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Akrečný disk', textParent);
    addLineBreak(textParent);
    addLineBreak(textParent);

    addSpan('Pri akrécii, narastaní čiernej diery, čierna diera ťahá plyn od hviezd, alebo inú hmotu iného objektu, ktorá potom začne obiehať čiernu dieru. Pretože gravitácia čiernych dier je pre ich veľkosť nadmerná, táto hmota sa pohybuje extrémne rýchlo a postupom času sa zahrieva, čo vyžaruje svetlo, ktoré je potom možné vidieť. Akrečný disk má zvláštny tvar kvôli ohybu svetelných lúčov gravitáciou čiernej diery.', textParent);
    addLineBreak(textParent);

    // add image(s)
    const accretionDiskPicture = document.createElement("img");
    accretionDiskPicture.classList.add("BHAnatomyPicture");
    accretionDiskPicture.src = "../images/Black_Hole_Accretion_Disk_Sim_4k_ProRes.00386_print.webp";
    accretionDiskPicture.style.backgroundColor = "orange";
    imgParent.appendChild(accretionDiskPicture);
}

function BHAnatomyTextEHShadow() {
    // initialize
    BHAnatomyOpenPopUp()

    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Tieň horizontu udalostí', textParent);
    addLineBreak(textParent);
    addLineBreak(textParent);

    addSpan('Niečo akoby troj-dimenzionálny tieň, tá časť čiernej diery, ktorú si človek často predstaví ako tú ,,dieru” čiernej diery. Je asi dvakrát taký veľký ako ozajstná čierna diera.', textParent);
    addLineBreak(textParent);
}

function BHAnatomyTextPhotonSphere() {
    // initialize
    BHAnatomyOpenPopUp()

    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Fotónová sféra', textParent);
    addLineBreak(textParent);
    addLineBreak(textParent);

    addSpan('Tenké svetelné krúžky na hranici tieňa horizontu udalostí. Sú to v skutočnosti vysoko skreslené obrazy akrečného disku. Toto svetlo obehne čiernu dieru aj viackrát pred tým, ako sa mu podarí utiecť.', textParent);
    addLineBreak(textParent);

    // add image(s)
    const photonSphereInfo = document.createElement("img");
    photonSphereInfo.classList.add("BHAnatomyPicture");
    photonSphereInfo.src = "../images/photon sphere 2.webp";
    photonSphereInfo.style.backgroundColor = "orange";
    imgParent.appendChild(photonSphereInfo);
}

function BHAnatomyTextDopplerEffect() {
    // initialize
    BHAnatomyOpenPopUp()

    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Dopplerov jav', textParent);
    addLineBreak(textParent)
    addLineBreak(textParent)
    addSpan('Tento jav spôsobuje, že časti akrečného disku sú v určitých oblastiach – ďalej od pozorovateľa – tmavšie a viac červené, pričom časti bližšie pri pozorovateľovi sú svetlejšie a modrejšie.', textParent);
    addLineBreak(textParent);

    // add image(s)
    const dopplerEffectPicture = document.createElement("img");
    dopplerEffectPicture.classList.add("BHAnatomyPicture");
    dopplerEffectPicture.src = "../images/doppler-effect.jpg";
    dopplerEffectPicture.style.backgroundColor = "orange";
    imgParent.appendChild(dopplerEffectPicture);
}

function BHAnatomyTextCorona() {
    // initialize
    BHAnatomyOpenPopUp()

    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Koróna', textParent);
    addLineBreak(textParent);
    addLineBreak(textParent);

    addSpan('Slabý, turbulentný extrémne horúci oblak tesne za akrečným diskom. Fyzici ju označujú ako jedno z najextrémnejších fyzických prostredí vo vesmíre. Nachádzajú sa tu extrémne silné magnetické polia. Častice v koróne obiehajú čiernu dieru takmer rýchlosťou svetla. Astronómovia sa stále snažia bližšie určiť jej rozsah, tvar a iné vlastnosti.', textParent);
    addLineBreak(textParent);

    // add image(s)
    const coronaPicture = document.createElement("img");
    coronaPicture.classList.add("BHAnatomyPicture");
    coronaPicture.src = "../images/Corona-1.jpeg";
    coronaPicture.style.backgroundColor = "orange";
    imgParent.appendChild(coronaPicture);
}

function BHAnatomyTextParticleJets() {
    // initialize
    BHAnatomyOpenPopUp()

    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Časticové prúdy', textParent);
    addLineBreak(textParent);
    addLineBreak(textParent);

    addSpan('Prúdy častíc, ktoré vystrelia takmer rýchlosťou svetla od vnútorného okraja akrečného disku. V prípade supermasívnych čiernych dier sú niekedy dlhé aj niekoľko stotisíc svetelných rokov.', textParent);
    addLineBreak(textParent);

    // add image(s)
    const particleJetsPicture = document.createElement("img");
    particleJetsPicture.classList.add("BHAnatomyPicture");
    particleJetsPicture.src = "../images/Particle_jets-1.jpeg";
    particleJetsPicture.style.backgroundColor = "orange";
    imgParent.appendChild(particleJetsPicture);
}

function BHAnatomyTextSingularity() {
    // initialize
    BHAnatomyOpenPopUp();
    const textParent = document.getElementById("BHAnatomyTextContainer");
    const imgParent = document.getElementById("BHAnatomyImageContainer");

    // add text
    addStrong('Singularita', textParent);
    addLineBreak(textParent);
    addLineBreak(textParent);

    addSpan('Stred čiernej diery, ktorý predpokladá Einsteinova teória všeobecnej relativity, kde je hmota stlačená do nekonečnej hustoty. Je to konečná zástavka pre hocičo, čo sa dostane za horizont udalostí. Nie je jasné, či singularita naozaj fyzicky existuje, alebo je možná len z čisto matematického hľadiska.', textParent);
    addLineBreak(textParent);

    // add image(s)
    const singularityPicture = document.createElement("img");
    singularityPicture.classList.add("BHAnatomyPicture");
    singularityPicture.src = "../images/singularity1.jpg";
    singularityPicture.style.backgroundColor = "orange";
    imgParent.appendChild(singularityPicture);
}

function scrollToItem(targetID) {
    const target = document.getElementById(targetID);
    target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    target.style.background = "grey";
    console.log("highlited");
    
    setTimeout(() => {
        target.style.background = "transparent";
        console.log("changed back");
    }, 1000); // highlight for easier use
    
}
