"""
File: prime_checker.py
Name: Quill
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


import math


# This constant controls when to stop
EXIT = -100


def main():
	"""
	n is an integer that is greater than 1.
	We will print Ture if n is a prime number; False if n is not a prime number.
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!')
			break
		i = 2	 # n is greater than 1, start checking from 2
		while i < n:
			if n % i == 0:
				print(str(n) + ' is not a prime number.')
				break
			i += 1	 # increase 'i' to check next number, until 'n-1'
		else:
			print(str(n) + ' is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
