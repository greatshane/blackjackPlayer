import random
# blackjack uses 1-13 then * 6 this is 
class Game:
    
    def __init__(self, decks):

        NUM_DECKS = decks
        NUM_STARTING_CARDS = 4
        
        startingHands = random.sample(range(NUM_DECKS*13), NUM_STARTING_CARDS)
        self.dealer = startingHands[0:2]
        self.player = startingHands[2:]
        
        self.remainingCards = set(list(range(NUM_DECKS*13))) - set(startingHands)
        self.remainingCards = list(self.remainingCards)

    def hit(self, dealer):
        #print(self.remainingCards)
        drawnCard = random.choice(self.remainingCards)
        if dealer == 1:
            self.dealer.append(drawnCard)
        else:
            self.player.append(drawnCard)
        self.remainingCards.remove(drawnCard)