name = "ada lovelace"
print (name.title())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " +last_name
print full_name
print "Hello Ada Lovlace"
score = 0
while True:
	print ("\nWho was " + full_name.title()+"?")
	choice1 = raw_input ("\nA) first women to Mars"+"\nB) first computer programer"+ "\nC) first president")
	if choice1 == 'B':
		print("\t Correct")
		score+=1
	elif choice1 == 'quit': 
		break
	if choice1 == 'A':
        print ("\t incorrect")
        score-=1	
     if choice1 ==  'C':
		 print 
		
	
 
