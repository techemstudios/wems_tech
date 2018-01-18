name = "viktor vaniakin"
print (name.title())
first_name = "Jonathan"
last_name = "Pilch"
fullname = first_name + " " + last_name
print fullname
message = "hello " + fullname.title() + "!"
print (message)
score = 0
while True:
	print ("\nwho was " + fullname.title() + "!")
	choice1 = raw_input("\nA) first boy to be super duper weird " +
										"\nB) weird " +
										"\nc) why... ")
	if choice1 == 'c':
		print("\tCorrrrrect!")
		score += 1e
	elif choice1 == 'b':
		break
	elif choice1 == 'a':
