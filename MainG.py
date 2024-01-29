from Game import Game
from Score import Score
from Converter import Converter
import time

def main():
    startingMoney = input("Select starting money in $: ")
    defaultbid = input("Select starting bid (default is $10): ")
    if len(defaultbid) == 0:
        score = Score(int(startingMoney))
    else:
        score = Score(int(startingMoney), int(defaultbid))
    mainHelper(score)


def mainHelper(score):
    game = Game(6)
    bust = False
    # print(game.player)
    # print(game.dealer)
    startP = Converter.convert(game.player)
    playerHC = max(Converter.handCount(startP))
    startD = Converter.convert(game.dealer)
    dealerHC = max(Converter.handCount(startD))
    joinedS = ' '.join([f'{item}  ' for item in startP])
    print(f"You have a\n\n {joinedS} \n")

    print(f"Dealer shows a\n\n {startD[0]}\n")
    if playerHC == 21 and dealerHC == 21:
        pPush(score)
        return
    elif playerHC == 21:
        pWin(score)
        return
    elif dealerHC == 21:
        joinedD = ' '.join([f'{item}  ' for item in startD])
        print(f"Dealer shows a\n\n {joinedD}\n")
        pLose(score)
        return
    while (True):
        choice = input("Make your choice (hit/stand/double) ")

        if choice == "hit":
            hit(game, 0)
            if busted(game, 0):
                pLose(score)
                return
        elif choice == "double":
            score.double()
            hit(game, 0)
            if busted(game, 0):
                pLose(score)
                return
            break

        else:
            break

    # Now dealer's turn
    
    bust = dealer(game)
    if bust == True:
        # Dealer busted here.. so player win
        pWin(score)
        return
    else:
        playerHand = Converter.convert(game.player)
        playerHC = Converter.handCount(playerHand)
        playerHC = [x for x in playerHC if x<=21]
        maxPlayer = min(playerHC, key=lambda x:abs(x-21))
        dealerHand = Converter.convert(game.dealer)
        dealerHC = Converter.handCount(dealerHand)
        dealerHC = [x for x in dealerHC if x<=21]
        maxDealer = min(dealerHC, key=lambda x:abs(x-21))
        if maxPlayer < maxDealer:
            pLose(score)
        elif maxPlayer == maxDealer:
            pPush(score)
        else:
            pWin(score)

    # print(Converter.convert(game.dealer))

def hit(game, dealer):
    game.hit(dealer=dealer)
    if dealer:
        time.sleep(2)
        startD = Converter.convert(game.dealer)
        joinedD = ' '.join([f'{item}  ' for item in startD])
        print(f"Dealer shows a\n\n {joinedD}\n")
        
    else:
        startP = Converter.convert(game.player)
        joinedS = ' '.join([f'{item}  ' for item in startP])
        print(f"You have a \n\n{joinedS} \n")
    


def busted(game, dealer):
    if dealer:
        dealerHand = Converter.convert(game.dealer)
        minValue = Converter.handCount(dealerHand)
        if min(minValue) > 21 and max(minValue) > 21:
            return True
        return False
    else:
        playerHand = Converter.convert(game.player)
        minValue = Converter.handCount(playerHand)
        if min(minValue) > 21 and max(minValue) > 21:
            startD = Converter.convert(game.dealer)
            joinedD = ' '.join([f'{item}  ' for item in startD])
            print(f"Dealer had a\n\n {joinedD}\n")
            return True
        return False
    
def dealer(game):
    
    dealerHand = Converter.convert(game.dealer)
    minValue = Converter.handCount(dealerHand)
    joinedD = ' '.join([f'{item}  ' for item in dealerHand])
    print(f"Dealer shows a \n\n{joinedD} \n")
    # This is for dealer hits soft 17???
    # 13 23 -> hit
    # 8 18 -> stand
    # 7 17 -> hit
    while max(minValue) < 17 or (max(minValue) > 21 and min(minValue) < 17):
        hit(game, 1)
        if busted(game, 1):
            return True
        dealerHand = Converter.convert(game.dealer)
        minValue = Converter.handCount(dealerHand)
    return False

def playAgain(score):
    userP = input("\nDo you want to play again? (y/n) \n")
    if userP == 'y':
        changeBid = input("\nEnter new bid (or not to keep as last) \n")
        if len(changeBid) != 0:
            score.changeBid(int(changeBid))
        mainHelper(score)
    else:
        return
    
def pWin(score):
    print("You WIN!!")
    score.win()
    print(f"You now have: {score.currentMoney}")
    playAgain(score)

def pPush(score):
    print("You PUSHED!!")
    score.push()
    print(f"You now have: {score.currentMoney}")
    playAgain(score)

def pLose(score):
    print("You LOSE!!")
    endGame = score.lose()
    print(f"You now have: {score.currentMoney}")
    if endGame:
        print("GAME OVER. You ran out of money :(")
        return
    playAgain(score)


if __name__ == "__main__":
    main()