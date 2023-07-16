"""
Description: Implementation of Bubble sort algorithm
Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'

Time Complexity: O(n^2)
Space Complexity: O(1) because it is in-place
"""


def bubble_sort(mylist) -> list:
    for p in range(len(mylist)):
        for i in range(0, len(mylist)-1):
            j = i+1
            if mylist[i] > mylist[j]:
                temp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = temp

    return mylist


# Test cases
l1 = [6, 5, 1, 3, 8, 7, 2, 4]
print(bubble_sort(l1))

l2 = [10, 1, 3, 7, 9, 7, 12, 0, 3]
print(bubble_sort(l2))

