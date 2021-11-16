class Bag():
	def __init__(self, values, weights, t_value, t_weight):
		self.Values = values
		self.Weights = weights

		self.totalValue = t_value
		self.totalWeight = t_weight

	def printBag(self):
		print("** VALUES **")
		print(self.Values)

		print("\n -- Total value: ", self.totalValue, "\n")

		print("** WEIGHTS **")
		print(self.Weights)

		print("\n -- Total weight: ", self.totalWeight, "\n")
		