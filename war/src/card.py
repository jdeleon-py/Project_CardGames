# Card class

class Card:
	VALUE = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
			"Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = Card.VALUE[self.rank]

	def __str__(self):
		return "{0} of {1}".format(self.rank, self.suit)

	def __eq__(self, card):
		return self.value == card.value

	def __gt__(self, card):
		return self.value > card.value

	def __lt__(self, card):
		return self.value < card.value


if __name__ == "__main__":
	cards = [Card("Hearts", "Queen"), Card("Diamonds", "Ace"), Card("Clubs", "Three")]

	for i in range(0, len(cards)): print("Card #{0}: {1}".format(i + 1, cards[i]))
	print("\n")
	for i in range(0, len(cards)): print("Value of Card #{0}: {1}".format(i + 1, cards[i].value))

	if   cards[1] > cards[0]:  print("Card 2 is greater than Card 1")
	elif cards[1] < cards[0]:  print("Card 2 is less than Card 1")
	elif cards[1] == cards[0]: print("Card 2 is equal to Card 1")
	else: pass
