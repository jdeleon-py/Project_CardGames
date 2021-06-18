# DEALER CLASS

from deck import Deck
from hand import Hand

class Dealer(Hand):
	'''
	METHODS:
		- ability to deal a card
		- ability to add a card to their hand

	ATTRIBUTES:
		- deck of cards to deal to itself and player
		- (inherited) hand of cards
	'''
	def __init__(self):
		super().__init__(self)
		self.deck = Deck()
	

	def deal_card(self):
		pass



if __name__ == "__main__":
	pass