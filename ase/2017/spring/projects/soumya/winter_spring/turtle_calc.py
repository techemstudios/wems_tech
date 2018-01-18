import turtle 
Tia = turtle.Turtle()

print("Give me a number please")
number1 =raw_input()
print("give me another")
number2 =raw_input()
number1 =int(number1)
number2 =int(number2)
print("operation?")
operation =raw_input()
if operation == "+":
	answer = number1 + number2
elif operation == "-":
	answer = number1 - number2
elif operation == "*": 
    answer = number1 * number2
elif operation == "/":
    answer = number1 / number2
    
#print(answer)

	# below is where you print
Tia.write(answer,font=(None,72,"italic"))
turtle.done()


