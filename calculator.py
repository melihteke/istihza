#!/bin/python3
giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) karekök hesapla
"""
print(giriş)

a = 1
while a == 1:
	soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
	if soru == "q":
		print("çıkılıyor...")
		a = 0
	elif soru == "1":
		sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
		sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
		#İlk %s'ye karşılık gelen değer : sayı1
		#İkinci %s'ye karşılık gelen değer: sayı2
		#Üçüncü %s'ye karşılık gelen değer: sayı1 + sayı2
		print("%s + %s = %s" %(sayı1, sayı2, sayı1 + sayı2))
	elif soru == "2":
		sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
		sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
		print("%s - %s = %s" %(sayı3, sayı4, sayı3 - sayı4))
	elif soru == "3":
		sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
		sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
		print("%s x %s = %s" %(sayı5, sayı6, sayı5 * sayı6))
	elif soru == "4":
		sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
		sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
		print("%s / %s = %s" %(sayı7, sayı8, sayı7 / sayı8))
	elif soru == "5":
		sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
		#İlk %s'ye karşılık gelen değer : sayı9
		#İkinci %s'ye karşılık gelen değer: sayı9 ** 2
		print("%s sayısının karesi = %s" %(sayı9, sayı9 ** 2))
	elif soru == "6":
		sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
		print("%s sayısının karekökü = %s" %(sayı10, sayı10 ** 0.5))
	else:
		print("Yanlış giriş.")
		print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

