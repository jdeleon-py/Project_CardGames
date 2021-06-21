# DECK CLASS

import random
from card import Card

class Deck:
	'''
	METHODS:
		- ability to randomly shuffle the array of card objects

	ATTRIBUTES:
		- array of card objects (every combination of card objects)
	'''
	SUIT = ["Spades", "Hearts", "Clubs", "Diamonds"]
	RANK = ["Two", "Three", "Four", "Five", "Six", "Seven",
			"Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

	def __init__(self):
		self.deck = [Card(suit, rank) for rank in Deck.RANK for suit in Deck.SUIT]
		self.shuffle()


	def shuffle(self):
		return random.shuffle(self.deck)


if __name__ == "__main__":
	new_deck = Deck()

	for i in range(0, 30): print("Card #{0}: {1}".format(i + 1, new_deck.deck[i]))
