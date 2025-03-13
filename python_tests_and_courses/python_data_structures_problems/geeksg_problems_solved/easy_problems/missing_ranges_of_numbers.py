"""
You have an inclusive interval [lower, upper] and a sorted array of unique integers arr[], all of which lie within this interval. A number x is considered missing if x is in the range [lower, upper] but not present in arr[]. Your task is to return the smallest set of sorted ranges that includes all missing numbers, ensuring no element from arr is within any range, and every missing number is covered exactly once.

Input: arr[] = [14, 15, 20, 30, 31, 45], lower = 10, upper = 50
Output: [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]
Explanation: These ranges represent all missing numbers between 10 and 50 not present in the array.
"""

def coverMissingRanges(arr, lower, upper):
    ranges = []
    size = len(arr)
    pointer = 0
    if arr[0] > lower:
        ranges.append([lower, arr[pointer] - 1])
        
    for i in range(1, size):
        print("pointer: ", pointer)
        print("i: ", i)
        if arr[pointer] > arr[i]:
            print(arr[pointer]+1, arr[i]-1)
            ranges.append(arr[pointer]+1, arr[i]-1)
        

        pointer+=1
        
    if arr[-1] < upper and pointer == size - 1:
        ranges.append([arr[-1]+1, upper]) 
    return ranges   
        
def solutionMissingRanges(arr, lower, upper):
    res = []
    n = len(arr)
    
    # Check for missing range before the first element
    if lower < arr[0]:
        res.append([lower, arr[0] - 1])
    
    # Iterate through the array
    for i in range(n - 1):
        # Check for missing range between current element and next element
        if arr[i + 1] - arr[i] > 1:
            res.append([arr[i] + 1, arr[i + 1] - 1])
    
    # Check for missing range after the last element
    if upper - arr[-1] > 1:
        res.append([arr[-1] + 1, upper])
    
    return res

arr = [14, 15, 20, 30, 31, 45]

lower = 10

upper = 50

print(coverMissingRanges(arr, lower, upper))  # Output: [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]
print(solutionMissingRanges(arr, lower, upper))  # Output: [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]

