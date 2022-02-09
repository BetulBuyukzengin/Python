# -*- coding: utf-8 -*-
#range kullanımı

print(*range(10))#0 dan 10(dahil değil) a kadar liste oluşturur.
print(*range(2,10)) # 2 ve 10 arası liste oluşturur.
print(*range(2,27,3))# 2 ve 27 arası 3 er 3 er liste oluşturur.
      
for i in range (10): #0 dan 9 a kadar çıktı verir (9 dahil)
  print(i)

for i in range(10): # 0 dan 9 taneye  kadar * yazdırır
    print(i*"*")
