import os

filePath = os.path.abspath(__file__)
relativeTextFilePath = os.path.join("..", "triedny fond.txt")
ABSPATH_textFilePath = os.path.abspath(os.path.join(filePath, relativeTextFilePath))

with open(ABSPATH_textFilePath, "r", encoding="utf-8") as file:
    data = file.read()
    transactionLog = [item.split(",") for item in data.split("\n")]
    transDict = {}
    for item in transactionLog:
        if item[0] not in transDict:
            transDict[item[0]] = 0
        transDict[item[0]] += float(item[1])
        
    transDict["Zostatok"] = sum(transDict.values())
    transFinal = [item.replace("[", "").replace("]", "").replace("'", "") for item in list(map(str, [list(item) for item in list(transDict.items())]))]

print(transDict)

with open(ABSPATH_textFilePath, "w", encoding="utf-8") as f:
    f.write("\n".join(transFinal))
