"""
Description: Implementation of Fibonacci functions using recursion and optimized via memoization.
    Input: the position of the element in Fibonacci series
    Output: get the number in the given position.

Time Complexity: O(n)

"""
from collections import defaultdict

fibo_hash = defaultdict(lambda: 0)
fibo_hash[0] = 0
fibo_hash[1] = 1


def get_fibo(position) -> int:
    if position in fibo_hash.keys():
        return fibo_hash[position]

    result = get_fibo(position - 1) + get_fibo(position - 2)
    fibo_hash[position] = result
    return result


# Test cases

print(get_fibo(10))
print(get_fibo(4))
print(get_fibo(1))
print(get_fibo(-1))
