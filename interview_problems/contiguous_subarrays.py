"""
<<<Contiguous Subarrays>>>
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous
subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.
Signature
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) at index 0 with the maximum value in the
subarray being 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1] [1, 2, 3, 4, 5, 6]


Time complexity: O(nk) is second algorithm, first one has better time efficiency
Space complexity: O(1) no need more space to perform get the counts
"""


def count_subarrays(arr) -> list:
    sub_count = len(arr)*[1]
    for i, element in enumerate(arr):
        forward, backward = i+1, i-1
        if i == 0:
            while forward < len(arr) and element > arr[forward]:
                sub_count[i] += 1
                forward += 1
        elif i == len(arr)-1:
            while backward >= 0 and element > arr[backward]:
                sub_count[i] += 1
                backward -= 1
        else:
            while forward < len(arr) and element > arr[forward]:
                sub_count[i] += 1
                forward += 1
            while backward >= 0 and element > arr[backward]:
                sub_count[i] += 1
                backward -= 1

    return sub_count


# Other implementation
def count_subarrays2(arr) -> list:
    # Write your code here
    sub_count = dict(zip(arr, [1] * len(arr)))
    for k, n in enumerate(arr):
        for z in range(k - 1, -1, -1):
            if arr[k] > arr[z]:
                sub_count[n] += 1
            else:
                break

        for z in range(k + 1, len(arr)):
            if arr[k] > arr[z]:
                sub_count[n] += 1
            else:
                break
    return list(sub_count.values())


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def print_integer(n):
    print('[', n, ']', sep='', end='')


def print_integer_list(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        print_integer_list(expected)
        print(' Your output: ', end='')
        print_integer_list(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    test_1 = [3, 4, 1, 6, 2]
    expected_1 = [1, 3, 1, 5, 1]
    output_1 = count_subarrays(test_1)
    check(expected_1, output_1)

    test_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [1, 2, 6, 1, 3, 1]
    output_2 = count_subarrays(test_2)
    check(expected_2, output_2)

    # Add your own test cases here
