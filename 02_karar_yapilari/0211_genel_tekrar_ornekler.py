#region If-Then

""" karşılaştırma operatörleri
eşittir ==
eşit değildir !=
küçüktür <
büyüktür >
küçük eşit <=
büyülk eşit >= """

#indent kavramı tab tuşu ile yapılır
"""
havaD="yağmurlu"
if havaD == "yağmurlu" :
    print("şemsiye al")
"""
"""
a = -1
if a<0 :
    print("{} sayısı negatiftir".format(a))
"""
"""
a=int(input("lütfen bir sayı giriniz : "))
if a>0 :
    print("{} sayısı pozitiftir.".format(a))
"""
"""
s1=15
s2=25
dil="python"
if s1>=s2 : pass 
if s1<=s2 : pass
if s1==s2 : pass
if s1 is s2 : pass
if s1!=s2 : pass
if s1 is not s2 : pass
if dil=="ali" : pass
if "yth" in dil : pass

"""
#endregion

#region If-Then-Else
"""
havaD=str(input("Hava durumunu giriniz..."))
if havaD=="Yağmurlu":
    print("Şemsiyeni almayı unutma!")
else:
    print("Hava günlük gülistanlık, rahat bir şeyler giy!")
"""

#engel örneği
"""
engeleDegdiMi= True
can, skor = 3,0
if engeleDegdiMi:
    can -= 1
    print("{} Canınız kaldı".format(can))
else:
    skor += 1
    print("{} anlık skorunuz".format(skor))
"""
"""
a=int(input("Lütfen bir sayı giriniz..."))
if a<0 :
    print("{} sayısı negatiftir.".format(a))
else:
    print("{} sayısı pozitiftir.".format(a))
"""
 #endregion

 #region If-Then-Else-Elif
"""
havaD = "yağmurlu"
if havaD=="yağmurlu":
    print("Şemsiyeni almayı unutma")
elif havaD=="sıcak":
    print("tişört giy")
else:
    print("kazak giy")
"""
"""
a=int(input("Lütfen bir sayı giriniz..."))
if a<0 :
    print("{} sayısı negatiftir.".format(a))
elif a==0 :
    print("LÜtfen 0 dışında bir sayı giriniz")
else:
    print("{} sayısı pozitiftir.".format(a))
"""

#endregion

#region iç içe if yapısı

#örnek1
"""
havaYagısliMi="yağmurlu"
havaSogukMu="soğuk"
if havaYagısliMi=="havadar":
    if havaSogukMu=="sıcak":
        print("şemsiyeni al,kazak giy")
    else:
        print("şemsiyeni al tişört giy")
else:
    print("şemsiyeni alma, kazak giy")
"""
#örnek2
"""
a = int(input("lütfen bir sayı giriniz..."))
if a>0:
    if a<100:
        print("{} sayısı 100'den küçük ve pozitiftir.".format(a))
    else:
        print("{} sayısı 100'den büyük ve pozitiftir.".format(a))
else:
    print("{} sayısı 100'den küçük ve negatiftir.".format(a))
"""
#örnek3
"""
temp1=float(input("lütfen vücut sıcaklığını giriniz..."))
temp2=float(input("lütfen vücut sıcaklığını giriniz..."))

if temp2>temp1:
    if temp2>=39:
        print("{} C* , !!! kritik vücut sıcaklığı !!!".format(temp2))
    elif temp2>=37 or temp2==39:
        print("ateşi yükseliyor")
    else:
        print("{} C* , vücut sıcaklığı normal seviyede!".format(temp2))
else:print( "ateşi düşüyor")
"""
#endregion

#region inline if
"""
a=int(input("bir sayı giriniz..."))
metin=""
if a==0:
    metin="sıfır"
elif a==1:
    metin="bir"
elif a==2:
    metin="iki"
else:
    metin="hatalı giriş"

print(metin)
print("-----------------------")

metin="sıfır" if a==0 else "bir" if a==1 else "iki" if a==2 else "hatalı giriş"
print(metin)"""

#endregion

#region mantıksal operatörler ile koşul birleştirme
"""
yas=int(input("Lütfen kursa kayıt olacak öğrencinin yaşını giriniz..."))
cevap="Kayıt yaptırabilirsiniz" if 4<yas<6 else "Kayıt yaptıramazsınız"
print(cevap)
print("-------------------")
yas=int(input("Lütfen kursa kayıt olacak öğrencinin yaşını giriniz..."))
if yas>4 and yas<6 :
    print("kayıt yaptırabilirsiniz")
else:
    print("kayıt yaptıramazsınız")
"""

#endregion

#region
#kullanıcı 0 girdiğinde program sonlanacak
#girilen sayıların en büyüğü ve en küçüğünü yazdır
'''
eb,ek,sayi
sayi=int(input("Lütfen bir sayı girin: "))
eb=sayi
ek=sayi
while sayi!=0:
    sayi=int(input("Lütfen bir sayı girin: "))
    if sayi>eb:
        eb=sayi
    elif sayi<ek and sayi!=0:
            ek=sayi
print(f"en büyük sayı {eb}, en küçük sayı {ek}")
'''

#endregion



