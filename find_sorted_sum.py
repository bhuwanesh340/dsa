# Sorted Pair Sum
# Given a sorted array and a number x, find a pair in array whose sum is closest to x.

# Input Format
# In the function an integer vector and number x is passed.

# Output Format
# Return a pair of integers.

# Sample Input
# {10, 22, 28, 29, 30, 40}, x = 54

# Sample Output
# 22 and 30
import numpy as np

def find_sorted_pair_sum(arr, val):
    start = 0
    end = len(arr)-1
    diff = np.inf
    leftIdx, rightIdx = 0,0

    while start < end:
        curr_sum = arr[start] + arr[end]

        if abs(curr_sum - val) < diff:
            diff = abs(curr_sum - val)
            leftIdx = arr[start]
            rightIdx = arr[end]

            start += 1
        else:
            end -= 1

    return diff, leftIdx, rightIdx

arr = [10,22,28,29,30,40]
val = 54

out, leftIdx, rightIdx = find_sorted_pair_sum(arr, val)
print(out, leftIdx, rightIdx)


