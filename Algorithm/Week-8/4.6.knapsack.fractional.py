from heapq import heappush, heappop
from typing import List, Tuple

class Item:
    def __init__(self, id: int, weight: float, profit: float) -> None:
        self.id: int = id
        self.weight: float = weight
        self.profit: float = profit
        self.profit_per_weight: float = profit / weight
        
def knapsack(n: int, W: float, w: List[float], p: List[float]) -> float:
    heap: List[Tuple[float, Item]] = []
    for i in range(n):
        item: Item = Item(i + 1, w[i], p[i])  # type: ignore
        heappush(heap, (-item.profit_per_weight, item))
    maxprofit: float = 0.0
    total_weight: float = 0.0

    # Complete the code here

    for i in range(n):
        p = heappop(heap)
        if(W >= total_weight + p[1].weight):
            total_weight += p[1].weight
            maxprofit += p[1].profit
        else:
            if(W >= total_weight + 1):
                for j in range(p[1].weight):
                    if(W >= total_weight + 1):
                        total_weight += 1
                        maxprofit += -p[0]
            else:
                break
                
    return maxprofit