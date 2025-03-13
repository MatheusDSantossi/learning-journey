# Bubble Sort
# Time: O(n^2)
# Space: O(1)
print("---------- Bubble Sort --------")

A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    
    while flag:
        flag = False
        
        for i in range(1, n):
            # if arr[i-1] < arr[i]: # Descending order
            if arr[i-1] > arr[i]: # Ascending order
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
                
bubble_sort(A)
print(A)
    
    
# Insertion Sort
# Time: O(n^2)
# Space: O(1)
print("---------- Insertion Sort --------")

B = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            # if arr[j-1] < arr[j]: # Descending order
            if arr[j-1] > arr[j]: # Ascending order
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
            
insertion_sort(B)
print(B)

# Selection Sort
# Time: O(n^2)
# Space: O(1)
print("---------- Selection Sort --------")

C = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
            
selection_sort(C)
print(C)

# Merge Sort
# Time: O(n log n) {n log2 n}
# Space: O(n) NOTE: Can be log n, but this is harder to write
print("---------- Merge Sort --------")

D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    n = len(arr)
    
    if n == 1:
        return arr
    
    m = n // 2
    L = arr[:m]
    R = arr[m:]
    
    L = merge_sort(L)
    R = merge_sort(R)
    l, r = 0, 0
    L_len = len(L) 
    R_len = len(R)
    
    sorted_arr = [0] * n
    i = 0
    
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
            
        i += 1
        
    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1
        
    return sorted_arr

print(merge_sort(D))

# Quick Sort
# Time: O(n log n) NOTE: Assuming a good pivot, in case we keep getting a bad pivot, in the worst case it's O(n^2)
# Space: O(log n)
print("---------- Quick Sort --------")

E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]
    
    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]
    
    L = quick_sort(L)
    R = quick_sort(R)
    
    return L + [p] + R

print(quick_sort(E))

# Counting Sort
# Time: O(n + j) NOTE: k is the max of values in the array {k is the range of data}
# Space: O(k)
print("---------- Counting Sort --------")

# F = [-5, 3, 2, 1, -3, -3, 7, 2, 2] # Doing with negative values is harder
F = [5, 3, 2, 1, 3, 3, 7, 2, 2]

def counting_sort(arr):
    n = len(arr)
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    
    for x in arr:
        counts[x] += 1
        
    i = 0
    for c in range(max_val + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1

counting_sort(F)
print(F)

# What we usually do in practice
# Time complexity is O(n log n) from using Tim Sort

G = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# In place (constant space)
G.sort()

print(G)

# Get new sorted array - O(n) space

H = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

sorted_H = sorted(H)

print(H, sorted_H)

# Sort array of tuples
I = [(-5, 3), (2, 1), (-3, -3), (7, 2), (2, 2)]

sorted_I = sorted(I, key = lambda t: t[-1])

print(sorted_I)
