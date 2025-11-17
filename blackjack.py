from random import randint

def createDeck():
    figures = {11:"jack", 12:"queen", 13:"king", 14:"ace"}
    colors = ["hearts", "diamonds", "spades", "clubs"]
    deck = []


    for item in colors:

        for i in range(1, 15):

            if i <= 10:
                c = str(i)
            else:
                c = figures[i]
            card = c + " of " + item
            deck.append(card)
    return deck

def getIndex(card, deck):
    for i, item in enumerate(deck):
        if item == card:
            return i

def drawCard(deck):
    r = randint(0, len(deck)-1)
    randomCard = deck[r]

    cardIndex = getIndex(randomCard, deck)
    deck.pop(cardIndex)

    return randomCard, deck

def getValue(card):
    numStr = ""
    i = 0
    while(card[i] != " "):
        numStr = numStr + card[i]
        i += 1
    
    try:
        num = int(numStr)
    except:
        if numStr != "ace":
            num = 10
        else:
            num = 11

    print(num)

    return num


deck = createDeck()
q = "t"
while(q == "t"):

    card, deck = drawCard(deck)
    print(card)
    #print(deck)
    getValue(card)

    q = input("Dalej? ")