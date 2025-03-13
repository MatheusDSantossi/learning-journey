def waveArray(arr):
    size = len(arr)
    pointer = 0
    
    for i in range(1, size):
        print("pointer: ", pointer)
        print("i: ", i)
        if arr[pointer] < arr[i]:
            arr[i], arr[pointer] = arr[pointer], arr[i]
        pointer += 1
        
    return arr

def sortInWaveSolution(arr):
    n = len(arr)
    arr.sort()
        
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr
        
arr = [10, 5, 6, 3, 2, 20, 100, 80]        

print(waveArray(arr))
print(sortInWaveSolution(arr))
        