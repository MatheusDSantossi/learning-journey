"""
Introduction: The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if the product of their abilities is maximum. Given the abilities of some candidates in an array, arr[], return the maximum collective ability from the pool of candidates.

Input: arr[] = [10, 3, 5, 6, 20]
Output: 1200
Explanation: Multiplication of 10, 6, and 20 is 1200.
"""

def sort_arr(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]
    
    L = [i for i in arr[:-1] if i <= p]
    R = [i for i in arr[:-1] if i > p]
    
    L = sort_arr(L)
    R = sort_arr(R)
    
    return L + [p] + R


def product_3_greater(arr):
    sorted_array = sort_arr(arr)
    product = 1
    for n in sorted_array[-3:]:
        product *= n
        
    return product

def maxProduct(arr):
    n = len(arr)
    
    maxA = float('-inf')
    maxB = float('-inf')
    maxC = float('-inf')
    
    minA = float('inf')
    minB = float('inf')
    
    for i in range(n):
        if arr[i] > maxA:
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
            
        elif arr[i] > maxB:
            maxC = maxB
            maxB = arr[i]
            
        elif arr[i] > maxC:
            maxC = arr[i]
            
        # update minimum
        if arr[i] < minA:
            minB = minA
            minA = arr[i]
            
        elif arr[i] < minB:
            minB = arr[i]
            
    return max(minA * minB * maxA, maxA * maxB * maxC)
    
arr = [852, -566, 182, -638, -693, -323]
# arr = [-10, -3, -5, -6, -20]
print(sort_arr(arr))

print("Multiplicaiton is equal to: ", product_3_greater(arr))
print("Multiplicaiton is equal to: ", maxProduct(arr))
