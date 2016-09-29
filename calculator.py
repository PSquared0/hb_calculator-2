"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
	user_input = raw_input("Enter Math Function Here: ")
	tokens = user_input.split(" ")
	operator = tokens[0]
	if operator=='square' or operator=='cube':
		num1 = int(tokens[1])
	else:
		(num1, num2) = int(tokens[1]), int(tokens[2])
	if operator == 'q':
		break
	elif operator == '+':
		result = add(num1, num2)
		print result
	elif operator == '-':
		result = subtract(num1, num2)
		print result
	elif operator == '*':
		result = multiply(num1, num2)
		print result
	elif operator == '/':
		result = divide(num1, num2)
		print result
	elif operator == 'square':
		result = square(num1)
		print result
	elif operator == 'cube':
		result = cube(num1)
		print result
	elif operator == 'pow':
		result = power(num1, num2)
		print result
	elif operator == 'mod':
		result = mod(num1, num2)
		print result