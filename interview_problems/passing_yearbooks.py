"""

Passing Yearbooks
There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.
Signature
int[] findSignatureCounts(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
Output
Return a list of n integers output, as described above.
Example 1
n = 2
arr = [2, 1]
output = [2, 2]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is Student 2.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is Student 1.
Pass 2:
Student 1 signs Student 2's yearbook. Then they pass it to the student at arr[0], which is Student 2.
Student 2 signs Student 1's yearbook. Then they pass it to the student at arr[1], which is Student 1.
Pass 3:
Both students now hold their own yearbook, so the process is complete.
Each student received 2 signatures.
Example 2
n = 2
arr = [1, 2]
output = [1, 1]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is themself, Student 1.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is themself, Student 2.
Pass 2:
Both students now hold their own yearbook, so the process is complete.
Each student received 1 signature

Extra Example:
input [4, 1, 2, 3], output = [4, 4, 4, 4]

p1:                                          ---> [Books to sign]
  -s 4 sign book 4 & passit to s at arr[3]=3.
  -s 1 sign book 1 & passit to s at arr[0]=4.
  -s 2 sign book 2 & passit to s at arr[1]=1.
  -s 3 sign book 3 & passit to s at arr[2]=2.--> [1, 2, 3, 4]
p2:
  - s 4 sign book 1 & passit to s at arr[3]=3.
  - s 1 sign book 2 & passit to s at arr[0]=4.
  - s 2 sign book 3 & passit to s at arr[1]=1.
  - s 3 sign book 4 & passit to s at arr[2]=2. --> [2, 3, 4, 1]

p3:
  - s 4 sign book 2 & passit to s at arr[3]=3.
  - s 1 sign book 3 & passit to s at arr[0]=4.
  - s 2 sign book 4 & passit to s at arr[1]=1.
  - s 3 sign book 1 & passit to s at arr[2]=2. --> [3, 4, 1, 2]

p4:
  - s 4 sign book 3 & passit to s at arr[3]=3.
  - s 1 sign book 4 & passit to s at arr[0]=4.
  - s 2 sign book 1 & passit to s at arr[1]=1.
  - s 3 sign book 2 & passit to s at arr[2]=2.--> [4, 1, 2, 3]
p5:
  - s 4 hold book 4 & keep it.
  - s 1 hold book 1 & keep it.
  - s 2 hold book 2 & keep it.
  - s 3 hold book 3 & keep it.




Time complexity: O(n^2)
Space complexity: O(n)
"""

import copy


# Add any extra import statements you may need here
def find_signature_counts(arr):
    to_sign = copy.deepcopy(arr)
    signs = len(arr) * [0]

    for i, student in enumerate(arr):
        signs[i] += 1
        to_sign[student - 1] = student

    while to_sign != arr:
        holding_book = copy.deepcopy(to_sign)
        for i, student in enumerate(arr):
            if student != holding_book[i]:
                to_sign[student - 1] = holding_book[i]
                signs[i] += 1
            else:
                continue

    return signs


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
    arr_2 = [4, 1, 2, 3]
    expected_2 = [4, 4, 4, 4]
    output_2 = find_signature_counts(arr_2)
    check(expected_2, output_2)

    arr_1 = [2, 1]
    expected_1 = [2, 2]
    output_1 = find_signature_counts(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2]
    expected_2 = [1, 1]
    output_2 = find_signature_counts(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
