# HAND CLASS

from card import Card

class Hand:
	'''
	METHODS:
		- ability to display all the cards in a hand
		- ability to add cards to a sub-array of cards (hand)
		- ability to sum all cards in the hand to produce a value relevant to the game
		- <base class for player and dealer object>

	ATTRIBUTES:
		- sub-array of card objects to be added (smaller than a deck)
	'''
	def __init__(self):
		self.cards = []
		self.sum = 0

	def display_hand(self):
		for i in range(0, len(self.cards)): print("Hand Card #{0}: {1}".format(i + 1, self.cards[i]))

	def hand_sum(self):
		for card in self.cards: self.sum += card.value
		return self.sum

	def add_card(self, new_card):
		self.cards.append(new_card)


if __name__ == "__main__":
	hand = Hand()

	hand.add_card(Card("Diamonds", "Ace"))
	hand.add_card(Card("Clubs", "Eight"))
	hand.add_card(Card("Spades", "Jack"))

	hand.display_hand()

	print("Hand sum: {}".format(hand.hand_sum()))
