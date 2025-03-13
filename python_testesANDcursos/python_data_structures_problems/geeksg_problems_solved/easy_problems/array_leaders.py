"""
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
"""

def arrayRightLeader(array):
    leaders = []
    pointer = 0
    max_element = array[-1]
    min_element = float('-inf')
    size = len(array)
    last_number = array[-1]
    for i in range(1, size):
        print("Last number: ", last_number)
        print("Size: ", size)
        print("i: ", i)
        print("Min element: ", min_element)
        
        if array[pointer] > array[i]:
            print("Max element: ", max_element)
            print("Array[i]: ", array[i])
            max_element = array[pointer]
            if array.count(array[i]) == 1:
                array.remove(array[i])
                size-=1
            leaders.append(max_element)
            
        pointer += 1
        print("Pointer: ", pointer)
        print("Size: ", size)
        
    leaders.append(last_number)
    return leaders

def solutionLeaders(arr):
    ans = []
    n = len(arr) 
    maxx = arr[n - 1]
    
    # We start traversing the array from the last element
    for i in range(n -1, -1, -1):
        # If the current element is greater than or equal to the max element found so far
        # then it is a leader and we add it to the result
        if arr[i] >= maxx:
            maxx = arr[i]
            ans.append(arr[i])
    
    ans.reverse()
    
    # The leader of an array is the last element
    
    return ans

arr = [16, 17, 4, 3, 5, 2]
arr = [10, 4, 2, 4, 1]
arr = [5, 10, 20, 40]
arr = [30, 10, 10, 5]

# print(arrayRightLeader(arr)) # Output: [17, 5, 2]
print(solutionLeaders(arr)) # Output: [17, 5, 2]
