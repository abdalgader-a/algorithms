"""
Description: Implementation of Radix Sort algorithm for non-negative array.
Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'



Time Complexity: O(nd), d number of max digits
Space Complexity: O(n+d)
"""


def aux_counting_sort(mylist, digit):
    n = len(mylist)
    ordered_list = [0] * n
    aux_count = [0] * 10

    for k in range(0, n):
        index = mylist[k] // digit
        aux_count[index % 10] += 1

    for k in range(1, 10):
        aux_count[k] += aux_count[k - 1]

    for k in range(len(mylist) - 1, -1, -1):
        index = mylist[k] // digit
        ordered_list[aux_count[index % 10] - 1] = mylist[k]
        aux_count[index % 10] -= 1

    for k in range(0, len(mylist)):
        mylist[k] = ordered_list[k]


def radix_sort(mylist):
    max_elem = max(mylist)
    digit = 1
    while max_elem / digit >= 1:
        aux_counting_sort(mylist, digit)
        digit *= 10
    return mylist


# Test cases
l0 = [10, 150, 95, 20, 250, 4, 13, 52]
print(radix_sort(l0))

l1 = [6, 5, 1, 3, 10, 8, 2, 1]
print(radix_sort(l1))
