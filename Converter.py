class Converter:
    
    def convert(hand):
        modded = [(i%13)+1 for i in hand]
        cards = []
        for x in modded:
            if x == 1:
                cards.append('A')
            elif x == 11:
                cards.append('J')
            elif x == 12:
                cards.append('Q')
            elif x == 13:
                cards.append('K')
            else:
                cards.append(x)
        return cards
    
    def handCount(cards):
        possibleHands = []
        for x in cards:
            # If the card is 2-10
            if isinstance(x, int):
                if len(possibleHands) == 0:
                    possibleHands.append(x)
                else:
                    possibleHands = [i+x for i in possibleHands]
                
            # If the card is J, Q, K
            elif x == 'J' or x == 'Q' or x == 'K':
                if len(possibleHands) == 0:
                    possibleHands.append(10)
                else:
                    possibleHands = [i+10 for i in possibleHands]
                
            # If the card is A
            else:
                if len(possibleHands) == 0:
                    possibleHands.extend([1, 11])
                else:
                    tempList = []
                    for i in possibleHands:
                        tempList.append(i+1)
                        tempList.append(i+11)
                    possibleHands = tempList
                
        possibleHands = list(set(possibleHands))
        
        return possibleHands

                

