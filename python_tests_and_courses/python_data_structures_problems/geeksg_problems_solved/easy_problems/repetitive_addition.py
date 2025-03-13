"""
Input: n = 1234
Output: 1
Explanation: Step 1: 1 + 2 + 3 + 4 = 10. Step 2: 1 + 0 = 1
"""

def repetitiveSum(n):
    # return sum(int(digit) for digit in str(n))
    # for n in range(len(str(n))):
    n_str = str(n)
    if len(n_str) > 1:
        n = sum(int(digit) for digit in n_str)
        
        n = repetitiveSum(n)
    
    return int(n)

def solutionSingleDigit(n):
    # Calculate the remainder when the number is divided by 9
    dig = n % 9
    print("DIG: ", dig)
    
    # If the remainder is not 0, return the remainder, otherwise return 9
    ans = dig if dig != 0 else 9
    
    return ans

print(repetitiveSum(1234))  # Output: 1
print(repetitiveSum(5674))  # Output: 4
print(repetitiveSum(9))  # Output: 9
print("SOLUTION CODE")
print(solutionSingleDigit(1234))  # Output: 1
print(solutionSingleDigit(5674))  # Output: 4
print(solutionSingleDigit(9))  # Output: 9
