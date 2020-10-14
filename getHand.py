import runHand
import getCard

result_frequency = {
    "Player": 0,
    "Banker": 0,
    "Tie": 0
}

for i in range(100000):
    bankInitial = (getCard.randomCard() + getCard.randomCard()) % 10
    playerInitial = (getCard.randomCard() + getCard.randomCard()) % 10

    result = runHand.baccaratHand(playerInitial, bankInitial)
    
    if result["Player"] > result["Banker"]:
        result_frequency["Player"] += 1
    elif result["Banker"] > result["Player"]:
        result_frequency["Banker"] += 1
    elif result["Banker"] == result["Player"]:
        result_frequency["Tie"] += 1

print(result_frequency)