"""
Input: arr = [54, 43, 2, 5, 14, 17, 18, 9]
Output: even: 54 2 14 18, odd: 43 5 17 19
"""

def separate_even_odd(arr):
    even_arr = []
    odd_arr = []
    
    for i in arr:
        if i % 2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
            
    return even_arr, odd_arr

arr = [54, 43, 2, 5, 14, 17, 18, 9]

even, odd = separate_even_odd(arr)

print("even:", even)
print("odd:", odd)
