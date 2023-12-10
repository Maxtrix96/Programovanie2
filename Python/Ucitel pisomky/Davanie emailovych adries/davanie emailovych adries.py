import os
filePath = os.path.abspath(__file__)
relativeTextFilePath1 = os.path.join("..", "ziaci.txt")
ABSPATH_ziaciFile = os.path.abspath(os.path.join(filePath, relativeTextFilePath1))

with open(ABSPATH_ziaciFile, "r", encoding="utf-8") as f:
    data = f.read()
    data = data.split("\n")
    peopleLog = ""

    for person in data:
        personData = person.split(":")
        firstName = personData[0]
        lastName = personData[1]
        personData.append(f"{firstName}.{lastName}@gmk-ra.sk")
        personFinal = f"{personData[0]}:{personData[1]}:{personData[2]}"
        peopleLog += f"{personFinal}\n"

with open(ABSPATH_ziaciFile, "w", encoding="utf-8") as f:
    f.write(peopleLog)