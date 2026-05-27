# name: 
# student id: 
def fib1(n: int) -> int:
    # Complete the code here

    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)