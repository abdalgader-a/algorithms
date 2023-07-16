"""
<<<Reverse to Make Equal>>>

Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
Signature
bool areTheyEqual(int[] arr_a, int[] arr_b)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if B can be made equal to A, return false otherwise.
Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A.


Time Complexity: O(n^2)
Space Complexity: O(n)

"""

import math
import copy


# Add any extra import statements you may need here
# Add any helper functions you may need here


def are_they_equal(target_array, array_b):
    for i in range(len(target_array)):
        if array_b[i] == target_array[i]:  # reduce the iterations the lists has identical entries at the beginning
            continue
        for j in range(i + 1, len(array_b)):
            aux = copy.deepcopy(array_b)
            aux[i:j + 1] = aux[i:j + 1][::-1]
            if aux == target_array:
                return True

    return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 4
    a_1 = [1, 2, 3, 4]
    b_1 = [1, 4, 3, 2]
    expected_1 = True
    output_1 = are_they_equal(a_1, b_1)
    check(expected_1, output_1)

    n_2 = 4
    a_2 = [1, 2, 3, 4]
    b_2 = [1, 2, 3, 5]
    expected_2 = False
    output_2 = are_they_equal(a_2, b_2)
    check(expected_2, output_2)

    # Add your own test cases here
