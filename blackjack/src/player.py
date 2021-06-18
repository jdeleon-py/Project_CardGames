# PLAYER CLASS

from hand import Hand
from account import Account

class Player(Hand):
	'''
	METHODS:
		- ability to place a bet (deposit/withdraw money from account)
		- ability to control their hand of cards (add card to hand)

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
		return "{}".format(self.name)

	def add_card(self, new_card):
		pass


if __name__ == "__main__":
	pass
