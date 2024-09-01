"""
File: prime_checker.py
Name: Wiley Lin
Skills used in this file: while loops, if statement, input/output, variables, function.
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This function checks whether the input is a prime number or not.
	It assumes input is always bigger than 1 (1 not included)
	If input == -100 then it means EXIT
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			break
		else:
			if n == 2:
				print(str(n) + ' is a prime number.')
			elif n % 2 == 0:
				print(str(n) + ' is not a prime number.')
			elif calculation(n) >= 1:
				print(str(n) + ' is not a prime number.')
			else:
				print(str(n) + ' is a prime number.')
	print('Have a good one!')


def calculation(n):
	"""
	This function deals with input n not being 2, and not able to be divided by 2.
	It checks whether n is a prime number or not,
	If n is a prime number, then abc would be bigger than 0
	If not, then abc stays 0
	This function returns abc to main
	"""
	abc = 0
	for i in range(2, n, 1):
		tt = n % i
		if tt == 0:
			abc = abc + 1
	return abc


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
