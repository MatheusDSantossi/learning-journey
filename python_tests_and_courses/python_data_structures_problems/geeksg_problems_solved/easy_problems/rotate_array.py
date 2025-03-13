"""
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
"""

def rotateArray(arr, d):
    pointer = 0
    size = len(arr)
    temp = 0
    
    for i in range(0, d):
        temp = arr[pointer]
        pointer  = i+1
        
        if pointer >= size:
            pointer = 0
        # print("POinter:", pointer)
    
    # print("Temp: ", temp)
    # temp_size = len(temp)
    index_of_pointer = arr.index(temp) + 1
    rotate_arr = []
    temp_arr = arr
    if index_of_pointer == 0:
        temp_arr.remove(temp)
        temp_arr.append(temp)
        new_arr = temp_arr     
    else:
        rotate_arr = arr[:index_of_pointer]
        print("Rotate_arr: ", rotate_arr)
        temp_arr = arr[index_of_pointer:]
        print("Temp_arr: ", temp_arr)
        new_arr = temp_arr + rotate_arr
        
    for n in new_arr:
        print(n, end = " ")
    return new_arr

def solutionRotateArr(arr, d):
    n = len(arr)
    d %= n
    # First reversing d elements from starting index
    arr[0:d] = reversed(arr[0:n])
    
    # Then reversing the last n-d elements
    arr[d:n] = reversed(arr[d:n])
    
    # Finally reversing the whole array
    arr[0:n] = reversed(arr[0:n])
    return arr[0:n]

# arr = [7, 3, 9, 1]
# d = 9
# arr = [1, 2, 3, 4, 5]
# d = 2
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3

# print(rotateArray(arr, d))
print(solutionRotateArr(arr, d))
