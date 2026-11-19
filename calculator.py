"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    return a+b
def sub(a, b): 
    return a-b

def mul(a, b):
    return a*b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a
def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return log(b, a)
def exp(a, b): 
    return a**b

def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b

def logarithm(a,b): 
    return log(b, a)
def exponent(a,b):
    return a**b

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError:
        raise ValueError

def square_root(a):
    if a>=0:
        return math.sqrt(a)
    else:
        raise ValueError
