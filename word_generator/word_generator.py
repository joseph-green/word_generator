import random

def generate_word(freq_map):

	word = []

	for letter in generate_letters(letter,freq_map)

		if letter == " ":

			return "".join(word)

		else:

			word.append(letter)

def generate_letters(letter,freq_map):

	next_letter_distribution = freq_map[letter]

	k = random.random()

	for i, letter_prob in enumerate(next_letter_distribution):

		k -= letter_prob

		if k <= 0:

			if i == len(next_letter_distribution) - 1:

				yield " "

			else:

				yield chr(ord('a') + i)



	

			















