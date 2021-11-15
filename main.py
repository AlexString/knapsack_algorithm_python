"""
File: .py
Author: AlexString
Description:
Algorithm that simply implements the knapsack problem with maximum and minimum weight criterion.
"""

from KnapSack import KnapSack
from Strategy import MinStrategy, MaxStrategy, MaxValueStrategy

def Main():
	# VALUES HERE
	knapSack_MaximumWeight = 100
	items_weight = [10,20,30,40,50] 
	items_values = [20,30,66,40,60] 

	# Printing items data
	print("Items weight:")
	print(items_weight)

	print("Items values:")
	print(items_values)

	print("\n\n")

	# You can switch between using MinStrategy / MaxStrategy / MaxValueStrategy
	knapSack = KnapSack(MaxValueStrategy())
	knapSack.execute(knapSack_MaximumWeight, items_weight, items_values)

Main()