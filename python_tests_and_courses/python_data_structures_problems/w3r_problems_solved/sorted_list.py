def sorted_order(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]
    
    L = [i for i in arr[:-1] if i <= p]    
    R = [i for i in arr[:-1] if i > p]    
    
    L = sorted_order(L)
    R = sorted_order(R)
    
    return L + [p] + R

arr = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

print(sorted_order(arr))
