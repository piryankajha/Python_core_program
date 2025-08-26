# Python_Conditional_Statements.py
"""
Topic: Conditional Statements in Python
Author : Piryanka Jha   
"""

# ---------------------------
# What are Conditional Statements?
# ---------------------------
# Conditional statements are used to perform different actions based on different conditions.
# Python uses if, elif, and else keywords for decision making.

# ---------------------------
# Basic if Statement
# ---------------------------
age = 23
if age >= 18:
    print("" eligible to vote.")

# ---------------------------
# if-else Statement
# ---------------------------
num = 9
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ---------------------------
# if-elif-else Ladder
# ---------------------------
marks = 78
if marks >= 985:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D or below")

# ---------------------------
# Nested if Statements
# ---------------------------
x = 10
y = 20
if x > 7:
    if y > 18:
        print("Both conditions are True")

# ---------------------------
# Using Logical Operators with Conditions
# ---------------------------
username = "Piryanka"
password = "6655"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


#____________________________________________________________________________________________________________________________
                                                QUESTIONS

