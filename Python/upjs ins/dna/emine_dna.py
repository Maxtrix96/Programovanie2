import os

currentFilePath = os.path.abspath(__file__)

readFileRelativePath = os.path.join("..", "DNA-casti.txt")
readFileABSPath = os.path.abspath(os.path.join(currentFilePath, readFileRelativePath))

writeFileRelativePath = os.path.join("..", "dna-vysledok.txt")
writeFileABSPath = os.path.abspath(os.path.join(currentFilePath, writeFileRelativePath))

class DNAProcesy():
    def __init__(self) -> None:
        with open(readFileABSPath, "r", encoding="UTF-8") as f:
            self.contents:str = f.read()
            self.lines:list[str] = self.contents.strip().split("\n")
            self.sequencesInLines:list[list[str]] = [line.split(" ") for line in self.lines]
        
        self.combineSequences()

        with open(writeFileABSPath, "w", encoding="UTF-8") as f:
            result:str = ""
            for seqs in self.sequencesInLines:
                result += "".join(seqs)
                result += "\n"
            f.write(result)
    
    def combineSequences(self):
#        for sequences in self.sequencesInLines:
#            ## nemozme ich duplikovat lubovolne
#            usedSequences:list[bool] = [False] * len(sequences)
#            # pri kazdom retazci sekvencii sa pozerame na jednotlive sekvencie
#            for i in range(len(sequences)):
#                seq:str =  sequences[i]
#                for j in range(len(sequences)):
#                    # ak sa nepozerame na rovnaku sekvenciu, mozeme ich skusit skombinovat
#                    if i != j and self.areCompatible(sequences[i], sequences[j]):
        for i in range(len(self.sequencesInLines)):
            seqs = self.sequencesInLines[i]
            # postupne pripajame prvy retazec k nejakemu dalsiemu (ci uz na koniec alebo zaciatok) a pripojenu 
            # sekvenciu odstranime
            while len(seqs) > 1:
                index = 1
                keepCombining = True
                while keepCombining:
                    # az ku koncu sa da pripojit nieco
                    if seqs[0][-4:] == seqs[index][0:4]:
                        # spoj ich
                        seqs[0] = seqs[0] + seqs[index][4:]
                        # potrebujeme dalsiu iteraciu
                        keepCombining = False
                        # odstran pripojene
                        seqs.remove(seqs[index])
                    # ak sa na zaciatok da nieco pripojit
                    elif seqs[0][0:4] == seqs[index][-4:]:
                        # spoj ich
                        seqs[0] = seqs[index][:-4] + seqs[0]
                        # potrebujeme dalsiu iteraciu
                        keepCombining = False
                        # odstran pripojene
                        seqs.remove(seqs[index])
                    index += 1
            self.sequencesInLines[i] = seqs
        print(self.sequencesInLines)
        
        


            
procesy = DNAProcesy()