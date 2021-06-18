# Player class

from deck import Deck

class Player:
	def __init__(self, name, deck_of_cards):
		self.name = name
		self.deck_of_cards = deck_of_cards

	def __str__(self):
		return "{}".format(self.name)

	def add_card(self, new_card):
		return self.deck_of_cards.append(new_card)

	def deal_card(self):
		return self.deck_of_cards.pop(0)


if __name__ == "__main__":
	deck = Deck()
	deck.shuffle()

	player1_deck = deck.deck[: int(len(deck.deck) / 2)]  # player gets half of a standard deck
	player = Player("Player 1", player1_deck)

	for i in range(0, 13): print("Dealt card #{0}: {1}".format(i + 1, player.deal_card()))

	dealt_card = player.deal_card()
	print("Dealt card to be added back into the deck: {0}".format(dealt_card))

	player.add_card(dealt_card)
	print("Newly added card at the end of the deck: {0}".format(player.deck_of_cards[-1]))
