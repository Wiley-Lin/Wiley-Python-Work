"""
File: weather_master.py
Name: Wiley Lin
Skills used in this file: while loops, if statement, input/output, variables.
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = -100


def main():
	"""
	This function calculates four factors:
	highest temperature, lowest one, temperature average,
	and number of cold days (temperature lower than 16)
	"""
	print("\"Weather Master\"")
	days = 0
	temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
	if temperature != EXIT:
		if temperature < 16:
			days = 1
		maximum = temperature
		minimum = temperature
		first_temperature = temperature
		times = 1
		ans = 0
		while True:
			temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
			if temperature == EXIT:
				break
			times = times + 1
			if temperature < 16:
				days = days + 1
			if temperature > maximum:
				maximum = temperature
			if temperature < minimum:
				minimum = temperature
			if temperature != EXIT:
				ans = ans + temperature
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average: ' + str((ans + first_temperature) / times))
		print(str(days) + ' cold day(s)')
	else:
		print('No numbers were entered')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
