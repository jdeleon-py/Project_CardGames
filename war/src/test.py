# Basic logic of the card game "War"
# only outputs whether a player has won

from deck import Deck
from player import Player


if __name__ == "__main__":
	deck = Deck()
	deck.shuffle()

	player1_deck = deck.deck[: int(len(deck.deck) / 2)]
	player2_deck = deck.deck[int(len(deck.deck) / 2) :]

	player1 = Player("Player 1", player1_deck)
	player2 = Player("Player 2", player2_deck)

	while True:
		if len(player1.deck_of_cards) == 0: 
			print("{} wins!".format(player2))
			break

		elif len(player2.deck_of_cards) == 0: 
			print("{} wins!".format(player1))
			break

		else:
			dealt_card1 = player1.deal_card()
			dealt_card2 = player2.deal_card()

			if dealt_card1 > dealt_card2:
				player1.add_card(dealt_card1)
				player1.add_card(dealt_card2)
				continue

			elif dealt_card1 < dealt_card2:
				player2.add_card(dealt_card1)
				player2.add_card(dealt_card2)
				continue

			else: #dealt_card1 == dealt_card2
				if len(player1.deck_of_cards) <= 3:
					print("{} wins!".format(player2))
					break

				elif len(player2.deck_of_cards) <= 3:
					print("{} wins!".format(player1))
					break

				else:
					cards1 = [player1.deal_card() for _ in range(0, 3)]
					cards2 = [player2.deal_card() for _ in range(0, 3)]

					det_card1 = player1.deal_card()
					det_card2 = player2.deal_card()

					if det_card1 > det_card2:
						for card in cards1: player1.add_card(card)
						for card in cards2: player1.add_card(card)
						player1.add_card(det_card1)
						player1.add_card(det_card2)
						player1.add_card(dealt_card1)
						player1.add_card(dealt_card2)
						continue

					elif det_card1 < det_card2:
						for card in cards1: player2.add_card(card)
						for card in cards2: player2.add_card(card)
						player2.add_card(det_card1)
						player2.add_card(det_card2)
						player2.add_card(dealt_card1)
						player2.add_card(dealt_card2)
						continue

					else: #det_card1 == det_card2
						for card in cards1: player1.add_card(card)
						for card in cards2: player2.add_card(card)
						player1.add_card(det_card1)
						player2.add_card(det_card2)
						player1.add_card(dealt_card1)
						player2.add_card(dealt_card2)
						continue
