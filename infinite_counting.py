#!/bin/python3

number = input("\nEnter the number: ")
limit = input("\nEnter the limit: ")

def count(number, limit):
	print(number)
	if number == limit:
		return "FINISHED"
	else:
		return count(int(number)+1, int(limit))

count(number,limit)

