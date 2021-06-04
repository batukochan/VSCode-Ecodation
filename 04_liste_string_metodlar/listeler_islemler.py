#region iki listeyi birleştirmek
"""
sayilar = [1,2,3,4,5,6,7,8]
harfler = ['a',"b","c","d"]
''' summation'''
listelerinBirlesimi = sayilar + harfler
print(listelerinBirlesimi) 
listelerinBirlesimi = harfler +sayilar
print(listelerinBirlesimi)
print(type(listelerinBirlesimi)) #list 
listelerinBirlesimi.append("python")
print(listelerinBirlesimi)
print(sayilar,harfler)
print(type(listelerinBirlesimi)) #list 
"""
#endregion

#region multiplyist
"""
sayilar = [1,2,3,4,5,6,7,8]
liste = sayilar*5
print(liste)
"""
"""
sayilar = [1,2,3,4,5,6,7,8,9,10]
karesi = []
print(sayilar)
for i in sayilar:
    kare = i**2
    karesi.append(kare)
print(karesi)
"""
#endregion

#region 
"""
karesi = [sayi**2 for sayi in range(1,11)]
print(karesi)
"""
'''
kenar uzunlukları 1den 10a kadar olan 
eşkenar üçgenlerin alanını bulan program
'''

#alan = (((3**1/2)*(a**2))/4)
"""
alanlar = [round((((3**1/2)*(i**2))/4),3) for i in range(1,11)]
print(alanlar)
"""
#1den 10000e kadar olan çiftleri
"""
ciftSayilar = [sayi for sayi in range(2,1001,2)]
print(ciftSayilar)
"""
#hem çift hem de üçe tam bölünen
"""
ucVecift = [sayi for sayi in range(1,1001) if sayi % 3 == 0] 
print(ucVecift)
"""
"""
ucVecift = [sayi for sayi in range(1,101) if sayi % 3 == 0 and sayi % 2 == 0] 
print(ucVecift)
"""
"""
isimler = ["ahmet","mehmet","onur","oğuzhan","doğukan"]
ismiOileBaslayanlar = [isim for isim in isimler if .startw with('o') ]
"""
#endregion

#region örnek
"""
list1 = [10,20,30]
list2 = [2,7,11,13]
yeniListe = []
for i in list1:
    for j in list2:
        yeniListe.append(i*j)
print(yeniListe)
"""
"""
list1 = [10,20,30]
list2 = [2,7,11,13]
yeniListe = [x*y for x in list1 for y in list2 if x*y <= 200]
print(yeniListe)
"""
"""
list1 = [10,20,30]
list2 = [2,7,11,13]
sayi = 110
if sayi in [x*y for x in list1 for y in list2 if x*y <= 200] :     
    print("ok")
"""
#endregion

#region
"""
kordinat = [5,3,2]
x,y,z = kordinat[:3]
multiply = x*y*z
print(multiply)
"""
#endregion
