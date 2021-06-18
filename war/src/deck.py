# Deck class

import random
from card import Card

class Deck:
	SUIT = ["Spades", "Hearts", "Clubs", "Diamonds"]
	RANK = ["Two", "Three", "Four", "Five", "Six", "Seven",
			"Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

	def __init__(self):
		self.deck = [Card(suit, rank) for rank in Deck.RANK for suit in Deck.SUIT]

	def shuffle(self):
		return random.shuffle(self.deck)

	def deal_card(self):
		return self.deck.pop(0)


if __name__ == "__main__":
	new_deck = Deck()
	new_deck.shuffle()

	for i in range(0, 3): print("Card #{0}: {1}".format(i + 1, new_deck.deal_card()))
	print("\n")
	print("{} cards left in the deck!".format(len(new_deck.deck)))
