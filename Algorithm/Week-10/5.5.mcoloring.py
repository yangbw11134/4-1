from typing import List

# Global variables
W: List[List[int]] = []     # Adjacency matrix
vcolor: List[int] = []      # Vertex colors
n: int = 0                  # Number of vertices
count: int = 0              # Solution counter

def promising(i: int) -> bool:
    global W, vcolor
    # Complete the code here
    j = 1
    is_promising = True

    while(j<i and is_promising):  
        if(W[i][j] and vcolor[i] == vcolor[j]):
            is_promising = False
        j+=1
    
    return is_promising

def mcoloring(i: int, m: int) -> None:
    global n, vcolor, count
    if promising(i):
        if i == n:
            print(vcolor[1:])
            # Complete the code here
            count +=1
        else:
            # Complete the code here
            for color in range(m):
                vcolor[i+1] = color
                mcoloring(i+1, m)
            
