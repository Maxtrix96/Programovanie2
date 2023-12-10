import random
import os

filePath = os.path.abspath(__file__)
relativeTextFilePath1 = os.path.join("..", "ulohy.txt")
listOfAvaialableQuestionsABSPATH = os.path.abspath(os.path.join(filePath, relativeTextFilePath1))

def create_abs_path(BaseName=str):
    relativeFinishedExamFilePath = os.path.join("..", "vytvorene pisomky",BaseName)
    ABSPATH_OfTestFile = os.path.abspath(os.path.join(filePath, relativeFinishedExamFilePath))
    return ABSPATH_OfTestFile

def create_questions(TextLines, NumberOfQuestions=int):
    generatedSample = random.sample(TextLines, NumberOfQuestions) #zadajte pocet uloh sem, max v mojom ulohy.txt je 19
    generatedText = "\n".join(generatedSample)
    return generatedText    

def create_tests(NumberOfTests=int, NumberOfQuestions=int):
    for i in range(NumberOfTests):
        with open(listOfAvaialableQuestionsABSPATH, "r", encoding="utf-8") as questions:
            originalText = questions.read()
            textLines = originalText.split("\n")
            generatedText =  create_questions(textLines, NumberOfQuestions)

        examName = create_abs_path(f"vysledna pisomka{i+1}.txt")
        with open(examName, "w", encoding="utf-8") as finishedTest:
            finishedTest.write(generatedText)


inputNumberOfTests = int(input("Zadaj pocet vygenerovanych pisomiek: "))
inputNumberOfQuestions = int(input("Zadaj pocet vygenerovanych otazok na pisomku: "))
create_tests(inputNumberOfTests, inputNumberOfQuestions) 