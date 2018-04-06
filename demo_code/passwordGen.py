import random

nouns = []
verbs = []
adjectives = []

def genPassword():
    if not nouns or not verbs or not adjectives:
        loadFiles()

    password = getRandomWord() + "-" + getRandomWord() + "-" + str(random.randint(0,100))
    return password
    

def loadFiles():
    global nouns, verbs, adjectives

    # Read in the nouns
    with open('commonEnglish/50nouns.txt') as f:
        nouns = f.read().splitlines()
    f.close()

    # Read in the verbs
    with open('commonEnglish/50verbs.txt') as f:
        verbs = f.read().splitlines()
    f.close()

    # Read in the nouns
    with open('commonEnglish/50adjectives.txt') as f:
        adjectives = f.read().splitlines()
    f.close()

def getRandomWord():
    global nouns, verbs, adjectives
    typeOfWord = random.randint(1,3)

    if typeOfWord == 1: return nouns[random.randint(0,49)]
    elif typeOfWord == 2: return verbs[random.randint(0,49)]
    else: return adjectives[random.randint(0,49)]

if __name__ == "__main__":
    print genPassword()