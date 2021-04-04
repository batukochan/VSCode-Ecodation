#region listeler
"""
sinifListesi=["Alperen","Batuhan","Kübra","Umut"]
print(sinifListesi)
print(type(sinifListesi))
liste=[]
print(liste)
"""
#endregion

#region örnek
"""
sayilar=[11,15,12,8.9,"ahmet","50 sayfa"] #elemanlar farklı olabilir.
print(sayilar)
"""
#endregion 

#region örnek
"""
sayilar=[11,15,12,8.9,"ahmet","50 sayfa"] #elemanlar farklı olabilir.
print(sayilar[-5])
"""
#endregion

#region degistirme
"""
sayilar=[11,15,7,12,1,0,3.14,12,13]
sayilar[2]="yedi"
print(sayilar)
"""
#endregion

#region örnek
"""
sayilar=[11,15,7,12]
print(sayilar)
sayilar[1]=sayilar[3]
print(sayilar)
"""
#endregion

#region listenin uzunluğu len
"""
sayilar=[11,15,7,12,15]
print(len(sayilar)) #eleman sayı olarak da düşünülebilir.
print(sayilar[len(sayilar)//2])
"""
#endregion

#region del_talimatı
"""
sayilar=[11,15,7,12,15]
print(sayilar)
del sayilar[-2]
print(sayilar)
print(len(sayilar))

'''
del sayilar #intellisense dersek listeyi siler ve nameerror verir.
'''
"""
#endregion

#region for döngüsü ile oku
"""
sayilar=[11,15,7,12,1,0,3.14,15]

for i in sayilar:
    if i>10:
        print(i,end=" ")
"""
#endregion

#region liste elemanlarını topla
"""
toplam=0
sayilar=[11,15,7,12,1,0,3.14,15]
for i in sayilar:
    toplam+=i
print(f"Listedeki elemanların toplamı {toplam}")
"""

#region sort-reverse
"""
sayilar = [1,54,6345,123,4234,653,12,6,1,32112,345]
sayilar.sort() #sıralar
print(sayilar)
sayilar.reverse() #tersten sıralar
print(sayilar)
"""
#endregion

#region set
"""
sayilar = [1,54,6345,123,4234,653,12,6,1,32112,345]
print(set(sayilar)) #aynı elemanları yazdırmaz.
"""
#endregion

#region listede for
"""
yorumBirakanlar = ["ahmet","mehmet","veli","ayşe"]

for kullanici in yorumBirakanlar:
    print(kullanici)

kullaniciSayisi = 0
for kullanici in yorumBirakanlar:
    kullaniciSayisi += 1
print(f"{kullaniciSayisi} adet yorum bırakıldı")
"""
#endregion

#region  örenkler split
"""
yorumBirakanlar = ["ahmet yılmaz","mehmet yağıbasan","veli çelik","ayşe burhanlı"]
ad = print(yorumBirakanlar[0].split()[0])
soyad = print(yorumBirakanlar[0].split()[1])
"""

"""
kullaniciSayisi = 0

for kullanici in yorumBirakanlar:
    kullaniciSayisi += 1
"""
"""
yorumBirakanlar = ["ahmet yılmaz","mehmet yağıbasan","veli çelik","ayşe burhanlı"]
kullaniciSayisi = 0
moderatör = "veli çelik"
moderatörSayisi = 0

for kullanici in yorumBirakanlar:
    
    ad , soyad = kullanici.split()[0] , kullanici.split()[1]
    if kullanici == moderatör:
        moderatörSayisi += 1
        print(f"{moderatörSayisi}. moderatörün adı {ad} sayadı {soyad}")
    else:
        kullaniciSayisi += 1
        print(f"{kullaniciSayisi}. kullanıcının adı {ad} sayadı {soyad}")
"""
#endregion

#region diğer iterable objelerde for döngüsü
"""
tup1 = (1,3,5,7)
for sayi in tup1:
    print(sayi)
"""
"""
liste = [[1,2],[3,4],[2,2]]
for x,y in liste: # listeler kaç elemanlıysa o kadar x,y,z... koymalıyız.
    print(x*y)
"""
"""
dic1={
    "ad" : "naz",
    "soyad" :"yağcıoğlu"
}

for k,v in dic1.items():
    print(f"key: [{k:^5}] \tValue:{v}")
"""
#endregion