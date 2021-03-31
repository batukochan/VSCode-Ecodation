#mantıksal operatörler -> logical operatörler

'''
ve        and
veya      or
değil     not
'''

#region
"""
print(5==5 and 15>5)
print(5==5 and 15<5)
print(5!=5 and 15==5)
print(5!=5 and 15>5)
"""
#endregion

#region
"""
a=int(input("sayı gir: "))
if 0<a<100:
    print("sayı 100den küçüktür")
"""
#endregion

#region

'''
4,5,6 yaşları için kurs 1e

'''

"""
yas=int(input("Lütfen yaşınızı giriniz: "))
if 4<=yas and yas<=6:
    print("Kurs 1'e kayıt olabilirsiniz.")
else:
    print("Kurs 1'e uygun değilsin.")
"""

#endregion

#region örnek
"""
index=19
while 18.5<index<24.99:
    kilo=float(input("Kilonuzu giriniz: "))
    boy=float(input("Boyunuz(m): "))
    index=kilo/boy**2
    if index>30 and boy<2.4:
        print("İdeal kilonun çok üstündesiniz.")
        index=19
        continue
    elif 25<index<29.99 and boy<2.4:
        print("İdeal kilonun üzeri")
        index=19
        continue
    elif 18.5<index<24.99 and boy<2.4:
        print("İdeal kilo")
        break
    elif index<18.49 and boy<2.4:
        print("ideal kilonun altı")
        index=19
        continue
    else:
        print("boyunuzu metre cinsinden yazınız örneğin : 1.84 ")
"""
"""
toplam = 0
while True:
    sayi = int(input("lütfen sayı giriniz. Çıkmak için 0 tuşuna basınız. \t"))
    if sayi == 0:
        break
    if sayi<0 or sayi %2 == 1:
        print("Negatif ve tek sayı giremezsin")
        continue
    toplam += sayi
print(toplam)
"""
"""
gelir=int(input("Yıllık gelirinizi giriniz(TL): "))
if 0<gelir<22000:
    vergi=gelir*0.15
    print(F"Ödenecek tutar: {vergi} TL")
elif 22000<gelir<49000:
    vergi=gelir*0.20
    print(F"Ödenecek tutar: {vergi} TL")
elif 49000<gelir<=180000:
    vergi=gelir*0.27
    print(F"Ödenecek tutar: {vergi} TL") 
"""
