# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#t_yil = int(input("Tug'ulgan yilinggizni kiriting: "))
#yosh = 2025 - t_yil

#print("Siz " + str(yosh) + " yoshda ekansiz")

#t_yosh = input(" Yoshinggizni kiriting? ")
#yil = int(t_yil)
##print("siz " + str(yil) + "yilda tug'ulgan ekansiz ! ")



##yosh = 30
#print(type(ism))
#print(type(yosh))



#ism = (" Jobir")
#xabar = ism + ' ' + str(yosh)  + 'yoshda'

#print(xabar)

#b = -30
#c = a+b

#print(c)


# 07 - dars LIST 
  


#hayvonlar = ['it','mushuk','sigir','qoy', 'quyon', 'mushuk']

#bozorlik = ['yog', 'un', 'piyoz', 'gosht', 'banan']
#print("Men "  +  mahsulot  + " sotib oldim")
#print("olinmagan mahsulotlar: " , bozorlik)


#narxlar = [ 12000, 18000, 10900, 22000, 25, 56]

#print("narxlar[2]" + "narxlar[3]")



# 7 - dars Amaliyot
#ismlar = ("Xadichabonu" , " Malika " , " Anna ")
#print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
#print("Salom " + ismlar[2] + " ahvoling qanday?") 
#print("Salom " + ismlar[1] + " bugun ko'rishamizmi?")

#print(f"{ismlar[2]} va {ismlar[1]} egizaklar")
#print(ismlar[-0] + " o'tgan hafta ko'rgan edim ")



#sonlar = (29, 33, 18, 99, 132, 23)
#print(sonlar)


#sonlar = sonlar[3] + 27
#del sonlar[1]
#print(sonlar[3])

#t_shaxslar = [" Amir Temur", " Imom Buhoriy", " Napaloen"]

#z_shaxslar = [' Bill Geyts', ' Ilon Mask', ' MuhammadALI ']


#print(f"\nMen tarixiy shaxslardan{t_shaxslar.pop(1)} bilan,\n\
 #     zamonaviy shaxslardan esa{z_shaxslar.pop(2)}bilan\n\
  #        suhbat qilishni istar edim\n")
#friends = []
#friends.append('Zahro')
#friends.append('Alisher')
#friends.append('Ahmad')
#print(friends)

#friends.append('Madina')
#friends.insert(0,'Nigina')
#friends.insert(2,'Ivan')
#print(friends)

#mehmonlar = []

#mehmonlar.append(friends.pop(3))
#mehmonlar.append(friends.pop(-1))
#mehmonlar.append(friends.pop(0))
#print("\nKelgan mehmonlar: ", mehmonlar)





 #08 - Dars. Ro'yhatlar bilan ishlash.
#  07.03.2025.yil.
# Muallif: Kurbanova Nozima
#cars =['BMW', 'Tricker', 'Bugatti', 'Rolls Roys', 'Tesla', 'Audi']
#cars.sort()
#print(cars)


#narhlar = [12000,22500,23456,9800,5600,9934,32874]
#arzon = min(narhlar)
#qimmat = max(narhlar)
#jami = sum(narhlar)
#print("eng arzon narx ", arzon, "Eng qimmati ", qimmat,)

#toys = ('doll', 'bear', 'bus', 'car','dino', 'snake')

#davlatlar = ["Uzbekiston" , "Qozog'iston" ,"Rossiya" ,"Singapur","Malaysia","AQSH"]
#print(davlatlar)

#sonlar = list(range(1,11))
#taomlar = ['osh', 'somsa','norin','kabob','manti']
#nonushta = taomlar[:]

#09-Dars 
# FOR LOOP
#  Muallif: Kurbanova Nozima
# 08.03.2025


#mehmonlar = ['Ali' ,'Hamza' ,'Dovud' ,'Umar' ,'Usmon']
#for mehmon in mehmonlar:print(f" Hurmatli {mehmon} , sizni 20 - dekabrda nahorgi oshga takl;if qilamiz!")
#print(" Hurmat bilan, palonchayevlar oilasi")



