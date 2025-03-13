# Time: O(log2 n) {log n} (log base 2 is basically dividing the value by 2 every time, the exactly thing the binary search does)
# Space: O(1) (we'll only storage 3 variables the most they being R, L and M) the search can be done recursively or not

A = [-3, -1, 0, 1, 4, 7]

# Naive O(n) searching
if -1 in A:
    print("Element found")
    
# Traditional Binary Search - Looking up if number is in array

def binarySearch(arr, target):

    N = len(A)
    L = 0
    R = N - 1

    while L <= R:
        # M = (L + R) // 2
        M = L + (R - L) // 2
        
        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1

    return False

print(binarySearch(A, 0))

# Based on a condition (Condition based)
B = [False, False, False, False, False, True]

def binarySearchCondition(arr):
    N = len(A)
    L = 0
    R = N - 1
    
    while L < R:
        # M = L + (R - L) // 2
        M = (L + R) // 2
        
        if B[M]:
            R = M
        else:
            L = M + 1
    
    return L

print(binarySearchCondition(B))
