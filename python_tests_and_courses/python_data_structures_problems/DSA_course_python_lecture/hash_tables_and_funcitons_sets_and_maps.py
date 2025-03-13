# Hashsets

s = set()

# Add item into set - 0(1)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)

# Lookup if item in set - O(1)
if 1 not in s:
    print(True)
    
# Remove item from set - O(1)
s.remove(1)
print(s)

string = "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccsddddddddeeeeeeeeeeeee"

setSt = set(string) # Set construction - O(S) - S is the length of the string

print(setSt) # Output: {'a', 'b', 'c', 'd', 'e'}

# Loop over items in set - O(n)
for x in s:
    print(x) 
    
# Hashmaps - Dictionaries

d = {"matheus": 1, "greg": 2, "steve": 3}
print(d)

# Add key:val in dictionary: O(1)

d['arsh'] = 4

print(d)

# Check for presence of key in dictionary: O(1)
if "greg" not in d:
    print(True)

# Check the value corresponding to a key in the dictionary O()    
print(d['greg'])

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
    print("Key: ", key)
    print("Value: ", val)

# Defaultdict
from collections import defaultdict

default = defaultdict(int)

print(default[2])
print(default)

# Counter
from collections import Counter

counter = Counter(string)

print(counter)
