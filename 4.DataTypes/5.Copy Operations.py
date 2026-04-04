# SHALLOW COPY➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# import copy
# a = [[1, 2], [3, 4]]
# b = copy.copy(a)
# b[0][0] = 100
# print("Original:", a)
# print("Copy:", b)

# 1. Simple List Copy
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a)

# 2. Modify Element (No Nested)
# a = [10, 20]
# b = a.copy()
# b[0] = 99
# print(a)

# 3. Nested List Change
# a = [[1, 2], [3, 4]]
# b = a.copy()
# b[0][0] = 100
# print(a)

# 4. Using copy Module
# import copy
# a = [[1, 2], [3, 4]]
# b = copy.copy(a)
# b[1][1] = 50
# print(a)

# Output: [[1, 2], [3, 50]]

# 5. Append Nested List
# a = [[1, 2]]
# b = a.copy()

# b.append([3, 4])
# print(a)

# Output: [[1, 2]]

# 6. Change Nested List
# a = [[1, 2]]
# b = a.copy()

# b[0].append(3)
# print(a)

# Output: [[1, 2, 3]]

# 7. Mixed List
# a = [1, [2, 3], 4]
# b = a.copy()

# b[1][0] = 99
# print(a)

# Output: [1, [99, 3], 4]

# 8. Using Slice Copy
# a = [1, 2, 3]
# b = a[:]

# b.append(5)
# print(a)

# Output: [1, 2, 3]

# 9. Slice with Nested
# a = [[1, 2], [3, 4]]
# b = a[:]

# b[0][1] = 99
# print(a)

# Output: [[1, 99], [3, 4]]

# 10. Multiple References
# a = [[1, 2]]
# b = a.copy()
# c = b

# c[0][0] = 10
# print(a)

# Output: [[10, 2]]

# 11. Dictionary Shallow Copy
# a = {"x": [1, 2]}
# b = a.copy()

# b["x"][0] = 99
# print(a)

# Output: {'x': [99, 2]}

# 12. Add Key in Copy
# a = {"a": 1}
# b = a.copy()

# b["b"] = 2
# print(a)

# Output: {'a': 1}

# 13. Tuple Inside List
# a = [(1, 2), [3, 4]]
# b = a.copy()

# b[1][0] = 100
# print(a)

# Output: [(1, 2), [100, 4]]

# 14. Deep Nested Structure
# a = [1, [2, [3, 4]]]
# b = a.copy()

# b[1][1][0] = 99
# print(a)

# Output: [1, [2, [99, 4]]]

# 15. Replace Whole Nested Object
# a = [[1, 2], [3, 4]]
# b = a.copy()

# b[0] = [9, 9]
# print(a)

# Output: [[1, 2], [3, 4]]


# DEEP COPY➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# import copy
# a = [[1, 2], [3, 4]]
# b = copy.deepcopy(a)
# b[0][0] = 100
# print("Original:", a)
# print("Copy:", b)



# DIRECT ASSIGNMENT➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
