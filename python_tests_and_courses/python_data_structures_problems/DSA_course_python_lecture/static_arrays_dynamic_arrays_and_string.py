# Static/Dynamic arrays
A = [1, 2, 3]

print(A)

# Append - Insert element at end of array - On average time: O(1)
A.append(5)

print(A)

# Popping - Deleting element at end of array - Time: O(1)
A.pop()

print(A)

# Insertion at specific index - Time: O(n)
A.insert(1, 4)

print(A)

# Modify an element - Time: O(1)
A[1] = 6

print(A)

# Acessing element ginen index i 0 O(1)
print(A[2])

# Checking if array has an element - Time: O(n)

if 7 in A:
    print("Element found")


# Remove - Deleting element by value - Time: O(n)
print("Remove: ", A.remove(3))

print(A)

# Checking length - Time: O(1)
print(len(A))

# Strings 

# Append to end of string - Time: O(n)
s = 'Hello'

b = s + "World"

print(b)

# Check if something is in string - Time: O(n)
if 'e' in s:
    print("Character found")
    
# Acess positions
print(s[2])

# Checking length - Time: O(1)
print(len(s))
