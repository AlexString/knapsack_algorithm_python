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