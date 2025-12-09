"""
Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.
"""

# NOTE: Bad code and didn't work properly
# def third_largest_element(arr):
#     n = len(arr)
#     if n < 3:
#         return "Array must contain at least 3 elements."
    
#     first = second = third = float('-inf')
    
#     for i in arr:
#         if i > first:
#             print("Frist: ", first)
#             first, second = i, first
            
#         elif i > second and i != first:
#             print("Second: ", second)
#             second = i

#     for i in arr:
#         if i > third and i != first and i != second:
#             third = i
#     return third

def third_largest_element(arr):
    n = len(arr)
    if n < 3:
        return "Array must contain at least 3 elements."
    
    big1 = -1
    big2 = -1
    big3 = -1
    
    for i in arr:
        if i > big3: #if current number is greater than third biggest
            big3 = i #update third biggest to current number
            
        if big3 > big2: #if third biggest is greater than second biggest
            big2, big3 = big3, big2 #swap second and third biggest
            
        if big2 > big1: #if second biggest is greater than first biggest
            big1, big2 = big2, big1 #swap first and second biggest
            
    return big3

arr = [2, 4, 1, 3, 5]

third_largest = third_largest_element(arr)
print("Third largest element:", third_largest)
