# LIST ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# a = [1, 2, 3, 4, 5]
# print(a)

# b = ["apple", "banana", "mango"]
# print(b)

# c = [1, "hello", 3.5, True]
# print(c)

# d = []
# print(d)

# e = [[1,2],[3,4]]
# print(e)

# f = [True,False,True]
# print(f)

# g = list((1,2,3))
# print(g)
 
# h = list(range(1, 6))
# print(h)

# J = [1,2,3]
# print("Original Series:" , J)
# J.append(4)
# print("New Series:", J)

# K = [1,2,3]
# print("Original Series:" , K)
# K.insert(1,20)
# print("New Series:", K)

# L = [1,2,3]
# print("Original Series:" , L)
# L.extend([4,5,6])
# print("New Series:", L)

# M = [1,2,3]
# print("Original Series:" , M)
# M.remove(3)
# print("New Series:", M)

# a = [1, 2]
# print("Original:", a)
# a.append([3, 4])
# print("After append:", a)

# TUPLE ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# t = (1, 2, 3)
# print("Tuple:", t)

# t = ("apple", "banana", "mango")
# print("Tuple:", t)

# t = (1, "hello", 3.5, True)
# print("Tuple:", t)

# t = (5,)
# print("Single element tuple:", t)

# t = (5)
# print("Type:", type(t))

# Nested Tuple
# t = ((1, 2), (3, 4))
# print("Nested tuple:", t)

# Duplicate Values
# t = (1,2,3,3,4,5,6,6)
# print("Tuple:", t)

# tuple() Constructor
# t = tuple([1, 2, 3])
# print("Tuple:", t)

# Tuple Indexing
# t = (10, 20, 30)
# print("First element:", t[0])

# Tuple Slicing
# t = (1, 2, 3, 4, 5)
# print("Slice:", t[1:4])

# Tuple Length
# t = (1, 2, 3)
# print("Length:", len(t))

# Tuple Concatination
# t1 = (1, 2)
# t2 = (3, 4)
# print("Combined:", t1 + t2)

# Tuple Repetition
# t = (1, 2)
# print("Repeated:", t * 3)

# Tuple to List
# t = (1, 2, 3)
# print("Original:", t)
# l = list(t)
# l.append(4)
# t = tuple(l)
# print("Modified tuple:", t)

# SET ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# 1. Simple Set
# s = {1, 2, 3}
# print("Set:", s)

# # 2. Duplicate Values Removed Automatically
# s = {1, 2, 2, 3, 3}
# print("Set (duplicates removed):", s)

# # 3. String Set
# s = {"apple", "banana", "mango"}
# print("Set:", s)

# # 4. Mixed Data Types
# s = {1, "hello", 3.5, True}
# print("Set:", s)

# # 5. Empty Set (Important ❗)
# s = set()
# print("Empty set:", s)

# # 6. Add Element
# s = {1, 2}
# print("Original:", s)
# s.add(3)
# print("After add:", s)

# # 7. Remove Element
# s = {1, 2, 3}
# print("Original:", s)
# s.remove(2)
# print("After remove:", s)

# # 8. Discard Element (No Error if Not Found)
# s = {1, 2, 3}
# print("Original:", s)
# s.discard(3)
# print("After discard:", s)

# # 9. Pop Element (Random Removal)
# s = {10, 20, 30}
# print("Original:", s)
# s.pop()
# print("After pop:", s)

# # 10. Union of Sets
# a = {1, 2}
# b = {3, 4}
# print("Union:", a | b)

# # 11. Intersection of Sets
# a = {1, 2, 3}
# b = {2, 3, 4}
# print("Intersection:", a & b)

# # 12. Difference of Sets
# a = {1, 2, 3}
# b = {2, 3}
# print("Difference:", a - b)

# # 13. Convert List to Set
# l = [1, 2, 2, 3]
# s = set(l)
# print("Converted set:", s)

# # 14. Clear Set
# s = {1, 2, 3}
# print("Original:", s)
# s.clear()
# print("After clear:", s)

# DICTIONARY ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# 1. Simple Dictionary
# d = {"a": 1, "b": 2}
# print("Dictionary:", d)
# print("")

# # 2. Access Value using Key
# d = {"name": "Harsh", "age": 22}
# print("Name:", d["name"])
# print("")

# # 3. Add New Key-Value
# d = {"a": 1}
# print("Original:", d)
# d["b"] = 2
# print("After adding:", d)
# print("")

# # 4. Update Value
# d = {"a": 1}
# print("Original:", d)
# d["a"] = 100
# print("After update:", d)
# print("")

# # 5. Mixed Data Types
# d = {"a": 1, "b": "hello", "c": 3.5}
# print("Dictionary:", d)
# print("")

# # 6. Nested Dictionary
# d = {"user": {"name": "Harsh", "age": 22}}
# print("Nested:", d)
# print("")

# # 7. Using get() Method
# d = {"a": 1}
# print("Value:", d.get("a"))
# print("")

# # 8. Remove Item using pop()
# d = {"a": 1, "b": 2}
# print("Original:", d)
# d.pop("a")
# print("After pop:", d)
# print("")

# # 9. Remove Last Item (popitem())
# # It removes from last
# d = {"a": 1, "b": 2}
# print("Original:", d)
# d.popitem()
# print("After popitem:", d)
# print("")

# # 10. Keys, Values, Items
# d = {"a": 1, "b": 2}
# print("Keys:", d.keys())
# print("Values:", d.values())
# print("Items:", d.items())
# print("")

# # 11. Update using update()
# d = {"a": 1}
# print("Original:", d)
# d.update({"b": 2, "c": 3})
# print("After update:", d)
# print("")

# # 12. Clear Dictionary
# d = {"a": 1, "b": 2}
# print("Original:", d)
# d.clear()
# print("After clear:", d)
# print("")

# # 13. Dictionary using dict() Constructor
# d = dict(name="Harsh", age=22)
# print("Dictionary:", d)

# STRING ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# 1. Simple String
# s = "Hello"
# print("String:", s)
# print("")

# # 2. String Indexing
# s = "Python"
# print("First character:", s[0])
# print("")

# # 3. String Slicing
# s = "Python"
# print("Slice:", s[1:4])
# print("")

# # 4. String Length
# s = "Hello"
# print("Length:", len(s))
# print("")

# # 5. Uppercase
# s = "hello"
# print("Upper:", s.upper())
# print("")

# # 6. Lowercase
# s = "HELLO"
# print("Lower:", s.lower())
# print("")

# # 7. Replace Characters
# s = "hello"
# print("Replace:", s.replace("h", "H"))
# print("")

# # 8. Split String
# s = "a b c"
# print("Split:", s.split())
# print("")

# # 9. Join Strings
# l = ["a", "b", "c"]
# print("Join:", " ".join(l))
# print("")


# # 10. Remove Spaces (strip)
# s = "  hello  "
# print("Strip:", s.strip())
# print("")

# # 11. Count Characters
# s = "banana"
# print("Count of 'a':", s.count("a"))
# print("")

# # 12. Find Position
# s = "python"
# print("Index of 't':", s.find("t"))
# print("")

# # 13. String Concatenation
# s1 = "Hello"
# s2 = "World"
# print("Combined:", s1 + " " + s2)
# print("")

# # 14. Reverse String
# s = "hello"
# print("Reversed:", s[::-1])