print("Masukan Angka ke-1 : ")
angka1=int(input())
print("Masukan Angka ke-2 : ")
angka2=int(input())
print("Masukan Angka ke-3 : ")
angka3=int(input())

print("\n")

if (angka1 > angka2) and (angka1 > angka3) :
    print(f"Bilangan Pertama ({angka1}) Lebih Besar Dari Bilangan Kedua ({angka2}) dan Ketiga ({angka3})")

elif (angka2 > angka1) and (angka2 > angka3) :
    print(f"Bilangan Kedua ({angka2}) Lebih Besar Dari Bilangan Pertama ({angka1}) dan Ketiga ({angka3}) ")

elif (angka3 == angka1) and (angka3 == angka2) and (angka2 == angka3) :
    print("Bilangan Yang dimasukan sama besar ")

else:
    print(f"Bilangan ketiga ({angka3}) lebih besar dari Bilangan pertama ({angka1}) dan kedua ({angka2}) ")