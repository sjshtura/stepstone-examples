def txt2morse(s):
	morse_alphabet = {'a': '.-', 'b': '-...',\
	'c': '-.-.', 'd': '-..', 'e':'.'}
	morse_string = ''
	for char in s:
		morse_code = morse_alphabet[char]
		morse_string += morse_code + ' '
	return morse_string

