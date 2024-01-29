class Score:
    
    def __init__(self, startMoney, bid=10):
        self.currentMoney = startMoney
        self.currentBid = bid
        self.currentDefault = bid

    def win(self):
        self.currentMoney += self.currentBid
        self.currentBid = self.currentDefault

    def push(self):
        self.currentBid = self.currentDefault

    def lose(self):
        self.currentMoney -= self.currentBid
        self.currentBid = self.currentDefault
        if self.currentMoney <= 0:
            return True

    def double(self):
        self.currentBid *= 2

    def changeBid(self, newBid):
        self.currentDefault = newBid
        self.currentBid = self.currentDefault





