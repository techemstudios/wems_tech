name = "Meira"
print(name.title())
first_name = "Meira"
last_name = "Boyle"
full_name = first_name + " " + last_name
print (full_name)
message = "Hello" + full_name.title() + "!"
print(message)
score = 0
while True :
	 print("\nWho was " + full_name.title() + "!")
	 choice1 = raw_input("\nA)first person to jump into th face of the earth " +
						"\nB)first competer programmer" +
						"\nC) first person to tango with a puma while drinking coffe and feedindher husband a moldy piece of bread" +
						"\n")
	 if choice1 == 'B':
		  print("\tCorrect!")
		  score += 1
	 elif choice1 == 'quit':
		  break
		  
	print("\nWho is Meira Boyle?")
	choice2 = raw_input("\nA)first person to become a fashion designer " +
						"\nB) a fourth grader" +
						"\nC) only peson at our school to have Boyle as a last name" +
						"\nfirst crazy person")
	 if choice1 == 'B':
		  print("\tCorrect!")
		  score += 1
	 elif choice1 == 'quit':
		  break