#for mehmon in mehmonlar:
 #     print(f"Hurmatli {mehmon}, ", mehmon)
  #    print("Hayr", mehmon)




#sonlar = list(range(11))

#for son in sonlar:
 #   print(f"{son} ning kvadrati {son**2} ga teng")
#sonlar_kvadrati = []
#for son in sonlar:

 #   sonlar_kvadrati.append(son**2)
    

#print(sonlar)
#print(sonlar_kvadrati)


#dostlar = []
#print("5 ta eng yaqin dostinggiz kim?")
#for n in range(5):
 #   dostlar.append(input(f"{n+1}-dostinggizni ismini kiriting: "))

#print(dostlar)


#n_people = int(input("bugun necha kishi bilan suhbat qildinggiz?>>>"))

#ismlar = []
#for n in range(n_people):
 #   ismlar.append(input(f"{n+1}-suhbat qilgan odaminggiz kim edi: ?"))
#print(ismlar)

#kinolar =[]# 
#print("5 ta eng sevimli kinolariz qaysilar?")

#for k in  range(5):
 #   kinolar.append(input(f"{k+1}_kino:"))
  #



#  print(kinolar)
"""
09/03/2025
 
 Dasturlash asoslari
 
#10-dars: Tarmoqlash

Muallif: Kurbanova Nozima
web:Men omadliman!
"""

#avtolar =['hundai','bmw', 'tricker','malibu', 'lasetti']



#for avto in avtolar:
 #   if avto == 'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())



#ism = 'Ali'
#ism.lower() == 'ali'



#ism=input('Isminggiz nima?\n>>>')
#if ism.lower() != 'ali':
#    print(f"Uzr, {ism.title()} biz Alini kutyapmiz. ")
#else:
#    print("Salom, Ali!")


#javob = float(input("12*6 nechiga teng?>>>"))
#if javob !=72:
#    print("Javob xato!")


#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>=18:
 #   print("Xush kelibsiz!")
#else:
 #   print('Kirish mumkin emas!')

#login = input("Yangi login tanlang: ")
#if len(login)<=5:
 #   print("Login 5 ta harfdan ko'p bo'lishi shart! ")


#yil = int(input("Tug'ilgan yilingizni kiriting!: "))
#if 2025-yil<18:
 #   print(f"Yoshingiz{2025 - yil}da ekan.")
  #  print(" Kirish mumkin emas")
#else:
#    print("Xush kelibsiz!")

#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>65: print("Siz Covid-19 risk guruhida ekansiz")

#x,y = 25,50
#print("x>y") if x>y else print("x<y")


"""

10/03/2025 

11 - dars: Bir nechta shartlarni tekshirish.
Muallif: Kurbanova Nozima
web: Lucky

"""

son = -72

if son <0:
    print("Manfiy son")
else:
    print("Musbat son")
narh = 15000
choy = True
salat = True
non =  True
kampot =True
assorti = False
if choy:
   narh = narh + 3000
   if salat:
       print("mijoz salat oldi .")
       if non:
          print("mijoz non oldi .")
          narh = narh + 2000
          if kampot:
                print("mijoz kampot oldi .")
                narh = narh + 5000
                if assorti:
                    print("mijoz assorti oldi .")
                    narh = narh + 10000
   
    
print(f"Jami {narh} so'm ")
 


#menu = ["Osh","norin", "somsa", "qozonkabob"]
#buyurtmalar = [ ]

#if buyurtmalar:
 #   for taom in buyurtmalar:
  #    if taom in menu:
   #     print(f"menuda {taom} bor ")
    #else:
     #   print(f"Kechirasiz, menyuda {taom} yo'q ")
                               
#else:
 #                                  
  #  print("savatchangiz bo'sh ")
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() not in menu:
#    print('afsuski bizda bunday ovqat yo\'q .')
#else:
#    print('buyurtmanggiz qabul qilindi .')
 





















































