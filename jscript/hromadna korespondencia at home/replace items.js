const XLSX = require('xlsx');
const workbook = XLSX.readFile('hromadna koresp tabulka.xlsx'); // Load local file
const sheetName = workbook.SheetNames[0]; // Get the first sheet
const data = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName]); // Convert to JSON
const fs = require('fs');
const mammoth = require('mammoth');

function saveDataAsJSONFile(inputtedData) {
    let myInfo = inputtedData;

    // Convert the object to a JSON string
    const readData = JSON.stringify(myInfo, null, 2); // Pretty-print with 2 spaces

    // Write the JSON string to a file
    fs.writeFileSync('info.json', readData);

    console.log('JSON file has been saved as info.json');
}
saveDataAsJSONFile(data);

console.log(data); // Display sheet data


// Function to extract text and return a promise
function extractTextFromDocx(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, (err, data) => {
            if (err) reject(err);
            mammoth.extractRawText({ buffer: data })
                .then(result => {
                    console.log("got the thing");
                    resolve(result.value); // Return the extracted text
                })
                .catch(reject);
        });
    });
}

const { Document, Packer, Paragraph } = require('docx');
const { info } = require('console');
const { type } = require('os');

async function createDocx(text, iteration) {
    // Create a new document
    const doc = new Document({
        sections: [
            {
                properties: {},
                children: [new Paragraph(text)], // Add the string as a paragraph
            },
        ],
    });

    // Generate the .docx file
    const buffer = await Packer.toBuffer(doc);

    // Save to file
    fs.writeFileSync(`finished files/output${iteration}.docx`, buffer);
    console.log(`File saved: output${iteration}.docx`);
}

function massMailingAtHome(originalDocumentText, spreadsheet){
    for (i = 0; i < spreadsheet.length; i++) {
        var customDocumentText = originalDocumentText; // document to insert stuff into

        // udaje z tabulky
        var information = spreadsheet[i]; // struktura dana = meno: {meno}, priezvisko: {priezvisko}, ...

        if ("Pohlavie" in information) {
            customDocumentText = customDocumentText.replace("{{Pohlavie}}", information["Pohlavie"] === "Muž" ? "ý" : "á"); // grammer thumbsup
        }else{
            customDocumentText = customDocumentText.replace("{{Pohlavie}}", "ý/á"); // ak nie je udaj Pohlavie, napis cez ý/á
        }
        Object.keys(information).forEach(key => {
            const regex = new RegExp(`{{${key}}}`, 'g'); // Global flag to replace all occurrences
            customDocumentText = customDocumentText.replace(regex, information[key]);
        });

        createDocx(customDocumentText, i); // call function to save as .docx file
    }
}

// Example usage with async/await
async function getText(filePath) {
    try {
        const text = await extractTextFromDocx(filePath);
        console.log
        massMailingAtHome(text, data);
    } catch (err) {
        console.error(err);
    }
}

getText('hromadna korespondencia.docx');