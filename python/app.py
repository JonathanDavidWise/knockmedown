#!/usr/bin/env python3

from math import *

print(ceil(37))


name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name + "! You are " + age +".")

lucky_numbers = [3, 4, 6, 11, 8, 9]
friends = ["a", "z", "c"]

# Index of list starting from 0
print(friends[2])

# Merge two lists
friends.extend(lucky_numbers)
print(friends)

# Append variable to list
friends.append(lucky_numbers)
print(friends)

# Insert at index
friends.insert(1, "les")
print(friends)

# Insert at index
friends.insert(1, "a")
print(friends)

# Remove first match from list
friends.remove("a")
print(friends)

# Remove last from list
friends.pop()
print(friends)

# Insert at index
friends.insert(1, "a")
print(friends)

# First in list
print(friends.index("a"))

# Count amount in list
print(friends.count("a"))

# Sort List
lucky_numbers.sort()
print(lucky_numbers)

# Reverse List
lucky_numbers.reverse()
print(lucky_numbers)

# Copy without linking
friends2 = friends.copy()

print(friends2)

# Tuples

coordinates = [(4,5), (5,4)]

print(coordinates[1][1])

friends3 = friends2

print(friends)
print(friends2)
print(friends3)

def sayhi(name, age):
    print("Hello " + name + "! You are " + str(age) + ".")

sayhi("Mike", 32)
sayhi("Steve", 40)

def sayhi(name, age):
    print("Hello " + name + "! You are " + age + ".")

sayhi("Mike", '34')
sayhi("Steve", '50')

def cube(num):
    return num*num*num

result = cube(4)
print(result)

is_male = False
is_tall = True


if is_male and is_tall:
    print("Male & Tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall and not male")
else:
    print("You are not male and tall.")
