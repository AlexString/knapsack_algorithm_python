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
    def knapSack(self):
        return "maximum", -1, max