import random
import os

currentFilePath = os.path.abspath(__file__)

def replaceVowelsWithRandomVowel():
    # zadefinuj cesty k suborom
    readFileRelativePath = os.path.join("..", "piesen.txt")
    readFileABSPath = os.path.abspath(os.path.join(currentFilePath, readFileRelativePath))

    writeFileRelativePath = os.path.join("..", "piesenNova.txt")
    writeFileABSPath = os.path.abspath(os.path.join(currentFilePath, writeFileRelativePath))

    changedText = ""
    # zamen samohlasky za nahodnu samohlasku
    with open(readFileABSPath, "r", encoding="UTF-8") as f:
        piesenText:str = f.read()
        vowels = [char for char in "aAáÁeEéÉiIíÍoOóÓôÔuUúÚyYýÝäÄ"]
        randomVowel = random.choice(vowels)
        for letter in vowels:
            piesenText = piesenText.replace(letter, randomVowel)
        changedText = piesenText

    # zapis do suboru
    with open(writeFileABSPath, "w", encoding="UTF-8") as f:
        f.write(changedText)

def makePracticeDictation():
    # zadefinuj cesty k suborom
    readFileRelativePath = os.path.join("..", "vybraneslova.txt")
    readFileABSPath = os.path.abspath(os.path.join(currentFilePath, readFileRelativePath))

    writeFileRelativePath = os.path.join("..", "diktat.txt")
    writeFileABSPath = os.path.abspath(os.path.join(currentFilePath, writeFileRelativePath))

    # zamen icka s _
    changedText = ""
    with open(readFileABSPath, "r", encoding="UTF-8") as f:
        dictationText:str = f.read()
        icka:str = "iIíÍyYýÝ"
        for letter in icka:
            dictationText = dictationText.replace(letter, "_")
        changedText = dictationText

    # zapis do suboru
    with open(writeFileABSPath, "w", encoding="UTF-8") as f:
        f.write(changedText)
    
def isPalindrome(myStr):
    return myStr == myStr[::-1]

def countLetters():
    # nadefinuj cesty k suborom
    readFileRelativePath = os.path.join("..", "slogan.txt")
    readFileABSPath = os.path.abspath(os.path.join(currentFilePath, readFileRelativePath))
    
    lettersCount = {}

    with open(readFileABSPath, "r", encoding="UTF-8") as f:
        myText = f.read()
        for letter in myText:
            if letter.isalnum():
                if letter not in lettersCount:
                    lettersCount[letter] = 0
                lettersCount[letter] += 1
    
    print(lettersCount)
    
def containsWord(word):
    readFileRelativePath = os.path.join("..", "piesen.txt")
    readFileABSPath = os.path.abspath(os.path.join(currentFilePath, readFileRelativePath))
    
    with open(readFileABSPath, "r", encoding="UTF-8") as f:
        piesenText:str = f.read()
        return word in piesenText

replaceVowelsWithRandomVowel()
makePracticeDictation()
print(isPalindrome("aabbaa"))
countLetters()
print(containsWord("Odrezal"))
print(containsWord("odrez"))
print(containsWord("odrezal"))
