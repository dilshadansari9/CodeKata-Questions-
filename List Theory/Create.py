#  What is a List in Python?
# A list is a built-in ordered, mutable, and heterogeneous data structure in Python used to store multiple items in a single variable.

# Key Characteristics
# Ordered: Items have a defined order (index).
# Mutable: Can be changed after creation.
# Allows duplicates.
# Heterogeneous: Can contain different data types.

my_list = [1, 2, 3, 'apple', 5.6] 

# Empty list 
empty = []

# With values
fruits = ['apple', 'banana', 'cherry']

# Mixed data types
mixed = [1, "hello", 3.14, True]

# Using list() constructor
nums = list((1, 2, 3))  # Note double brackets

# Nested list (2D list)
matrix = [[1, 2], [3, 4]]

# Indexing 
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last element)

# Slicing 
print(fruits[1:3])     # ['banana', 'cherry']
print(fruits[:2])      # ['apple', 'banana']
print(fruits[::-1])    # ['cherry', 'banana', 'apple'] (reversed)

# List Operations 
a = [1, 2, 3]
b = [4, 5]
print(a + b)     # Concatenation: [1, 2, 3, 4, 5]
print(a * 2)     # Repetition: [1, 2, 3, 1, 2, 3]

# Membership 
print(2 in a)    # True
print(6 not in a)  # True

