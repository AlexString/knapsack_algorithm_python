from abc import ABC, abstractmethod

class Strategy(ABC):
    
    @abstractmethod
    def knapSack(self):
        pass

class MinStrategy(Strategy):
    def knapSack(self):
        return super().knapSack()
    
class MaxStrategy(Strategy):
    def knapSack(self):
        return super().knapSack()