from collections import defaultdict
# city_map = {}
city_map = defaultdict(list)

cities = ["Calgary", "Vancouver", "Toronto"]

# First you need to initialize the key, to avoid that we can use a defaultdictionary

city_map["Canada"].append(cities)

city_list = city_map.values()
print(city_list)

# Coding interview problem
class Solution:
    def groupAnagrams(self, strs: list[str]):
        # anagram_map = {}
        anagram_map = defaultdict(list)
        result = []
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        
        # print(anagram_map)
        for value in anagram_map.values():
            result.append(value)
            
        return result

solution = Solution()

print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
