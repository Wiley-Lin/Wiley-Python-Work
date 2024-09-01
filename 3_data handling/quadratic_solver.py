"""
File: quadratic_solver.py
Name: Wiley Lin
Skills used in this file: if statement, input/output, variables.
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
	The formula: ax2+bx+c=0
	This function checks three input numbers a, b, c used to fill the formula above,
	doing calculation to see how many roots the formula has.
	"""
	print('Quadratic Solver')
	a = int(input('Enter a :'))
	b = int(input('Enter b :'))
	c = int(input('Enter c :'))
	r = b * b - 4 * a * c

	if r > 0:
		print('Two roots: ' + str((-b + math.sqrt(r))/(2*a)), str((-b - math.sqrt(r))/2*a))
	elif r == 0:
		print('One root: ' + str((-b + math.sqrt(r))/(2*a)))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
