"""
Description: Implementation of Random Quick Sort algorithm
Same as Quick Sort except just before executing the partition algorithm,
it randomly selects the pivot between a[i...j] instead of always choosing
a[i] (or any other fixed index between [i...j]) deterministically.

Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'


Time complexity: O(N log N) on average
Space complexity: O(1)
"""
import random


def partition(arr, begin, end) -> int:
    pivot = arr[end]
    i = begin - 1
    for j in range(begin, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def partition_rand(arr, begin, end):
    rand_pivot = random.randrange(begin, end)

    arr[end], arr[rand_pivot] = \
        arr[rand_pivot], arr[end]
    return partition(arr, begin, end)


def random_quick_sort(arr, begin, end) -> list:
    if begin < end:
        pivot_idx = partition_rand(arr, begin, end)
        random_quick_sort(arr, begin, pivot_idx - 1)
        random_quick_sort(arr, pivot_idx + 1, end)
    return arr


# Test cases
ll = [5, 2, 4, 6, 1, 3]
first_index = 0
end_index = len(ll) - 1
print(random_quick_sort(ll, first_index, end_index))

ll2 = [5, 2, 4, 6, 1, 1, 3, 6, 7, 3]
end_index = len(ll2) - 1
print(random_quick_sort(ll2, 0, end_index))

ll3 = [5]
end_index = len(ll3) - 1
print(random_quick_sort(ll3, 0, end_index))
