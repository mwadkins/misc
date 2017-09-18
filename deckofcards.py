from random import shuffle

class card():
    suit=""
    name=""
    value=0
    
    def __init__(self,s,v,n):
        self.suit=s
        self.value=v
        self.name=n
    def __str__ (self):
        return self.name + " of " + self.suit + " value=" + str(self.value)
        
class deck():
    
    cards=[]
    
    def __init__ (self):
        for i in range (2,11):
            for suit in ("spades","diamonds","hearts","clubs"):
                c = card (suit,i,str(i))
                self.cards.append(c)
        for i in  ("ace","jack","queen","king"):
            for suit in ("spades","diamonds","hearts","clubs"):
                c = card (suit,10,i)
                self.cards.append(c)
        self.top=0
                
    def printdeck (self):
        for i in self.cards:
            print i

    def shuffledeck (self):
        shuffle(self.cards)
        self.top=0

    def getcard (self):
        if (self.top==len(self.cards)-1):
            self.shuffledeck
        card=self.cards[self.top]
        self.top+=1
        return card
    
class hand:
    myhand=[]

    def add_card(self,c):
        self.myhand.append(c)

    def get_count(self):
        tot=0
        for c in self.myhand:
            #fixme: handle ace
            tot+= myhand[c].value()
        return tot
    
    def hit (self):
        tot=self.get_count()
        if (tot <18):
            return True
        return False

    def reset(self):
        self.myhand=[]

    def __str__(self):
        for i in len(self.myhand):
            ret+=str(self.myhand[i]) + " "
        return ret
        
class cardgame():
    scores=[]
    num_players=0
    deck=None
    
    def __init__(self,num_players):
        self.num_players=num_players
        for i in range(num_players):
            self.scores.append(0)
        self.deck=deck()

                
class blackjack(cardgame):
    def __init__(self,num_players):
        cardgame.__init__(self,num_players)

    def play(self,num_rounds):
        hands = [None for i in range(self.num_players)]
        for i in range(num_rounds):
            # deal two cards to each player
            for i in range (self.num_players):
                for j in range (0,2):
                    hands[i]=hand()
                    hands[i].add_card(self.deck.getcard())
            # ask each player if they want to hit or stay
            for i in range (self.num_players):
                while (hands[i].hit()):
                    hands[i].add_card(self.deck.getcard())
            # find winners
            max=0
            for i in range (self.num_players):
                count=hands[i].get_count()
                if ((count>max) and (count<=21)):
                    max=count
                    scores.append(count)
                print hands[i]
                
            for i in range (self.num_players):
                if (scores[i]==max):
                    print "player ",i," is a winner.  Score=",max
                    
            # collect cards
            for i in range (self.num_players):
                hands[i].reset()
        


b=blackjack(4)
b.play(1)
