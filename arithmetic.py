def add(list):
    """ Return sum of multiple intergers"""
    answer = 0
    for item in range(len(list)):
        answer = answer + int(list[item])
    return answer 

def subtract(list):
    """ Return subraction of multiple intergers"""
    answer = 0
    for item in range(len(list)):
        answer = answer - int(list[item])
    return answer 

def multiply(list):
    """ Return product of the inputs"""
    answer = 1
    for item in range(len(list)):
        answer = answer * int(list[item])
    return answer

def divide(num1, num2):
    """ divides the first input by the second, returning a floating number"""
    return num1 / float(num2)

def square(num1):
    """ Return square of the interger"""
    return num1 * num1

def cube(num1):
    """ Return cube of the interger"""
    return num1 ** 3

def power(num1, num2):
    """ Returns the result of raising the first input to the power of the second input"""
    return num1 ** num2

def mod(num1, num2):
    """ Returns the remainder when the first input is divided by the second input
"""
    return num1 % num2
