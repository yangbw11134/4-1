from typing import List

n: int
W: int
w: List[int]
include: List[int]

def promising(i: int, weight: int, total: int) -> bool:
    global n, W, w, include

    if weight == W:
        return True

    if i == n:
        return False

    return (weight + total >= W) and (weight + w[i+1] <= W)


def sumofsubsets(i: int, weight: int, total: int) -> None:
    global n, W, w, include

    if promising(i, weight, total):
        if weight == W:
            print("found:", include[1:])
        else:
            include[i+1] = 1
            sumofsubsets(i+1, weight + w[i+1], total - w[i+1])

            include[i+1] = 0
            sumofsubsets(i+1, weight, total - w[i+1])