import random
import sys

COLOR = ["Red", "Green", "Blue", "Yellow"]

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        return "{} of {}".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for c in COLOR:
            for val in range(1, 11):  # Using numbers 1-10 for simplicity
                self.cards.append(Card(c, val))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def showHand(self):
        for card in self.hand:
            print(card.show())

    def playCard(self, cardIndex):
        if cardIndex >= 0 and cardIndex < len(self.hand):
            return self.hand.pop(cardIndex)
        else:
            return None

def main():
    print("Welcome to the Uno-like Game!")

    deck = Deck()
    player1 = Player(input("Enter Player 1's name: "))
    player2 = Player("Game Master")  # Automated opponent

    # Initial draw
    player1.draw(deck, 7)
    player2.draw(deck, 7)

    currentPlayer = player1
    otherPlayer = player2

    while True:
        print(f"\n{currentPlayer.name}'s turn.")
        currentPlayer.showHand()

        cardPlayed = False
        while not cardPlayed:
            playerInput = input("Choose a card to play (1-{}), or 'draw' to draw a card: ".format(len(currentPlayer.hand)))
            if playerInput.lower() == 'draw':
                currentPlayer.draw(deck, 1)
                currentPlayer.showHand()
            else:
                try:
                    cardIndex = int(playerInput) - 1  # Adjust for 0-index
                    if 0 <= cardIndex < len(currentPlayer.hand):
                        card = currentPlayer.playCard(cardIndex)
                        print(f"{currentPlayer.name} played {card.show()}")
                        cardPlayed = True
                except ValueError:
                    print("Invalid input, please try again.")

        # Check win condition
        if len(currentPlayer.hand) == 0:
            print(f"\n{currentPlayer.name} wins!")
            break

        # Switch players
        currentPlayer, otherPlayer = otherPlayer, currentPlayer

if __name__ == "__main__":
    main()
