"""
Description: Implementation of Insertion sort algorithm
Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'

Time Complexity: O(n^2)
Space Complexity: O(1) because it's in-place

"""


def insertion_sort(mylist) -> list:
    for i in range(1, len(mylist)):
        key = mylist[i]
        j = i - 1
        while j >= 0 and mylist[j] > key:
            mylist[j + 1] = mylist[j]
            j = j - 1
        mylist[j + 1] = key
    return mylist


# Test cases
ll = [5, 2, 4, 6, 1, 3]
print(insertion_sort(ll))
ll2 = [5, 2, 4, 6, 1, 1, 3, 6, 7, 3]
print(insertion_sort(ll2))
