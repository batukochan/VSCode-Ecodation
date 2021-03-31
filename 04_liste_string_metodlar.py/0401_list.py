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
#region







#endregion