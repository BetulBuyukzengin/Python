# -*- coding: utf-8 -*-
"""
Betül Büyükzengin
201713171064


"""
print("Burc programi.....")
gun = int(input("Lütfen dogum tarihinizin gününü giriniz: "))
ay = input("Lütfen dogum tarihinizin ayını giriniz:  ")
if ay == 'december':
  if(gun > 22):
        print('burcunuz:capricorn')
  else :
      print('burcunuz:sagittarius')
      
  
elif ay == 'january':
  if (gun > 20):
       print('burcunuz:aquarius')
  else:
       print('burcunuz:capricorn')
        
elif ay == 'february':
  if (gun > 19):
        print('burcunuz:pisces')
  else:
         print("burcunuz:aquarius")
elif ay == 'march':
  if (gun > 21):
         print('burcunuz:aries')
  else:
         print('burcunuz:pisces')
elif ay == 'april':
  if (gun > 20):
         print('burcunuz:taurus')
  else:
         print('burcunuz:aries')
elif ay == 'may':
  if (gun > 21):
    print('burcunuz:gemini')  
  else:
       print('burcunuz:taurus')
elif ay == 'june':
  if (gun > 21):
        print('burucunuz:cancer') 
  else: 
        print('burucunuz:gemini')
elif ay == 'july':
  if (gun > 23):	
        print('burucunuz:leo')
  else:
        print('burucunuz:cancer')
        
elif ay == 'august':
  if (gun > 23):
        print('burucunuz:virgo')
  else:
        print('burucunuz:leo')
elif ay == 'september':
  if (gun > 23):
         print('burucunuz:libra')
  else :
         print('burucunuz:virgo')
elif ay == 'october':
  if (gun > 23):
         print('burucunuz:scorpio') 
  else:
         print('burucunuz:libra')
elif ay == 'november':
  if (gun > 22):
         print("burucunuz:sagittarius")
  else:
         print("burucunuz:scorpio")
        
    