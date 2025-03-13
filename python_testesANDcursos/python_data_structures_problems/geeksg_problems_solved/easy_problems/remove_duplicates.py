"""
Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and modify the original array such that all the distinct elements come at the beginning of the original array.
Input: arr = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return 1 after modifying the array, the driver code will print the modified array elements.
"""

def searchedOnInternetRemoveDuplicates(numbers):
    res = []
    size = 0
    
    for val in numbers:
        if val not in res:
            res.append(val)
            size += 1
            
    return res, size

def removeDuplicates(numbers):
    # Initializting pointer i to the first element of the array
    i = 0
    size = len(numbers)
    
    # Iterating through the array
    for j in range(1, size):
        # If current element is not equal to the previous element
        if numbers[j]!= numbers[i]:
            # Increment i and assign the current element to the i'th position
            i += 1
            numbers[i] = numbers[j]
    
    # Returning the modified array size
    return numbers[:i+1], i+1

arr = [2, 2, 2, 2, 2]
arr = [1, 2, 4]
arr = [1, 2, 4, 2]

modified_arr, modified_size = removeDuplicates(arr)
modified_arr, modified_size = searchedOnInternetRemoveDuplicates(arr)

print(modified_arr) # [2]
print(modified_size) # Output: 1
