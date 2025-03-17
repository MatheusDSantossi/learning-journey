# Hashsets

s = set()

print(s)

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

# Lookup if item in set - O(1)
# if 1 in s:
if 1 not in s:
    print(True)

# Remove item from set - O(1)
s.remove(3)
print(s)


string = "aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbccccccc"
set2 = set(string) # Set construction - O(S) - S is the length of the string
print(set2)

# Loop over items in set - O(n) - N is the number of items in the set
for x in s:
    print(x)
    
# Hashmaps - Dictionaries
d = {'matheus': 1, 'steve': 2, 'rob': 3}
print(d)

# Add key:val into dictionary - O(1)
d['arsh'] = 4
print(d)

# Check for presence of key in dictionary: O(1)
if 'matheus' in d:
    print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['matheus'])

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
    print(f'{key}: {val}')

# Defaultdict
from collections import defaultdict

default = defaultdict(list)

print(default[2])

print(default)

# Counter
from collections import Counter

counter = Counter(string)

print(string)
print(counter)
