"""
Name: Wiley Lin
------------------------------
This program analyzes Romeo and Juliet script, and counts each word's occurrence.
Skills used in this file: file handling, functional data types and structures, lambda expressions, function.
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	with open(FILE, 'r') as f:
		word_d = {}
		for line in f:
			tokens = line.split()
			for token in tokens:
				token = string_manipulation(token)
				# print(token)
				if token not in word_d:
					word_d[token] = 1
				else:
					word_d[token] += 1
		print_out_d(word_d)


def string_manipulation(token):
	ans = ""
	for ch in token:
		if ch.isalpha() or ch.isdigit():
			ans += ch.lower()
	return ans


def print_out_d(d):
	for word, occurrence in sorted(d.items(), key=lambda ele: ele[1]):
		print(word, '→', occurrence)


if __name__ == '__main__':
	main()
