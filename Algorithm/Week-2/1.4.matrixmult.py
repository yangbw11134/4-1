# name: 
# student id: 
from typing import List

def matrixmult(n: int, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j];


    

    return C