# name: 
# student id: 
def fib2(n: int) -> int:
    f = [0] * (n + 1)
    # Complete the code here
    if n <= 1:
        f[n] = n
    else:
        f[n] = f[n-1] + f[n-2]

    return f[n]
