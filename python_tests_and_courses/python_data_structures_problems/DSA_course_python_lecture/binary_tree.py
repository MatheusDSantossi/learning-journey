# Binary Trees

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)
    
    
#       1
#   2       3        
# 4    5  10

A = TreeNode(1)

B = TreeNode(2)

C = TreeNode(3)

D = TreeNode(4)

E = TreeNode(5)

F = TreeNode(10)

A.left = B

A.right = C

B.left = D

B.right = E

C.left = F

print(A)

# Recursive Pre Order Traversal (DFS) Time: O(n), Space: O(n)

print("Recursive Pre Order Traversal (DFS)")

def pre_order_traversal(node):
    if not node:
        return

    print(node)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

pre_order_traversal(A)

# Recursive In Order Traversal (DFS) Time: O(n), Space: O(n)

print("Recursive In Order Traversal (DFS)")

def in_order_traversal(node):
    if not node:
        return

    in_order_traversal(node.left)
    print(node)
    in_order_traversal(node.right)
    
in_order_traversal(A)

# Recursive Post Order Traversal (DFS) Time: O(n), Space: O(n)

print("Recursive Post Order Traversal (DFS)")

def post_order_traversal(node):
    if not node:
        return

    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node)

post_order_traversal(A)

# Iterative Pre Order Traversal (DFS) Time: O(n), Space: O(n)

print("Iterative Pre Order Traversal (DFS)")

def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        
pre_order_iterative(A)

# Level Order Traversal (BFS) Time: O(n), Space: O(n)

print("Level Order Traversal (BFS)")

from collections import deque

def level_order(node):
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order(A)

# Check if value Exists (DFS) Time: O(n), Space: O(n)

print("Check if value Exists (DFS)")

def search(node, target):
    if not node:
        return False
    
    if node.data == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

print(search(A, 5))

# Binary Search Tree (BSTs)
print("Binary Search Tree (BSTs)")

#            5
#       1         8
#   -1     3   7    9

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print(A2)

in_order_traversal(A2)

# Time: O(log n), Space: O(log n)

def search_bst(node, target):
    if not node:
        return False
    
    if node.data == target:
        return True
    
    if target < node.data: return search_bst(node.left, target)
    
    else: return search_bst(node.right, target)

print(search_bst(A2, 4))
