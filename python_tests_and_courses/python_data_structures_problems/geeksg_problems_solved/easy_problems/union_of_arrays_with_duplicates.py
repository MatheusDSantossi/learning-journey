"""
Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct.
"""

def unionOfTwoArrays(arrA, arrB):
    new_array = []

    new_arrayA = set(arrA)
    new_arrayB = set(arrB)

    print(new_arrayA)
    print(new_arrayB)

    new_array = list(new_arrayA) + list(new_arrayB)
    new_array = set(new_array)
    return len(new_array)


# Example

arrA = [1, 2, 3, 4, 5]
arrB = [1, 2, 3]
arrA = [85, 25, 1, 32, 54, 6]
arrB = [85, 2] 
arrA = [1, 2, 1, 1, 2]
arrB = [2, 2, 1, 2, 1]

result = unionOfTwoArrays(arrA, arrB)
print(result)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
