"""
<<<Minimum Length Substrings>>>

You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected
substring. Determine the minimum length of the substring of s such that string t is a substring of the selected
substring.
Signature
int minLengthSubstring(String s, String t)
Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the
minimum length required is 5.

Time complexity:
Space complexity:
"""


def min_length_substrings(s, t):
    if len(t) > len(s):
        return -1

    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    start = 0
    min_length = float('inf')
    count = len(t)

    for end in range(len(s)):
        if s[end] in t_count:
            t_count[s[end]] -= 1
            if t_count[s[end]] >= 0:
                count -= 1

        while count == 0:
            min_length = min(min_length, end - start + 1)

            if s[start] in t_count:
                t_count[s[start]] += 1
                if t_count[s[start]] > 0:
                    count += 1

            start += 1

    if min_length == float('inf'):
        return -1
    else:
        return min_length


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


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
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substrings(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substrings(s2, t2)
    check(expected_2, output_2)

    # Add your own test cases here
