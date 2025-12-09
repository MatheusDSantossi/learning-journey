"""
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
"""

def second_largest(arr):
    n = len(arr)
    if n < 2:
        return -1

    first = second = float('-inf')
    for num in arr:
        if num > first:
            first, second = num, first
        elif num > second and num != first:
            second = num
            
    if second == float('-inf'):
        return -1
    else:
        return second

# arr = [12, 35, 1, 10, 34, 1]
arr = [10, 5, 10]

# print(sort_arr(arr))
print("Second largest element is", second_largest(arr))
