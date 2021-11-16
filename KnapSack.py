from Strategy import Strategy
from Strategy import MaxValueStrategy
from Bag import Bag

class KnapSack():
    
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        self.discarder = 0
        self.knapSackCriterion = None
        self.message = ""

        self.bag = None
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def printData(self):
        if self.bag is None:
            print("Error: cannot print total values, try using execute() first")
            return
        self.bag.printBag()

    def execute(self, KW, it_w, it_v) -> None:
        if len(it_w) is not len(it_v):
            print("Error: Discrepancy between items weight length and items values length, does not match.")
            return

        it_n = len(it_w)
        self.message, self.discarder, self.knapSackCriterion = self._strategy.knapSack(it_w)
        
        dummy_array = [0] * it_n # Creating an array of it_n length filled with 0's
        dummy_weightArray = list(it_w) # Using a copy of the it_w array

        # If Strategy is MaxValueStrategy it needs to divide values per unit
        if isinstance(self._strategy, MaxValueStrategy):
            dummy_weightArray = self._strategy.divideValuesPerUnit(it_v,it_w)

        current_weight = 0
        final_weight_values_list = list() # Final values will end in this list

        # [ KnapSack alorithm ]
        while( current_weight < KW ):
            actual_value = self.knapSackCriterion(dummy_weightArray) # Using criterion from KnapSack algorithm
            actual_value_position = dummy_weightArray.index(actual_value) # Getting value position

            # If the current weight + the next calculated item is still less than the KnapSack weight:
            if (current_weight + it_w[actual_value_position]) <= KW:
                current_weight += it_w[actual_value_position]
                dummy_array[actual_value_position] = 1
            else:
                break
            
            final_weight_values_list.append(actual_value) # Adding it to array
            dummy_weightArray[actual_value_position] = self.discarder # Discard that value

        # Finished algorithm - Now printing results
        total_value = 0
        values_grabbed = list()

        for i in range(len(dummy_array)): # Getting data from auxiliar dummy_array
            if dummy_array[i] != 0:
                values_grabbed.append(it_v[i])
                total_value += it_v[i]

        # Finished algorithm - setting data, printing at last.
        self.bag = Bag(values_grabbed, final_weight_values_list, total_value, current_weight)
        print("Algorithm: '", self.message ,"' has been used. printing now.")
        self.printData()
