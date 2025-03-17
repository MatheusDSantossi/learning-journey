class HashSet():
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * self._capacity
        
    def add(self, i):
        h = hash(i)
        idx = h % self._capacity
        
        if self._data[idx] is not None:
            if i not in self._data[idx]:
                self._data[idx].append(i)
                
        else:
            self._data[idx] = [i]
            
    def remove(self, i):
        h = hash(i)
        idx = h % self._capacity
        
        if self._data[idx] is not None:
            if i in self._data[idx]:
                self._data[idx].remove(i)
        return False
    
    def __contains__(self, i):
        h = hash(i)
        idx = h % self._capacity
        
        if self._data[idx] is not None:
            if i in self._data[idx]:
                return True
                
        return False
    
    def __str__(self):
        return "{}" + ", ".join(str(i) for lst in s._data if lst is not None for i in lst) + "}" 
    
h = HashSet(100000000)
lst = [i for i in range(100000000)]
print(lst[:10])

for i in lst:
    h.add(i)
    
print(17 in h)
print(9999999 in h)

h.remove(9999999)
print(9999999 in h)

print(hash(9999999))
print(h._data[99999999])
