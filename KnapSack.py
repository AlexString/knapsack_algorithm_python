from Strategy import Strategy
from Strategy import MaxValueStrategy
from Bag import Bag

class KnapSack():
    
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        self.discarder = 0
        self.criterion_function = None
        self.message = ""

        self.bag = None
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    def getStrategy(self, weight):
        return self._strategy.knapSack(weight)
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def printBagContent(self):
        if self.bag is None:
            print("Error: cannot print total values, try using execute() first")
            return
        self.bag.printBag()

    def execute(self, knapsack_max_weight, items_weight, items_values) -> None:
        def makeDummyArray(length):
            return [0] * length

        if len(items_weight) is not len(items_values):
            print("Error: Discrepancy between items weight length and items values length, does not match.")
            return

        items_length = len(items_weight)

        # Get variables from strategy
        self.message, self.discarder, self.criterion_function = self.getStrategy(items_weight)
        
        dummy_array = makeDummyArray(items_length)
        items_weight_copy = list(items_weight)

        if isinstance(self._strategy, MaxValueStrategy): # it needs to divide values per unit
            items_weight_copy = self._strategy.divideValuesPerUnit(items_values,items_weight)

        current_weight = 0
        final_items_weight_values = list()

        # [ KnapSack alorithm ]
        while( current_weight < knapsack_max_weight ):
            actual_value = self.criterion_function(items_weight_copy) # max/min
            actual_value_position = items_weight_copy.index(actual_value)

            # current weight + the next calculated weight
            future_weight = current_weight + items_weight[actual_value_position]

            # if future weight is still less than the KnapSack max weight:
            if future_weight <= knapsack_max_weight: # Add it and discard that value from the dummy array
                current_weight = future_weight
                dummy_array[actual_value_position] = 1
            else:
                break
            
            # Add the value and discard it.
            final_items_weight_values.append(actual_value)
            items_weight_copy[actual_value_position] = self.discarder

        # Finished algorithm - Now printing results
        total_value = 0
        values_grabbed = list()

        # Using dummy array to get data
        for i in range(len(dummy_array)): 
            if dummy_array[i] != 0:
                values_grabbed.append(items_values[i])
                total_value += items_values[i]

        # Setting data and printing.
        self.bag = Bag(values_grabbed, final_items_weight_values, total_value, current_weight)

        print("Algorithm: '", self.message ,"' has been used. printing now.")
        self.printBagContent()
