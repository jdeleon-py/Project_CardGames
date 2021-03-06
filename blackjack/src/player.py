# PLAYER CLASS

from hand import Hand
from account import Account

class Player(Hand):
	'''
	METHODS:
		- ability to place a bet (deposit/withdraw money from account)
		- ability to control their hand of cards (add card to hand)
		- <can call player.add_card() since it is inherited from Hand object>

	ATTRIBUTES:
		- name ("Player")
		- (inherited) hand of cards
		- bank account
	'''
	def __init__(self, name):
		Hand.__init__(self)
		self.name = name
		self.account = Account(self.name, 1000)

	def __str__(self):
		return '{}'.format(self.account)

	def place_bet(self):
		bet_input = int(input("Enter an amount you want to bet: "))
		print('{}'.format(self.account.withdraw(bet_input)))


if __name__ == "__main__":
	player = Player("Player")

	# if testing for adding cards to hand, see dealer.py

	# place bets
	for _ in range(0, 3):
		player.place_bet()
		print('{}\n'.format(player))
