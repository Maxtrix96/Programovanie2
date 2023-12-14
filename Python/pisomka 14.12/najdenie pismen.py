userInput = input("Zadaj text na najdenie pismen: ")

def find_letters(text):
    aCount, cCount, ACount, CCount = text.count("a"), text.count("c"), text.count("A"), text.count("C")
    result = f"Pocet a: {aCount}\nPocet A: {ACount}\nPocet c: {cCount}\nPocet C: {CCount}"
    return result

print(find_letters(userInput))