"""
Input: arr = [54, 43, 2, 1, 5]
Output: 105
"""

def sum_list(arr):
    head = arr[0]
    for x in arr[1:]:
        summ = head = x + head
    return summ

summ = sum_list([324, 5, 2, 2])
print(summ)
