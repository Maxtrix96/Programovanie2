myFile = "C://Users/anton/Desktop/compooter backups/skola/Dejepis/sussous.txt"

with open(myFile, "r", encoding="utf-8") as file:
    readFIle = file.read()
    print(readFIle)