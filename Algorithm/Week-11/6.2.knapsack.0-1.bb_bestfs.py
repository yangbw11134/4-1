from heapq import heappush, heappop
from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
        # Complete the code here
        totweight = u.weight
        bound = u.profit
        j = u.level + 1
        while(j <= n and totweight + w[j] <= W):
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if(k<=n):
            bound = bound + (W-totweight) * p[k] / w[k]
        
        return bound

def knapsack3(n: int, W: float, w: List[float], p: List[float]) -> float:
    count = 0
    heap = [] # Initialize Priority Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    heappush(heap, (-v.bound, v))
    count +=1
    while len(heap) != 0:
        # Complete the code here
        Node.__lt__ = lambda self, other: False
        item = heappop(heap)
        v = item[-1]

        if(v.bound > maxprofit):
            u = Node(v.level + 1, v.weight + w[v.level+1], v.profit + p[v.level+1])
            if(u.weight <= W and u.profit > maxprofit):
                maxprofit = u.profit

            u.bound = boundof(u, n, W, w, p)
            if(u.bound > maxprofit):
                heappush(heap, (-u.bound, u))
            
            u = Node(v.level + 1, v.weight, v.profit)

            u.bound = boundof(u, n, W, w, p)
            if(u.bound > maxprofit):
                heappush(heap, (-u.bound, u))

    return maxprofit
