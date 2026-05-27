from typing import List

def partition(low: int, high: int, S: List[int]) -> int:
    pivotitem = S[low]
    j = low

    # Complete the code here
    for i in range(low+1, high+1):
        if(pivotitem > S[i]):
            j = j + 1
            value = S[j]
            S[j] = S[i]
            S[i] = value
    pivotpoint = j
    value = pivotitem
    S[low] = S[j]
    S[j] = value

    return pivotpoint

def quicksort(low: int, high: int, S: List[int]) -> None:
    if low < high:
        # Complete the code here
        pivotpoint = partition(low, high, S)
        quicksort(low, pivotpoint-1,S)
        quicksort(pivotpoint + 1, high,S)

