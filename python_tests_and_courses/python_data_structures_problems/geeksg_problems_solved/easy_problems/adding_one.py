"""
Given a non-negative integer(without leading zeroes) represented as an array arr. Your task is to add 1 to the number (increment the number by 1). The digits are stored such that the most significant digit is at the starting index of the array.
Examples:
Input: arr[] = [5, 6, 7, 8]
Output: [5, 6, 7, 9]
Explanation: 5678 + 1 = 5679
"""
def addingOne(arr):
    n = ""
    array_after_adding = []
    for i in arr:
        n += str(i)
    
    n_adding_one = str(int(n) + 1)
    for t in n_adding_one:
        array_after_adding.append(int(t))
    return array_after_adding

def solutionAddOne(arr):
    n = len(arr)
    carry = 1
    
    # Traverse the array from right to left
    for i in range(n -1, -1, -1):
        # Add carry to the current digit and update carry
        arr[i] += carry
        carry = arr[i] // 10
        arr[i] = arr[i] % 10
        
    ans = []
    
    # If carry is 1 after the loop, append it to the answer array
    if carry == 1:
        ans.append(carry)
        
    # Apend the modified digits from the array to the answer array
    ans.extend(arr)
    
    # Return the answer array
    return ans

arr = [5, 6, 7, 8]
# arr = [9, 9, 9]

print(addingOne(arr))
print(solutionAddOne(arr))
