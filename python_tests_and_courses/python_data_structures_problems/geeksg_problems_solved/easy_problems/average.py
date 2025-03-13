"""
Input: arr = [-12, 8, -7, 6, 12, -9, 14]
Output: avg = 10.0
Explanation: The non negative numbers are 8 6 12 14. The sum is 8+6+12+14 = 40, Average = 40/4 = 10.0
"""

def average_list(arr):
    size = 0
    summ = 0
    
    for i in arr:
        if i >= 0:
            summ += i
            size += 1
            
    average = summ / size   
    
    return average

# arr = [-12, 8, -7, 6, 12, -9, 14]
# arr = [1, 2, 3]
arr = [5, 0, 0, 0]

avg = average_list(arr)

print("Average = ", avg)
