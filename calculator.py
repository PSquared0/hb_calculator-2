"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
	user_input = raw_input("Enter Math Function Here: ")
	tokens = user_input.split(" ")
	if tokens[0] == 'q':
		break
	elif tokens[0] == '+':
		result = add(int(tokens[1]), int(tokens[2]))
		print result
	elif tokens[0] == '-':
		result = subtract(int(tokens[1]), int(tokens[2]))
		print result
	elif tokens[0] == '*':
		result = multiply(int(tokens[1]), int(tokens[2]))
		print result