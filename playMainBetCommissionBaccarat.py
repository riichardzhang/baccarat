# Commission Baccarat session with only main bets.
# House takes 5% commission from winning Bank bet.

import random
import getCard
import runHand

BANKROLL = 0
NUMHANDS = 1000000

MAIN_BET_SIZE = 100

LOSE = 0
PLAYER_WIN = 1
BANKER_WIN = 2
TIE = 3

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
    
    if result["Player"] > result["Banker"] and mainBet == 0:
        return PLAYER_WIN
    elif result["Player"] > result["Banker"] and mainBet == 1:
        return LOSE
    elif result["Banker"] > result["Player"] and mainBet == 0:
        return LOSE
    elif result["Banker"] > result["Player"] and mainBet == 1:
        return BANKER_WIN
    elif result["Banker"] == result["Player"]:
        return TIE

def playSession(bet_size):
    global BANKROLL
    for hand in range(NUMHANDS):
        result = playHand()

        if result == LOSE:
            BANKROLL -= bet_size
        elif result == PLAYER_WIN:
            BANKROLL += bet_size
        elif result == BANKER_WIN:
            BANKROLL += (bet_size * 0.95)


playSession(MAIN_BET_SIZE)
print(f"Net win/loss after {NUMHANDS} commission hands @ ${MAIN_BET_SIZE} bets = {BANKROLL}")
print(f"Average cost per hand {BANKROLL/NUMHANDS}")












