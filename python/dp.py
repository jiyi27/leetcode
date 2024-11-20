"""
Fibonacci numbers
"""


def fibRecursive(n: int) -> int:
    if n < 2:
        return n
    return fibRecursive(n - 1) + fibRecursive(n - 2)


def fibDp(n: int) -> int:
    if n < 2:
        return n
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

