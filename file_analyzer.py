def scale_frequency_map(freq_map):

	for key, val in freq_map.items():

		s = sum(val)

		print(s)

		freq_map[key] = list(map(lambda x: x / s, val))

def generate_frequency_map(textfile):

	#create a empty list for all letters of the alphabet
	freq_map = {chr(i + ord('a')): [0 for j in range(27)] for i in range(26)}

	#add space character to map
	freq_map[" "] = [0 for j in range(27)]

	for line in open(textfile):

		letter_array = list(line)

		last_letter = letter_array[0]

		freq_map[" "][ord(last_letter) - ord('a')] += 1

		for k in letter_array[1:-1]:

				freq_map[last_letter][ord(k) - ord('a')] += 1

				last_letter = k

		freq_map[last_letter][-1] += 1



	scale_frequency_map(freq_map)

	return freq_map
