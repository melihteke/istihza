#!/bin/python3
username = input("Please enter your username :")
password = input("Please enter your password :")

if username == "abcdefg":
	if password == "12345678":
		print("You are logged in to very critical Software")
	else:
		print("Please enter correct password")
else:
	print("Please enter correct username")
