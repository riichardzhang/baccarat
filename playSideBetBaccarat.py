# Commission Baccarat session with only main bets.
# House takes 5% commission from winning Bank bet.

import random
import getCard
import runHand

BANKROLL = 0
NUMHANDS = 1000000

MAIN_BET_SIZE = 25

LOSE = 0
PLAYER_WIN = 1
BANKER_WIN = 2
TIE = 3

def playHand():
    # Generate cards
    bank1 = getCard.randomCard()
    bank2 = getCard.randomCard()
    player1 = getCard.randomCard()
    player2 = getCard.randomCard()
    
    bankInitial = (getCard.cardToValue(bank1) + getCard.cardToValue(bank2)) % 10
    playerInitial = (getCard.cardToValue(player1) + getCard.cardToValue(player2)) % 10

    result = runHand.baccaratHand(playerInitial, bankInitial)

    if result["Banker"] == result["Player"]:
        return TIE


def playSession(bet_size):
    global BANKROLL
    for hand in range(NUMHANDS):
        result = playHand()

        if result == TIE:
            BANKROLL += (bet_size * 8)
        else:
            BANKROLL -= bet_size


playSession(MAIN_BET_SIZE)
print(f"Net win/loss after {NUMHANDS} tie bets @ ${MAIN_BET_SIZE} bets = {BANKROLL}")
print(f"Average cost per hand {BANKROLL/NUMHANDS}")