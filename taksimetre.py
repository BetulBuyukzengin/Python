# -*- coding: utf-8 -*-
#Taksimetre hesaplama

def taksimetre(taksi,sayi):
    if((taksi=="sarı") or (taksi=="bordo")):
        ucret=(km*3.45)+5.55
    elif((taksi=="siyah") or (taksi=="turkuaz")):
        ucret=(km*3.99)+6.68
    return ucret
        
renk=input("renk gir:")
km=int(input("yol gir:"))

x=taksimetre(renk,km)
print(x)
        
       
        
        
    
