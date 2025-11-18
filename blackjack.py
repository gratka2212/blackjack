from random import randint

def createDeck():
    figures = {11:"jack", 12:"queen", 13:"king", 14:"ace"}
    colors = ["hearts", "diamonds", "spades", "clubs"]
    deck = []


    for item in colors:
        for i in range(2, 15):
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
    #print(f"\n\n{r}")
    #print(deck)
    #print(deck[r])
    #print("\n\n")
    randomCard = deck[r]

    cardIndex = getIndex(randomCard, deck)
    deck.pop(cardIndex)

    return randomCard, deck

def getValue(card):
    #print(card)
    valueStr = ""
    i = 0
    while(card[i] != " "):
        valueStr = valueStr + card[i]
        i += 1
    
    try:
        value = int(valueStr)
    except:
        if valueStr != "ace":
            value = 10
        else:
            value = 11

    return value

def cardsInHand(card, cards):
    count = 0
    for item in cards:
        cardV = ""
        i = 0
        while(item[i] != " "):
            cardV = cardV + item[i]
            i += 1
        if card == cardV:
            count += 1
    return count

def hit(deck, cards, points):
    card, deck = drawCard(deck)
    cards.append(card)
    value = getValue(card)
    points += value
    if points > 21:
        points = 0
        aces = cardsInHand("ace", cards)
        for item in cards:
            value = getValue(item)
            points += value
        for i in range(aces):
            points -= 10
            if points <= 21:
                i = aces - 1
    return deck, cards, points


############# START AND SETUP #############
deck = createDeck()
nextGame = "Y"

while(nextGame.capitalize() == "Y"):

    playerCards = []
    dealerCards = []
    playerPoints = 0
    dealerPoints = 0
    for i in range(2):      # FIRST TWO CARDS FOR PLAYER
        card, deck = drawCard(deck)
        playerCards.append(card)
        value = getValue(card)
        playerPoints += value

    for i in range(2):      # FIRST TWO CARDS FOR DEALER
        card, deck = drawCard(deck)
        dealerCards.append(card)
        value = getValue(card)
        dealerPoints += value

    print(f"DEALER:\n{dealerCards[0]},      X\n\n")

    for item in playerCards:
        print(item)
    print(f"Points: {playerPoints}")

    if playerPoints == 21:
        print("\n####################\n###   YOU WIN    ###\n####################")
        print("\n\n")
        for item in playerCards:
            print(item)
        print(playerPoints)
        exit()


    ################## GAME ##################
    decision = input("Hit or Stand?\n")
    while(True):
        if decision.capitalize() == "Hit":
            deck, playerCards, playerPoints = hit(deck, playerCards, playerPoints)
            if playerPoints == 21:
                decision = "Stand"
                print("\n\n")
                for item in playerCards:
                    print(item)
                print(playerPoints)
                continue

        elif decision.capitalize() == "Stand":
            print("\n\n")
            for item in dealerCards:
                print(item)
            print(f"Points: {dealerPoints}")

            while(dealerPoints <= 16):
                deck, dealerCards, dealerPoints = hit(deck, dealerCards, dealerPoints)
                print("\n\n")
                for item in dealerCards:
                    print(item)
                print(f"Points: {dealerPoints}")

            if dealerPoints > 21 or dealerPoints < playerPoints:
                print("\n####################\n###   YOU WIN    ###\n####################")

            elif dealerPoints == playerPoints:
                print("\n####################\n###  IT'S A TIE  ###\n####################")

            else:
                print("\n####################\n###   YOU LOSE   ###\n####################")

            break

        else:
            print("Instructions unclear.")
            decision = input("Hit or Stand?\n")
            continue

        print("\n\n")
        for item in playerCards:
            print(item)
        print(playerPoints)

        if playerPoints > 21:
            print("\n####################\n###   YOU LOSE   ###\n####################")
            break
        
        decision = input("Hit or Stand?\n")
    if len(deck) > 26:
        nextGame = input("Do you want to play another round? (Y/N)\n")
        print("\n\n")
    else:
        deck = createDeck()
        nextGame = input("Do you want to play a new game? (Y/N)\n")
        print("####################\n###   RESTART    ###\n####################")
