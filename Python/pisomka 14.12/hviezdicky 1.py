import os

dirPath = os.path.dirname(__file__)
resultPath = os.path.join(dirPath, "hviezdicky output.txt")

pocetHviezdiciek = int(input("Zadaj pocet hviezdiciek v 1. riadku: "))

def make_line(number):
    result = ""
    for i in range(number):
        result += "*"
    return result

def make_stars(amount: int):
    final = ""
    for i in range(amount):
        final += f"{make_line(amount)}\n"
        amount -= 1
    return final

answer = make_stars(pocetHviezdiciek)
print(answer)

with open(resultPath, "w", encoding="utf-8") as f:
    f.write(answer)