import turtle
puck = turtle.Turtle()

print ("type in a number")
n1 = raw_input()

print ("type in a second number")
n2 = raw_input()

n1=int(n1)
n2=int(n2)
print("type in only + because it only adds")
opperation = raw_input()

if opperation == "+":
	answer = n1 + n2
else:
	answer = n1 + n2


puck.write(answer,font=(None,40,"Bold"))
turtle.done() 
