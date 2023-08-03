"""
Description: Implementation of Counting sort algorithm
Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'

Time Complexity: O(n + max)
Space Complexity: O(n + max)
"""


def counting_sort_operation(mylist) -> list:
    max_elem = max(mylist)
    ordered_list = [0] * len(mylist)
    aux_count = [0] * (max_elem+1)
    for i in mylist:
        aux_count[i] += 1

    for i in range(1, len(aux_count)):
        aux_count[i] = aux_count[i-1] + aux_count[i]

    for i in mylist:
        ordered_list[aux_count[i]-1] = i
        aux_count[i] -= 1

    return ordered_list


def counting_sort(mylist) -> list:
    min_num = min(mylist)
    if min_num < 0:
        neg_elems, pos_elems = [], []
        for i in mylist:
            if i < 0:
                neg_elems.append(-1 * i)
            else:
                pos_elems.append(i)
        order_neg = counting_sort_operation(neg_elems)[::-1]
        for k in range(len(order_neg)):
            order_neg[k] = -1 * order_neg[k]

        return order_neg + counting_sort_operation(pos_elems)
    else:
        return counting_sort_operation(mylist)


# Test cases
l1 = [6, 5, 1, 3, 10, 8, 2, 1]
print(counting_sort(l1))

l2 = [10, -1, 3, -7, 9, 7, 12, 0, -3]
print(counting_sort(l2))

