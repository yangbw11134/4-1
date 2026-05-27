from typing import List

def merge(h: int, m: int, U: List[int], V: List[int], S: List[int]) -> None:
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    # Complete the code here
    while(i < h and j < m ):
        if(U[i] < V[j]):
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1
    if(i >= h):
        S[k:h+m] = V[j:m]
    else:
        S[k:h+m] = U[i:h]
    

def mergesort(n: int, S: List[int]) -> None:
    h = n // 2
    m = n - h
    
    U = [0] * h
    V = [0] * m

    if n > 1:
        # Complete the code here
        U[0:h] = S[0:h]
        V[0:m] = S[h:n]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)