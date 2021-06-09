"""
class Insan:
    ad = ""
    soyAd = ""
    ozellik = []

i1 = Insan()
i1.ad = "Batu"
i1.soyAd = "Koçhan"
i1.ozellik.append("Hayalperest")
i2 = Insan()
i2.ad = "Mercan"
i2.soyAd = "Atay"
i2.ozellik.append("Uykucu")
"""
"""
print(i1.ad,i1.soyAd,i1.ozellik)
print(i2.ad,i2.soyAd,i2.ozellik)


çıktı → 
Batu Koçhan ['Hayalperest', 'Uykucu']
Mercan Atay ['Hayalperest', 'Uykucu']

Class içerisinde bir liste kullanırsak bu liste nesnelerin kendine 
ait bir liste olmuyor, tüm nesnelerin ortak özelliklerinin tutulduğu 
bir liste oluşturuluyor.

Ayrı ayrı alabilmek içim self kullanılır.
"""
"""

class Insan:
    insanSayisi = 0
    def __init__(self) -> None:
        self.ozellik = []
        self.ad = ""
        self.soyAd = ""
        Insan.insanSayisi +=1

i1 = Insan()
i1.ad = "Batu"
i1.soyAd = "Koçhan"
i1.ozellik.append("Hayalperest")
i2 = Insan()
i2.ad = "Mercan"
i2.soyAd = "Atay"
i2.ozellik.append("Uykucu")

print(i1.ad,i1.soyAd,i1.ozellik)
print(i2.ad,i2.soyAd,i2.ozellik)
print(Insan.insanSayisi)
"""

class Insan:
    insanSayisi = 0
    def __init__(self,ad,soyAd,ozellik:list) -> None:
        self.ozellik = ozellik
        self.ad = ad
        self.soyAd = soyAd
        Insan.insanSayisi +=1
    def yazdir(self):
        print(f"{self.ad} {self.soyAd} {self.ozellik}")

i1 = Insan(ad="Batu",soyAd="Koçhan",ozellik=["Hayalperest"])
i1.yazdir()

# ornek 2

class Ogrenci:
    def __init__(self,adSoyAd="",not1=1,not2=1):
        self.adSoyAd = adSoyAd
        self.not1 =not1
        self.not2 =not2
    def notHesapla(self):
        return (self.not1 + self.not2) / 2

isim = input("Lütfen Ad Soyad giriniz: ")
n1 = int(input("vize notu: "))
n2 = int(input("Final notu: "))
o1 = Ogrenci(isim,n1,n2)
notOrtalaması = o1.notHesapla()
print(notOrtalaması)
