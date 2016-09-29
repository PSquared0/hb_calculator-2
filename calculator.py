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
	try:
		if operator=='square' or operator=='cube':
			num1 = int(tokens[1])
		elif operator == 'q':
			break
		else:
			(num1, num2) = int(tokens[1]), int(tokens[2])
	except ValueError:
		print "Sorry, wrong input. Please use q for quit; square, cube, pow, mod, or an operator before your numbers."
		continue
	if operator == '+':
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