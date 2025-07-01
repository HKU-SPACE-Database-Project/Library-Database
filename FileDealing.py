#FileDealing.py

def Read(FName):
    Wordlist = []
    with open(FName,'r') as opf:
        while(True):
            Wordlist.append(opf.readline())
            if Wordlist[len(Wordlist)-1] == "":
                break
    return Wordlist

        
