#!/bin/python3

kalkış = input("Kalkış yeri: ")
varış = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayısı = input("Bilet sayısı: ")

metin = "{} noktasindan {} noktasina 14:30 hareket saatli sefer icin {} adina {} adet bilet ayrilmistir.!"

print("\n\n**********************************************\n\n")
print(metin.format(kalkış,varış,isim_soyisim,bilet_sayısı))
print("\n\n**********************************************\n\n")

