#!/bin/python

telephone_dic = {"Melih TEKE":"0533 345 34 35",
		 "Osman TEKE":"0523 123 12 34",
		 "Ali BEKIR":"0512 124 45 65",
		 "Cansin TEKE":"0544 123 67 98",
		 "Mehmet YEK":"0573 145 42 43"}

asked_record = input("Please enter the name for your query: ")

if asked_record in telephone_dic:
	print("\n%s's phone number is %s" %(asked_record, telephone_dic[asked_record]))
	with open("phone_query.txt", "a") as f:
		f.write("\n %s's phone number is %s" %(asked_record, telephone_dic[asked_record]))
		f.close()
else:
	print("The person you have searched was not found in database !!!! ")


