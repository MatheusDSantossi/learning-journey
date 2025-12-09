def findingMinandMax(arr):
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return min_val, max_val

arr = [10, 20, 30, 40, 50]
arr = [22, 14, 8, 17, 35, 3]

min_val, max_val = findingMinandMax(arr)

print("Minimum value:", min_val)

print("Maximum value:", max_val)
    