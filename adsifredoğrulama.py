# -*- coding: utf-8 -*-

#***********************************************KULLANICI ADI VE ŞİFRE DOĞRULAMA PROGRAMI*****************************

defkullanici="betul"
defparola="12345"

while(True):
  kullanici=input("Kullanıcı adınızı giriniz:")
  parola=input("Parolanızı giriniz:")

  if((kullanici==defkullanici) and (parola==defparola)):
    print("Hoşgeldiniz......")
    break
  elif((kullanici!=defkullanici)and (parola==defparola)):
    print("Lütfen kullanıcı adını doğru giriniz.")
   
  elif((kullanici==defkullanici) and (parola!=defparola)):
    print("Parolanızı mı unuttunuz")   
    cevap=input("Parolanızı değiştirmek ister misiniz:(E/H)")
    
    if(cevap=="E"):
        yeniparola=input("Yeni parolanızı giriniz:")
        print("Lutfen bekleyiniz...")
        defparola=yeniparola
        print("Yeni parolanız başarıyla değiştirildi.")
  else:
    print("Tekrar deneyin")
    
 
   