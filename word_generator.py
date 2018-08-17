import random

def generate_word(freq_map):

	word = []

	letter = " "

	while True:

		letter = get_next_letter(letter,freq_map)

		if letter = " ":

			return word.join("")

		else:

			word.append(letter)

def get_next_letter(letter,freq_map):

	next_letter_distribution = freq_map[letter]

	k = random.random()

	for i, letter_prob in next_letter_distribution:

		k -= letter_prob

		if k <= 0:

			if i == len(next_letter_distribution) - 1:
				return " "

			return chr(ord('a') + i)

	return " "


def generate_frequency_map(textfile):

	#create a empty list for all letters of the alphabet
	freq_map = {chr(i + ord('a'): [0 for j in range(27)] for i in range(26))}

	#add space character to map
	freq_map[" "] = [0 for j in range(27)]

	file = open("textfile")

	last_letter = " "

	for line in file:

		letter_array = clean_line(line)

		for k in letter_array:

			















