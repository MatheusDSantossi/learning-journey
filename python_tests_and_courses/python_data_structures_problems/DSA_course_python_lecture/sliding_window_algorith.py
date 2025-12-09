# Variable-Length Sliding Window problem:

# Time: O(n)
# Space: O(n)
def lengthOfLongestSubstring(s):
    l = 0
    longest = 0
    sett = set()
    n = len(s)
    
    # O(n)
    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
            
        w = (r - l) + 1 # Window
        longest = max(longest, w)
        
        sett.add(s[r])
        
    return longest

s = "abcabcbb"
print(lengthOfLongestSubstring(s))

# Fixed-length Sliding Window

# Time: O(n)
# Space: O(1)
def findMaxAverage(nums, k):
    n = len(nums)
    curr_sum = 0
    
    for i in range(k):
        curr_sum += nums[i]
    
    max_avg = curr_sum / k
    
    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        
        avg = curr_sum / k
        max_avg = max(max_avg, avg)
        
    return max_avg

nums = [1, 12, -5, -6, 50, 3]
print(findMaxAverage(nums, 4))
