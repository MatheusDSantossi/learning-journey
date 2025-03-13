"""
Input: a = 1, b = 2, c = 3
Output: 1 2 3
Explanation: Just create a list and append 1 2 3 to it. Then return [1,2,3] list.
"""

def append_list(**kargs):
    appended_list = []
    
    for k in kargs:
        appended_list.append(kargs[k])
    
    return appended_list        

arr = append_list(a = 4, b = 5, c = 6, w = 10)
print(arr)
        