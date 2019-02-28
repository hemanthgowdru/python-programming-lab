import random

while True: 
	d = input("Press r to roll, q to quit:")

	if d == 'r':
		print("you got :",random.randit(1,6))
		
	elif d == 'q':
		print("Bye!")
		exit()

print("end")


