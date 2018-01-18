name = "ada lovelace"
print (name.title())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print full_name
message = "Hello" +  " " + full_name.title() + "!"
print message
score = 0
while True:
	print ("\nWho was" + " " + full_name.title() + "!")
	choice1 = raw_input("\nA) a party girl" +
						"\nB) first computer programmer" +
						"\nC) i dont know")
	if choice1 == 'B':
		print ("\tCorrect!")
		score +=1 
	elif choice1 == 'quit':
		break 
	print ("Who was Morgan Calla?")
	choice1 = raw_input("\nA) a piece of hair" +
						"\nB) someone crazy" +
						"\nC) i dont know")
	if choice1 == 'B':
		print ("\tCorrect!")
		score +=2 
