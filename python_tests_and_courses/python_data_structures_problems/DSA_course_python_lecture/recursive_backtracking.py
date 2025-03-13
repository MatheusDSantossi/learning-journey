# Return all possible sets possibles

# Time: O(2^n)
# Space: O(n)
def subsets(nums):
    n = len(nums)
    res, sol = [], []
    
    # def backtrack(start):
    def backtrack(i):
        if i == n:
            res.append(sol[:]) # Copy of what solution is (sol[:])
            return
        
        # Don't pick nums[i]
        backtrack(i + 1)
        
        # Pick nums[i]
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop() # Backtrack to remove the current element
    
    backtrack(0)
    return res

print(subsets([1, 2, 3]))
    