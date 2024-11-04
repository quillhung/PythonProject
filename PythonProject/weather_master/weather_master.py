"""
File: weather_master.py
Name: Quill
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program will ask weather data from user to compute the highest,
	lowest, average, cold days among the inputs.
	"""
	print("stanCode \"Weather Master 4.0\"!")
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		count = 1
		total = data
		highest = data
		lowest = data
		average = total / count
		cold_days = 0
		while data != EXIT:
			data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			if data == EXIT:
				break
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < 16:
				cold_days += 1
			count += 1	 # count = count+1
			total += data	 # to sum all data
			average = total / count
		print('Highest temperature = '+str(highest))
		print('Lowest temperature = '+str(lowest))
		print('Average = '+str(average))
		print(str(cold_days)+' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
