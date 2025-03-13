# Trees and Linked Lists are a subclass of graphs

# Time complexity: O(V + E) NOTE: V is equal to vertex and E is equal to edge which means V + E because we're visiting all the edges of that vertex
# Space: O(V + E)

# Array of edges (Directed) [Start, End]

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

print(A)

# Convert Array of Edges -> Adjancecy Matrix

M = []

for i in range(n):
    M.append([0] * n)
    
for u, v in A:
    M[u][v] = 1
    
    # Uncomment the following line if the graph is undirected
    # M[v][u] = 1
    
print(M)

# Convert Array of Edges -> Adjancecy List
from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    
    # Uncomment the following line if the graph is undirected
    # D[v].append(u)
    
print(D)

print(M[3])
print(D[3])

# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges


def dfs_recursive(node):
    print(node)
    for neig_node in D[node]:
        if neig_node not in seen:
            seen.add(neig_node)
            dfs_recursive(neig_node)
        
source = 0
seen = set()
seen.add(source)

dfs_recursive(source)

# Iterative DFS with Stack - O(V + E)

source = 0

seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for neighbor_node in D[node]:
        if neighbor_node not in seen:
            seen.add(neighbor_node)
            stack.append(neighbor_node)
            
# BFS with Queue - O(V + E)

source = 0

from collections import deque

seen = set()
seen.add(source)

q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for neighbor_node in D[node]:
        if neighbor_node not in seen:
            seen.add(neighbor_node)
            q.append(neighbor_node)

# Store graps in memory

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        
    def __str__(self):
        return f"Node({self.data})"
    
    def display(self):
        connections = [node.data for node in self.neighbors]
        return f"{self.data} is connected to {connections}"
    
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)	
D.neighbors.append(C)

print(A.display())