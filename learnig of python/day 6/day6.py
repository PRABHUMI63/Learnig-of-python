# Day 6: Lists in Python
# Part 1: What is a List?
# A list is a collection of items in a particular order. It can hold items of different types (integers, strings, etc.) and is one of the most versatile data structures in Python.

# Example:
my_list = [10, 20, 30, 40, 50]
print(my_list)

# Part 2: Accessing List Elements
# You can access elements of a list using indexing (starting from 0 for the first element).

# Example:
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Output will be 10

# Part 3: Modifying Lists
# You can change a list’s elements by assigning new values to specific indexes.

# Example:
my_list = [10, 20, 30]
my_list[1] = 100
print(my_list)  # Output will be [10, 100, 30]
# Part 4: List Methods
# Python provides various methods to work with lists, like append(), insert(), remove(), etc.

# Example:
# append() adds an element at the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

meri_list= [ 5 , 6, 3 ,9]
meri_list.append(33)
print(meri_list)

meri_list.insert(1,4)
print(meri_list)
print(meri_list[2])