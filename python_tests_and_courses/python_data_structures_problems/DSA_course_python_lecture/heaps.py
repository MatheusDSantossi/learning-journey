# Build a Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq

print(A)
heapq.heapify(A)

print(A)

# Heap Push (Insert element)
# Time: O(log n)

heapq.heappush(A, 4)
print(A)

# Heap Pop (Extract min value)
# Time: O(log n)

minn = heapq.heappop(A)

print(A, minn)

# Heap Sort
# Time: O(n log n), Space: O(n)
# NOTE: O(1) Space is possible via swapping, but this is complex

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
        
    return new_list

B = [1, 3, 5, 8, 10, 20, 4, 50]
print(heapsort(B))

# Heap Push Pos: Time: O(log n)
heapq.heappushpop(A, 99)
print(A)

# Peak at Min: Time O(1)
A[0]

# Max Heap

C = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(C)

for i in range(n):
    C[i] = -C[i]
    
heapq.heapify(C)

print(C)

heapq.heappush(B, -7) # Inser 7 into max heap

# Build heap from scratch - Time: O(n log n)
D = [-5, 4, 2, 1, 7, 0, 3]
heap = []

for x in D:
    heapq.heappush(heap, x)
    print(heap, len(heap)) # Checking also the size of heap

# Putting tuples of items on the heap

E = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(E)
# Key is the value on teh list and the value is the frequency
print(counter)

heap = []

for k, v in counter.items():
    heapq.heappush(heap, (v, k))
    
print(heap)
