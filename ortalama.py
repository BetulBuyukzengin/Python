# -*- coding: utf-8 -*-

    
vize=int(input("Vize notunuzu giriniz:"))
vYüzde=40*vize/100
#print(vYüzde)
final=int(input("Final notunuzu giriniz:"))
fYüzde=60*final/100
#print(fYüzde)
ortalama=vYüzde+fYüzde
print("Ortalamanız: ",ortalama)
if 90<=ortalama<=100:
    print("Harf notu: AA")
elif 85<=ortalama<=89:
    print("Harf notu:BA")
elif 80<=ortalama<=84:
    print("Harf notu:BB")
elif 75<=ortalama<=79:
    print("Harf notu:CB")
elif 70<=ortalama<=74:
    print("Harf notu:CC")
elif 65<=ortalama<=69:
    print("Harf notu:DC")
elif 60<=ortalama<=64:
    print("Harf notu:DD")
elif 50<=ortalama<=59:
    print("Harf notu:FD")
elif 0<=ortalama<=49:
    print("Harf notu:FF")
    

