#!/bin/python3

ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
	sayı1 = int(ilk_sayı)
	sayı2 = int(ikinci_sayı)
	print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ZeroDivisionError:
	print("Bir sayiyi 0 a bolemezsiniz")
