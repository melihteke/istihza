
#!/bin/python

fihrist_data = {"Melih TEKE" : {"age" : "35", "sex" : "male", "weight" : "76", "height" : "170" },
				"Femke Duur": {"age" : "35", "sex" : "female", "weight" : "68", "height" : "163" },
				"Olga Imeik" : {"age" : "31", "sex" : "female", "weight" : "80", "height" : "173" },
				"Rachid Meere":{"age" : "43", "sex" : "male", "weight" : "95", "height" : "183" },
				}



option = input("Please select one of the below options: \n1-Search person you already think that he/she in the database \n2-Add new person to database\n")								

if option == "1":
	person = input("Who do you looking for ? ")
	print(" %s : " %(fihrist_data[person]))
	print(" %s : " %(fihrist_data[person]["age"]))
	print(" %s : " %(fihrist_data[person]["sex"]))
	print(" %s : " %(fihrist_data[person]["weight"]))
	print(" %s : " %(fihrist_data[person]["height"]))
elif option =="2":
	person = input("Who is the person you would like to add into db ?")
	age = input("What is the age of that person ?")
	sex = input("What is the sex of that person ?")
	weight = input("What is the weight of that person ?")
	height = input("What is the height of that person ?")
	fihrist_data = {person : {"age" : age, "sex" : sex, "weight" : weight, "height" : height }}
	pass
else:
	print("Please enter only 1 or 2")
	person = input("Please select te person that you would like to get some info: ")

print("\nHere below you can see the current new DB:")
print(fihrist_data)


