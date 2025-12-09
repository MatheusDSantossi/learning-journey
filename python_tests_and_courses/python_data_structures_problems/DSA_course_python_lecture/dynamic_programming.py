# Fibonacci number

def fib(n):
    # Recursive Solution
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n-2) + fib(n-1)

print(fib(10)) # 55

# Time: O(n)
# Space: O(n)
def fib(n):
    # Dynamic programming
    memo = {0 : 0, 1 : 1}
    
    def f(x):
        if x in memo:
            return memo[x]
        
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
        
    return f(n)

print(fib(10))

# Bottom Up dynamic programming

# Time: O(n)
# Space: O(n)
def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
        
    return dp[n]

print(fib(10)) # 55

# Bottom up

# Time: O(n)
# Space: O(1)
def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    # dp = [0] * (n+1)
    
    prev = 0
    curr = 1
    
    for i in range(2, n+1):
        prev, curr = curr, prev + curr
        
    return curr

print(fib(10)) # 55

# Mathematical calculation

def fib(n):
    golden_ratio = (1 + (5 ** 0.5)) / 2
    
    return int(round((golden_ratio ** n) / (5 ** 0.5)))

print(fib(10)) # 55
