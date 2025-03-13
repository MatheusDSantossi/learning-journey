# Linear Search
def searchingUnsortedArr(arr, n):
    for i in arr:
        if i == n:
            # return True
            return arr.index(i)
    return False

arr = [2, 3, 4, 10, 40]
n = 10

result = searchingUnsortedArr(arr, n)

# print(result)  # Output: True

# Binary search

def binarySearch(arr, start, end, key):

    # If case is evaluated when element is found else -1 is returned
    if start < end:

        mid = (start + end) // 2
        
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            return binarySearch(arr, start, mid - 1, key)
        
        if key > arr[mid]:
            return binarySearch(arr, mid + 1, end, key)
        
    else:
        return -1
    
if __name__ == "__main__":
    arr = [11, 20, 39, 44, 57, 63, 72, 88, 94]
    key = 88

    index = binarySearch(arr, 0, len(arr) - 1, key)
    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")
