#!/bin/python3

person_info = { "Ahmet Özkoparan": 	{"Memleket": "İstanbul",
			 		 "Meslek" : "Öğretmen",
			 		 "Yaş" : 34},
		"Mehmet Yağız" : 	{"Memleket": "Adana",
			 		 "Meslek" : "Mühendis",
			 		 "Yaş" : 40},
		"Seda Bayrak" : 	{"Memleket": "İskenderun",
			 		 "Meslek" : "Doktor",
			 		 "Yaş" : 30}}
print("""\nCurrently we have only below people's details
	therefore please select the person
	1- Ahmet Özkoparan
	2- Mehmet Yağız
	3- Seda Bayrak\n\n\n""")
name=input("Specify the name and surname that you are looking for : ")

print("%s kisisinin \n1-Memleketi:%s\n2-Meslegi:%s\n3-Yasi:%s'dir" %(name, person_info[name]["Memleket"], person_info[name]["Meslek"], person_info[name]["Yaş"]))












