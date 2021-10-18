from Strategy import Strategy

class KnapSack():
    
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        self.discarder = 0
        self.knapSackCriterion = 0
        
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
        
    def execute(self, KW, it_w, it_v) -> None:
        pass