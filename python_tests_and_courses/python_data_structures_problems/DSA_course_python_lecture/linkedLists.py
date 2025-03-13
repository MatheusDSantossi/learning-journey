# Singly & Doubly Linked

class SinglyNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)

Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
D = SinglyNode(5)

Head.next = A
A.next = B
B.next = C
C.next = D

print(Head)

# Traverse the list - O(n)
curr = Head

while curr:
    print(curr)
    curr = curr.next
    
# Display linked list - O(n)
def display(head):
    curr = head
    elements = []
    
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
        
    print("-> ".join(elements))
    
display(Head)

# Search for node values - O(n)
def search(head, val):
    curr = head
    
    while curr:
        if val == curr.data:
            return True
        curr = curr.next
        
    return False

print(search(Head, 2))

# Doubly Linked Lists
print("-------- Doubly Linked Lists -----------")

class DoublyNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return str(self.data)
    

head = tail = DoublyNode(1)
print(head)
print(tail)

# Display - O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
        
    print(" <-> ".join(elements))
    
display(head)

# Insert at beggining - O(1)

def insert_at_beginning(head, tail, data):
    new_node = DoublyNode(data, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)

def insert_at_end(head, tail, data):
    new_node = DoublyNode(data, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)
