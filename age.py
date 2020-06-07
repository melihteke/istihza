#!/bin/python3

age=input("Please specify the age :")
age = int(age)
if age < 5:
	print("You are baby")
elif age < 10:
	print("You are still baby")
elif age == 18:
	print("Ohh thats a good age")
elif age < 25:
	print("You are still teen")
else:
	print("You are getting older, sorry dude")

