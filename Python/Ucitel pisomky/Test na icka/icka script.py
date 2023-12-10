import os

filePath = os.path.abspath(__file__)
relativeTextFilePath1 = os.path.join("..", "icka test original.txt")
textFilePath1 = os.path.abspath(os.path.join(filePath, relativeTextFilePath1))
relativeTextFilePath2 = os.path.join("..", "icka test vysledok.txt")
textFilePath2 = os.path.abspath(os.path.join(filePath, relativeTextFilePath2))

def erase_i_y(Text):
    translation = str.maketrans("iíIÍyýYÝ", "________")
    translatedText = Text.translate(translation)
    
    return translatedText

with open(textFilePath1, "r", encoding="utf-8") as file:
    originalText = file.read()
    updatedText = erase_i_y(originalText)

with open(textFilePath2, "w", encoding="utf-8") as file:
    file.write(updatedText)