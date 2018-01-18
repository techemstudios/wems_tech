print "Can you guess my secret number?"

secret_number = 14

guess_number = int(raw_input('Enter your number: '))

if secret_number == guess_number:
	print 'YOU WIN!'
else:
	print 'YOU LOOSE!'
