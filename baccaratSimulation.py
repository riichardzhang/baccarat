# Written by Richard Zhang

import runHand
import getCard
import getStats

NUMHANDS = 100000

result_frequency = {
    "Player": 0,
    "Banker": 0,
    "Tie": 0,
    "Banker6": 0,
    "playerPair": 0,
    "bankerPair": 0
}

def generateHands(result_frequency):
    for i in range(NUMHANDS):
        # Generate initial deal
        bank1 = getCard.randomCard()
        bank2 = getCard.randomCard()
        player1 = getCard.randomCard()
        player2 = getCard.randomCard()

        # Check for pairs
        if player1 == player2:
            result_frequency["playerPair"] += 1

        if bank1 == bank2:
            result_frequency["bankerPair"] += 1 
        
        # Store the score in variables.
        bankInitial = (getCard.cardToValue(bank1) + getCard.cardToValue(bank2)) % 10
        playerInitial = (getCard.cardToValue(player1) + getCard.cardToValue(player2)) % 10

        # Determine result from tableu.
        result = runHand.baccaratHand(playerInitial, bankInitial)
        
        # Update result_frequency.
        if result["Player"] > result["Banker"]:
            result_frequency["Player"] += 1
        elif result["Banker"] > result["Player"]:
            result_frequency["Banker"] += 1
        elif result["Banker"] == result["Player"]:
            result_frequency["Tie"] += 1

        # Bank wins on 6 condition
        if result["Banker"] == 6 and result["Banker"] > result["Player"]:
            result_frequency["Banker6"] += 1
    
    return result_frequency



def printPercentages(result_frequency):
    playerPercent = getStats.getPercent(result_frequency["Player"], NUMHANDS)
    bankerPercent = getStats.getPercent(result_frequency["Banker"], NUMHANDS)
    banker6Percent = getStats.getPercent(result_frequency["Banker6"], NUMHANDS)
    tiePercent = getStats.getPercent(result_frequency["Tie"], NUMHANDS)
    playerPairPercent = getStats.getPercent(result_frequency["playerPair"], NUMHANDS)
    bankerPairPercent = getStats.getPercent(result_frequency["bankerPair"], NUMHANDS)


    print(f"""
    Player = {playerPercent} / 1 in {getStats.getOccurance(playerPercent)} times
    Banker = {bankerPercent} / 1 in {getStats.getOccurance(bankerPercent)} times
    Bank win on 6 = {banker6Percent} / 1 in {getStats.getOccurance(banker6Percent)} times
    Tie = {tiePercent} / 1 in {getStats.getOccurance(tiePercent)} times
    Player Pair = {playerPairPercent} / 1 in {getStats.getOccurance(playerPairPercent)} times
    Banker Pair = {bankerPairPercent} / 1 in {getStats.getOccurance(bankerPairPercent)} times"""
    )

print(generateHands(result_frequency))
printPercentages(result_frequency)





