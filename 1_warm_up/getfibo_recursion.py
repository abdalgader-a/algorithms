"""
Description: Implementation of Fibonacci functions using recursion:
    Input: the position of the element in Fibonacci series
    Output: get the number in the given position.

Complexity: O(2^n)

"""


def get_fibo(position) -> int:
    if position < 0:
        return -1
    if position == 0 or position == 1:
        return position
    else:
        return get_fibo(position-1) + get_fibo(position-2)


#Test cases

print(get_fibo(10))
print(get_fibo(4))
print(get_fibo(1))
print(get_fibo(-1))

