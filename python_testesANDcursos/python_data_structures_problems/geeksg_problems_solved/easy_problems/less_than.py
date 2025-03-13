"""
Input: arr = [54, 43, 2, 1, 5], k = 6
Output: 2 1 5
Explanation: 2 1 5 are less than 6.
"""

def less_than(arr, k):
    return [i for i in arr if i < k]
    # numbers = [i for i in arr if i < k]
    # for i in numbers:
    #     if i is not None:
    #         print(i, end=" ")

arr = [54, 43, 2, 1, 5]
print(less_than(arr, 6))
