# Game Interface
# Add monte_carlo features to CLI class
#	- if monte_carlo in init() member: add counters and stats

import time
from deck import Deck
from player import Player

class CLI:
	NUM_CARDS_WAR = 3

	def __init__(self, elapsed_time, monte_carlo):
		self.elapsed_time = elapsed_time
		self.monte_carlo = monte_carlo
		self.iteration = 0

		self.deck = Deck()
		self.deck.shuffle()

		self.player1_deck = self.deck.deck[: int(len(self.deck.deck) / 2)]
		self.player2_deck = self.deck.deck[int(len(self.deck.deck) / 2) :]

		self.player1 = Player("Player 1", self.player1_deck)
		self.player2 = Player("Player 2", self.player2_deck)

		if self.monte_carlo:
			pass

	def run(self):
		while True:
			self.iteration += 1
			print("iteration: {}".format(self.iteration))
			print("------------------------------------------------------------------")
			print('\n')
			print("------------------------------------------------------------------")
			time.sleep(self.elapsed_time)

			if len(self.player1.deck_of_cards) == 0: 
				print("{} wins!".format(self.player2))
				break

			elif len(self.player2.deck_of_cards) == 0: 
				print("{} wins!".format(self.player1))
				break

			else:
				dealt_card1 = self.player1.deal_card()
				dealt_card2 = self.player2.deal_card()
				print("{0} vs. {1}".format(dealt_card1, dealt_card2))

				if dealt_card1 > dealt_card2:
					self.player1.add_card(dealt_card1)
					self.player1.add_card(dealt_card2)
					print("{0} wins this round with {1} cards now in their deck!".format(self.player1, len(self.player1_deck)))
					print("{0} lost this round with {1} cards now in their deck!".format(self.player2, len(self.player2_deck)))
					continue

				elif dealt_card1 < dealt_card2:
					self.player2.add_card(dealt_card1)
					self.player2.add_card(dealt_card2)
					print("{0} lost this round with {1} cards now in their deck!".format(self.player1, len(self.player1_deck)))
					print("{0} wins this round with {1} cards now in their deck!".format(self.player2, len(self.player2_deck)))
					continue

				else: #dealt_card1 == dealt_card2
					if len(self.player1.deck_of_cards) <= CLI.NUM_CARDS_WAR:
						print("{} wins!".format(self.player2))
						break

					elif len(self.player2.deck_of_cards) <= CLI.NUM_CARDS_WAR:
						print("{} wins!".format(self.player1))
						break

					else:
						print("WAR!")
						cards1 = [self.player1.deal_card() for _ in range(0, CLI.NUM_CARDS_WAR)]
						cards2 = [self.player2.deal_card() for _ in range(0, CLI.NUM_CARDS_WAR)]

						det_card1 = self.player1.deal_card()
						det_card2 = self.player2.deal_card()
						print("{0} vs. {1}".format(det_card1, det_card2))

						if det_card1 > det_card2:
							for card in cards1: self.player1.add_card(card)
							for card in cards2: self.player1.add_card(card)
							self.player1.add_card(det_card1)
							self.player1.add_card(det_card2)
							self.player1.add_card(dealt_card1)
							self.player1.add_card(dealt_card2)
							print("{0} wins this round with {1} cards now in their deck!".format(self.player1, len(self.player1_deck)))
							print("{0} lost this round with {1} cards now in their deck!".format(self.player2, len(self.player2_deck)))
							continue

						elif det_card1 < det_card2:
							for card in cards1: self.player2.add_card(card)
							for card in cards2: self.player2.add_card(card)
							self.player2.add_card(det_card1)
							self.player2.add_card(det_card2)
							self.player2.add_card(dealt_card1)
							self.player2.add_card(dealt_card2)
							print("{0} lost this round with {1} cards now in their deck!".format(self.player1, len(self.player1_deck)))
							print("{0} wins this round with {1} cards now in their deck!".format(self.player2, len(self.player2_deck)))
							continue

						else: #det_card1 == det_card2 -> DRAW!
							for card in cards1: self.player1.add_card(card)
							for card in cards2: self.player2.add_card(card)
							self.player1.add_card(det_card1)
							self.player2.add_card(det_card2)
							self.player1.add_card(dealt_card1)
							self.player2.add_card(dealt_card2)
							print("Draw! Continuing game!")
							continue

if __name__ == "__main__":
	game = CLI(0.1)
	game.run()
