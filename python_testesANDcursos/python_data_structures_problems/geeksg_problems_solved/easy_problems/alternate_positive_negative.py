"""
Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

Note:
- Resulting array should start with a positive integer (0 will also be considered as a positive integer).
- If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
- The array may or may not have the equal number of positive and negative integers.

Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
Explanation: The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 4 and then -1 and so on.
"""

def rearrenge(arr):
    n = len(arr)
    positive_array = []
    negative_array = []
    new_array = []
    
    for i in arr:
        if i >= 0:
            positive_array.append(i)
        elif i < 0:
            negative_array.append(i)
    
    print(negative_array, 'negative')
    print(positive_array, 'postive')
    
    i = 0
    j = 0
    while i < len(negative_array) or j < len(positive_array):
        if j < len(positive_array):
            new_array.append(positive_array[j])
        if i < len(negative_array):
            new_array.append(negative_array[i])
        i += 1
        j += 1            
    return new_array

arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

print(rearrenge(arr))  # Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
