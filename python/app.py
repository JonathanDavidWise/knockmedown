#!/usr/bin/env python3

from math import *

# print(ceil(37))


# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("Hello " + name + "! You are " + age +".")

# lucky_numbers = [3, 4, 6, 11, 8, 9]
# friends = ["a", "z", "c"]

# # Index of list starting from 0
# print(friends[2])

# # Merge two lists
# friends.extend(lucky_numbers)
# print(friends)

# # Append variable to list
# friends.append(lucky_numbers)
# print(friends)

# # Insert at index
# friends.insert(1, "les")
# print(friends)

# # Insert at index
# friends.insert(1, "a")
# print(friends)

# # Remove first match from list
# friends.remove("a")
# print(friends)

# # Remove last from list
# friends.pop()
# print(friends)

# # Insert at index
# friends.insert(1, "a")
# print(friends)

# # First in list
# print(friends.index("a"))

# # Count amount in list
# print(friends.count("a"))

# # Sort List
# lucky_numbers.sort()
# print(lucky_numbers)

# # Reverse List
# lucky_numbers.reverse()
# print(lucky_numbers)

# # Copy without linking
# friends2 = friends.copy()

# print(friends2)

# # Tuples

# coordinates = [(4,5), (5,4)]

# print(coordinates[1][1])

# friends3 = friends2

# print(friends)
# print(friends2)
# print(friends3)

# def sayhi(name, age):
#     print("Hello " + name + "! You are " + str(age) + ".")

# sayhi("Mike", 32)
# sayhi("Steve", 40)

# def sayhi(name, age):
#     print("Hello " + name + "! You are " + age + ".")

# sayhi("Mike", '34')
# sayhi("Steve", '50')

# def cube(num):
#     return num*num*num

# result = cube(4)
# print(result)

# is_male = False
# is_tall = True


# if is_male and is_tall:
#     print("Male & Tall")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are a tall and not male")
# else:
#     print("You are not male and tall.")

# def max_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

# print(max_num(300, 2000, 1000))

# num1 = float(input("Enter first number:"))
# op = input("Enter operator:")
# num2 = float(input("Enter second number:"))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid Operator")

# # Create Dictionary
# monthConversions = {
#     "Jan": "January",
#     1: "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }

# print(monthConversions["Nov"])
# print(monthConversions.get("Dec"))
# print(monthConversions.get("Mar", "Not a valid key"))
# print(monthConversions.get(1, "Not a valid key"))

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print("Done with loop")

# # Secret word game

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True    

# if out_of_guesses:
#     print("You lose")
# else:
#     print("You win!")

# friends = ["a", "bubba", "c"]

# for letter in "Giraffe Acadamy":
#     print(letter)
# print("")

# for friend in friends:
#     print(friend)
# print("")

# for index in range(3, 10):
#     print(index)
# print("")

# for index in range(len(friends)):
#     print(friends[index])
# print("")

# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("not first")
# print("")

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for i in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(2, 12))

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# print(number_grid[0][2])

# for row in number_grid:
#     for col in row:
#         print(col)

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))

# Try Except block

# try:
#     number = int(input("Enter a number: "))
#     print(number)
#     value = 10/0
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid Input")

# Reading from other files

# employee_file = open("employees.txt", "r")
# r is read
# w is write
# a is append
# r+ is read and write
'''
# print(employee_file.readable())
use in code
'''
# for employee in employee_file.readlines():
#     print(employee)

# # Read each line and enters cursor to next
# print(employee_file.readline())
# print(employee_file.readline())

# # Read all lines and enters
# print(employee_file.readlines())

# # Each of these moves the cursor down the file.

# employee_file.close()


# # Writeing to files or makeing new files
# employee_file = open("employees1.html", "w")
# employee_file.write("<p>This is HTML</p>")
# employee_file.close()
# employee_file = open("employees.txt", "r")
# print(employee_file.read())
# employee_file.close()

# import useful_tools

# print(useful_tools.roll_die(99))

# # Objects

# from Student import Student

# student1 = Student("Jim", "Business", 3.8, False)
# student2 = Student("Pam", "Art", 3.0, False)
# print(student1.gpa)
# print(student2.gpa)

# print(student1.on_honor_roll())

# # Multiple choice quiz
# from Question import Question

# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#             answer = input(question.prompt)
#             if answer == question.answer:
#                 score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

# run_test(questions)

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
