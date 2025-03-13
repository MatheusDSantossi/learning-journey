"""
Input: arr = [54, 43, 2, 1, 5]
Output: 53 42 1 0 4
"""

def decrement_list(arr):
    
    for i in arr:
        decrement = i - 1 
        # decremented_list.append(decrement)
        print(decrement, end=" ")
        
decrement_list([324, 5, 2, 2, 0])
