#!/bin/python3
d1 = open("isimler1.txt")
d1_satırlar = d1.readlines()
d2 = open("isimler1.txt")
d2_satırlar = d2.readlines()
for i in d2_satırlar:
	if i in d1_satırlar:
		print(i)
d1.close()
d2.close()
