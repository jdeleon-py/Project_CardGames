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
		Hand.__init__(self)
		self.deck = Deck()
	

	def deal_card(self):
		return self.deck.deck.pop(0)


if __name__ == "__main__":
	dealer = Dealer()

	# Three random cards are dealt
	for i in range(0, 3): print("Card #{0}: {1}".format(i + 1, dealer.deal_card()))

	# Dealer deals cards that are then added to their own hand
	dealer.add_card(dealer.deal_card())
	dealer.add_card(dealer.deal_card())
	dealer.add_card(dealer.deal_card())

	# Cards in hand are displayed
	dealer.display_hand()
