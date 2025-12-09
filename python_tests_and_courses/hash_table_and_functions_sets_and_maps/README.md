# Python Hashmaps & Hashsets 🗺️🔢

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Data Structures](https://img.shields.io/badge/Data%20Structures-Hashmaps%20%26%20Hashsets-brightgreen)

**A hands-on collection of Hashmap and Hashset implementations in Python**  
*Exploring hash functions, collision handling, and real-world use cases*

## 🚀 Overview

This repository contains Python implementations of Hashmaps and Hashsets, fundamental data structures widely used in algorithmic problem-solving and efficient data storage. The code is inspired by [Greg Hogg's DSA lecture](https://www.youtube.com/watch?v=iZyxNEBpqFY), which provides an excellent breakdown of hashing concepts.

## 📂 Folder Structure

| File | Description |
|------|------------|
| `hashmap_example.py` | Demonstrates the implementation and use cases of Hashmaps |
| `hashset_example.py` | Covers the working principles of Hashsets |
| `hashsets_and_hashmaps.py` | Comparative analysis and use cases of both structures |
| `heaps_example.py` | Introduction to Heaps in relation to Hashmaps |

## 🛠 Key Concepts Covered

1. **Hash Functions** - How keys are mapped to indices
2. **Collision Resolution** - Handling hash collisions effectively
3. **Time Complexity** - Why Hashmaps and Hashsets are fast for lookups
4. **Memory Efficiency** - Trade-offs in storage and speed
5. **Real-World Applications** - When and why to use these structures

## 🔬 Code Demonstration

Example: Simple Hashmap Implementation
```python
class SimpleHashMap:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
```
## 📚 Reference
This work is based on the concepts explained in Greg Hogg’s YouTube tutorial:
📺 Hash Tables: Hash Functions, Sets, & Maps

📬 **Let's Connect!**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Matheus_Santossi-blue?style=flat&logo=linkedin)](https://linkedin.com/in/matheussantossi) 
[![GitHub Issues](https://img.shields.io/github/issues/MatheusDSantossi/learning-journey)](https://github.com/MatheusDSantossi/learning-journey/issues)
