"""
<<<Matching Pairs>>>

Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after
swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index
of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i]
are equal.
Note: This means you must swap two characters at different indices.

Signature
int matchingPairs(String s, String t)

Input
s and t are strings of length N
N is between 2 and 1,000,000

Output
Return an integer denoting the maximum number of matching pairs

Example 1
s = "abcd"
t = "adcb"
output = 4
Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.
Example 2
s = "mno"
t = "mno"
output = 1
Explanation:
Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1,
s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.

"""

import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
    # Write your code here
    n, k = len(s), 0
    diff = []
    for i in range(n):
        if s[i] == t[i]:
            k += 1
        else:
            diff.append(i)

    if len(diff) == 0 or len(diff) == 1:
        return n - 2
    else:
        for d_i in range(0, len(diff) - 1):
            for d_j in range(1, len(diff)):
                t_target = t[diff[d_i]] + t[diff[d_j]]
                s_target = s[diff[d_j]] + s[diff[d_i]]
                if s_target == t_target:
                    return k + 2  # if allows more than one swap, change it to k += 2 and return k by end of else clause


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def print_integer(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    right_tick = '\u2713'
    wrong_tick = '\u2717'
    if result:
        print(right_tick, 'Test #', test_case_number, sep='')
    else:
        print(wrong_tick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        print_integer(expected)
        print(' Your output: ', end='')
        print_integer(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "adcjkm2lb", "abc2kmjld"
    expected_2 = 7
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here

    s_3, t_3 = "abcd", "abcd"
    expected_3 = 2
    output_3 = matching_pairs(s_3, t_3)
    check(expected_3, output_3)
