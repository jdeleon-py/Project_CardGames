# ACCOUNT CLASS

class Account:
	'''
	METHODS:
		- ability to represent an account object as its name and balance
		- ability to deposit a value to the balance
		- ability to withdraw a valid value from the balance

	ATTRIBUTES:
		- name on the account
		- starting balance of the account 
		- (a future implementation will save the balance to a file and loaded when the game starts)
	'''
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance


	def __str__(self):
		return "Account Name: {0}; Account Balance: {1}".format(self.name, self.balance)


	def deposit(self, amount):
		self.balance += amount
		return "Deposit accepted!"


	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			return "Withdraw accepted!"
		return "Withdraw not accepted!"


if __name__ == "__main__":
	pass