#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation based on operator
if operator == '+':
    print("Result: ", add(num1, num2))
elif operator == '-':
    print("Result: ", subtract(num1, num2))
elif operator == '*':
    print("Result: ", multiply(num1, num2))
elif operator == '/':
    print("Result: ", divide(num1, num2))
else:
    print("Invalid operator. Please enter +, -, *, or /.")


# In[ ]:




