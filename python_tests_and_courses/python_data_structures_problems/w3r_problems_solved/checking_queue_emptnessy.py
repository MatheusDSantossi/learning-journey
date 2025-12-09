import queue

p = queue.Queue()
q = queue.Queue()

for x in range(4):
    p.put(x)
    
print(p.empty())
print(q.empty())
