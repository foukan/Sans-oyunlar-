import random
a = 0
denemeHak = 1
dogru = ". seferde buldu"
yanliş = ". yanlış"
while a != 101 and denemeHak < 4 :
      a =random.randint(99,101)
      print(a)
      if a == 101:
            print(str(denemeHak)+ dogru)
      else:
            print(str(denemeHak)+ yanliş)
      denemeHak = denemeHak + 1