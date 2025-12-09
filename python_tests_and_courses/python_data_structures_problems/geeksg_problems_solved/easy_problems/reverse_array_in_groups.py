"""
Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
"""

def reverser_array_in_gp(arr, k):
    n = len(arr)
    if k > n:
        return arr[::-1] 
    
    groups = n % k
    
    group1 = arr[:groups+1]
    group2 = arr[(groups+1)::]
    
    reverse_gp1, reverse_gp2 = group1[::-1], group2[::-1]
    
    return reverse_gp1 + reverse_gp2               

def reverseInGroups(arr, k):
    n = len(arr)
    returned_arr = []
    
    for i in range(0, n, k):
        if i + k < n:
            arr[i:i+k] = arr[i:i+k][::-1]
            returned_arr += arr[i:i+k]
        else:
            arr[i:n] = arr[i:n][::-1]
            returned_arr += arr[i:n]
            
    return returned_arr
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 3

result = reverseInGroups(arr, k)
print(result)
