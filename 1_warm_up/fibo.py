"""
Description: Create a two Fibonacci functions:
    fib: write Fibonacci series up to n
    fib2: return Fibonacci series up to n
Complexity:
    fib is O(n)
    fib2 is O(n)

"""


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
