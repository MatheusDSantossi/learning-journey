# Also called Squeeze

def sortedSquare(nums):
    left = 0
    right = len(nums) - 1
    result = []
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1
            
    result.reverse()
    return result

print(sortedSquare([-4, -1, 0, 3, 10]))

# Time: O(n)
# Space: O(n) or considering that the result is required we can say that is O(1)
