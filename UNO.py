from ast import While
import random
import sys
COLOR = ["red", "green", "blue", "yellow"]

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
        
    def show(self):
        val = self.value
        return "{} of {}".format(val, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print (card.show())

    # Generate cards
    def build(self):
        self.cards = []
        for c in COLOR:
            for val in range(1,11):
                self.cards.append(Card(c, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print ("Welcome! {}".format(self.name))
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

    # Display all the cards in the players hand
    def showHand(self):
        print ("{}'s hand: {}".format(self.name, self.hand))
        return self

    def discard(self,where):
        if len (self.hand) < where:
            print ("hand is empty")
        else: 
            return self.hand.pop(where)

if __name__ == "__main__":
    # Test making a Card
    # card = Card('Spades', 6)
    # print card

    # Test making a Deck
    while True:
        print("Would you like to play a game of Uno with the Game Master?")
        play = input("(Y)es or (N)o pussy: ")
        if play == "Y" or play == "yes" or play == "Yes"or play == "y":
            print("choice was yes")
            GameDeck = Deck()
            GameDeck.shuffle()
            #GameDeck.show()
            name = input("Enter your name: ")
            player1 = Player(name)
            player1.sayHello()
            player1.draw(GameDeck, 7)
            player1.showHand()
            player1.discard(2)
            player1.showHand()


            gM = Player("GM")
            gM.draw(GameDeck,7)

            board = Player("board")
            board.draw(GameDeck,1)
            board.showHand()


        else:
            print("What a Pussy!")
            sys.exit()
    
