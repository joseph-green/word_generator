import random

def generate_word(freq_map):

 	word = []

 	letter = " "

 	while True:

 		letter = get_next_letter(letter,freq_map)

 		if letter == " ":

 			return "".join(word)

 		else:

 			word.append(letter)

def get_next_letter(letter,freq_map):

	next_letter_distribution = freq_map[letter]

	k = random.random()

	for i, letter_prob in enumerate(next_letter_distribution):

		k -= letter_prob

		if k <= 0:

			if i == len(next_letter_distribution) - 1:

				return " "

			return chr(ord('a') + i)

	return " "


	

			















