"""
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
"""

def sort_arr(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    p = arr[-1]
    
    L = [i for i in arr[:-1] if i >= p]
    R = [i for i in arr[:-1] if i < p]
    
    L = sort_arr(L)
    R = sort_arr(R)
    
    return L + [p] + R
    
def move_zeros_to_end(arr):
    sorted_array = sort_arr(arr)
    
    # return sorted_array
    
    zeros_n = []
    
    for i in sorted_array:
        if i == 0:
            zeros_n.append(i)
            sorted_array.remove(i)
        
    return sorted_array + zeros_n

# arr = [1, 2, 0, 4, 3, 0, 5, 0]
arr = [3, 5, 0, 0, 3, 0, 5, 0]

print(move_zeros_to_end(arr))
    