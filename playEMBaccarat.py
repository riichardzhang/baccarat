import random
import getCard
import runHand

BANKROLL = 0
NUMHANDS = 100000

MAIN_BET_SIZE = 100

WIN = 1
LOSE = 0
TIE = 2
BANK_WIN_6 = 3

def playHand():
    # 0 for player, 1 for bank
    player_or_bank = [0, 1]

    # Randomise bet choice
    mainBet = random.choice(player_or_bank)

    # Generate cards
    bank1 = getCard.randomCard()
    bank2 = getCard.randomCard()
    player1 = getCard.randomCard()
    player2 = getCard.randomCard()
  
    bankInitial = (getCard.cardToValue(bank1) + getCard.cardToValue(bank2)) % 10
    playerInitial = (getCard.cardToValue(player1) + getCard.cardToValue(player2)) % 10

    result = runHand.baccaratHand(playerInitial, bankInitial)

    if (result["Banker"] == 6 and result["Banker"] > result["Player"]) and mainBet == 1:
        return BANK_WIN_6
    
    if result["Player"] > result["Banker"] and mainBet == 0:
        return WIN
    elif result["Player"] > result["Banker"] and mainBet == 1:
        return LOSE
    elif result["Banker"] > result["Player"] and mainBet == 0:
        return LOSE
    elif result["Banker"] > result["Player"] and mainBet == 1:
        return WIN
    elif result["Banker"] == result["Player"]:
        return TIE

def playSession(bet_size):
    global BANKROLL
    for hand in range(NUMHANDS):
        result = playHand()

        if result == LOSE:
            BANKROLL -= bet_size
        elif result == WIN:
            BANKROLL += bet_size
        elif result == BANK_WIN_6:
            BANKROLL += bet_size/2



playSession(MAIN_BET_SIZE)
print(BANKROLL)









