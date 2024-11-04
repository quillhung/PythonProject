"""
File: quadratic_solver.py
Name: Quill
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


import math


def main():
	"""
	This program should implement a console program
	that asks 3 inputs (a, b, and c) from users to compute
	the roots of equation: ax^2 + bx + c = 0
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = b**2 - 4*a*c
	if discriminant > 0:
		y = math.sqrt(discriminant)
		x1 = (-b + y) / (2*a)
		x2 = (-b - y) / (2*a)
		print('Two roots: ' + str(x1) + ', ' + str(x2))
	if discriminant == 0:
		x = -b / (2*a)
		print('One roots: ' + str(x))
	if discriminant < 0:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
