# knapsack algorithm in python

This script handles the Knapsack problem with the 3 modes:

- Considering maximum weight values.
- Considering minimum weight values.
- Considering max values.

Also, [@DieGopherLT](https://github.com/DieGopherLT) implemented the Strategy pattern.

# Quick view:

## **Strategy.py**
```python
from abc import ABC, abstractmethod

# The Strategy interface declares operations common to all supported versions of some algorithm.
class Strategy(ABC):
    
    @abstractmethod
    def knapSack(self, weight = None):
        pass

# This a concrete interface that implements Strategy
class MinStrategy(Strategy):
    def knapSack(self, it_w):
        return "mininum", max(it_w) + 1000, min

# Another concrete Strategy that implements it
class MaxStrategy(Strategy):
    def knapSack(self, it_w):
        return "maximum", -1, max

# Third algorithm mode in a Strategy
class MaxValueStrategy(Strategy):
    def divideValuesPerUnit(self, list_values, list_weights):
        auxiliar_list = list()
        for i in range(len(list_values)):
            auxiliar_list.append(list_values[i]/list_weights[i])
            # You can convert the values to int, instead of float
            #auxiliar_list.append(int(list_values[i]/list_weights[i]))
        return auxiliar_list

    def knapSack(self, it_w):
        return "max value per unit", -1, max
```

## **KnapSack.py**
This class uses the strategy to change functions in the code. Is the main class to operate with the Strategy given into like in *main.py*

```python
# Destructuring the strategy to use.
self.message, self.discarder, self.knapSackCriterion = self._strategy.knapSack(it_w)
```
## **main.py**
```python
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

	print("\nItems values:")
	print(items_values)

	print("\n")

	# You can switch between using MinStrategy / MaxStrategy / MaxValueStrategy
	knapSack = KnapSack(MaxValueStrategy())
	knapSack.execute(knapSack_MaximumWeight, items_weight, items_values)

Main()
```
## **Bag.py**
It stores the items and provides a method to print them.


```python
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
```