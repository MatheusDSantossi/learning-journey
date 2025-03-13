"""
other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.

Example:
Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.
"""

def waveArray(arr):
    n = len(arr)
    for i in range(n-1):
        if i % 2 == 0:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
    return arr

def solutionWaveArray(arr):
    for i in range(0, len(arr) -1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        
    return arr

# arr = [1, 2, 3, 4, 5]
arr = [2, 4, 7, 8, 9, 10]

print(waveArray(arr)) # Output: [2, 1, 4, 3, 5]
print(solutionWaveArray(arr)) # Output: not as I expected
