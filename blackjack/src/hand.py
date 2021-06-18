# HAND CLASS

from card import Card

class Hand:
	'''
	METHODS:
		- ability to add cards to a sub-array of cards (hand)
		- ability to sum all cards in the hand to produce a value relevant to the game
		- <possible base class for player and dealer object>

	ATTRIBUTES:
		- sub-array of card objects to be added (smaller than a deck)
	'''
	def __init__(self):
		self.cards = []
		self.sum = 0


	def hand_sum(self):
		for card in self.cards:
			self.sum += card
		return self.sum


	def add_card(self, new_card):
		self.cards.append(new_card)


if __name__ == "__main__":
	pass