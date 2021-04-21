import getCard

result = {
        "Player": -1,
        "Banker": -1
    }

def setResult(player, banker):
    result["Player"] = player
    result["Banker"] = banker

# Generate third card, add to total and return total.
def getTotal(total):
    thirdCard = getCard.randomCard()
    total += thirdCard
    total = total % 10

    return total


def baccaratHand(playerInitial, bankerInitial):
    ## Hand finished after initial deal condition.

    # Initial tie
    if (playerInitial >= 6 and playerInitial <= 9) and \
          (playerInitial >= 6 and playerInitial <= 9) and \
          (playerInitial == bankerInitial):
        setResult(playerInitial, bankerInitial)
        return result

    # Player natural
    elif playerInitial == 8 or playerInitial == 9:
        setResult(playerInitial, bankerInitial)
        return result

    # Bank natural
    elif (bankerInitial == 8 or bankerInitial == 9):
        setResult(playerInitial, bankerInitial)
        return result

    # 7-6 Conditions
    elif (playerInitial == 7 and bankerInitial == 6 or
          bankerInitial == 7 and playerInitial == 6):
        setResult(playerInitial, bankerInitial)
        return result

    ## Third card conditions

    playerTotal = playerInitial
    bankerTotal = bankerInitial

    ## Stand conditions


    # Player stands on 6 or 7
    if playerInitial == 6 or playerInitial == 7:
        bankerTotal = getTotal(bankerTotal)
        setResult(playerTotal, bankerTotal)

        return result
    # Bank stands on 7
    elif bankerInitial == 7:
        playerThird = getCard.randomCard()
        playerTotal += playerThird
        playerTotal = playerTotal % 10

        setResult(playerTotal, bankerTotal)
        return result

    ## Player tableau

    # Player draw
    if playerInitial >= 0 and playerInitial <= 5:
        playerThird = getCard.randomCard()
        playerTotal += playerThird
        playerTotal = playerTotal % 10
   

    ## Bank tableau

    # Bank draw
    if bankerInitial >= 0 and bankerInitial <= 2:
        bankerTotal = getTotal(bankerTotal)
    # Bank == 3
    elif bankerInitial == 3 and playerThird != 8:
        bankerTotal = getTotal(bankerTotal)
    # Bank == 4
    elif bankerInitial == 4 and (playerThird >= 2 and playerThird <= 7):
        bankerTotal = getTotal(bankerTotal)
    # Bank == 5
    elif bankerInitial == 5 and (playerThird >= 4 and playerThird <= 7):
        bankerTotal = getTotal(bankerTotal)
    # Bank == 6
    elif bankerInitial == 6 and (playerThird == 6 or playerThird == 7):
        bankerTotal = getTotal(bankerTotal)
    

    setResult(playerTotal, bankerTotal)
    return result






    
    




