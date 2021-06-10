# region örnek

"""
-Calisan sınıfı
ad,soyad,tc,maas
bilgiVer() -> kullanıcıların bilgilerini yazdırsın
ZamYap(tl) -> eğer yapılmak istenilen zam maaşın %40ından fazlaysa emin misin diye sorulsun
cevap e ya da E ise zam yapılsın h ya da H ise işlem yapılmasın.
-Sirket sınıfı
AlimYap() -> çalışan sınıfından nesneyi gönderip bilgilerini yazdırıp, işe alım yapılır.
IstenCikar() -> çalışan sınıfından nesneyi gönderip bilgilerini yazdırıp işten çıkartır.
"""


def cevap():
    cevap = input("""Zam yapmak için e/E, sayfadan ayrılmak için h/H giriniz...
Cevap: """)
    return cevap


class Calisan:
    def __init__(self, ad, soyAd, kimlik, maas) -> None:
        self.ad = ad
        self.soyAd = soyAd
        self.kimlik = kimlik
        self.maas = maas

    def BilgiVer(self):
        return f"""
İsim: {self.ad}
Soyisim: {self.soyAd}
Kimlik: {self.kimlik}
Maaş: {self.maas}
"""

    def ZamYap(self, zam):
        zam=int(input("Zam (tl): "))
        zMo = zam / self.maas  # zam-maaş-oranı zMo
        if zMo > 0.4:
            print("Emin misiniz ?")
            if cevap().isalpha() and cevap().lower() == "e":
                yeniMaas = int(self.maas) + zam
                self.maas = yeniMaas
            else:
                print("Zam yapmak için e/E, işlemden çıkmak için h/H giriniz...")
        else:
            yeniMaas = int(self.maas) + zam
            self.maas = yeniMaas


calisan1 = Calisan(ad="Muhittin", soyAd="Karabacak",
                   kimlik="22845321143", maas=4285)
"""
# calisan1.ZamYap()
# print(calisan1.BİlgiVer())
"""

class Sirket:

    def __init__(self, ad, kurulusTarihi):
        self.ad = ad
        self.kurulusTarihi = kurulusTarihi
        self.calisanlar = []

    def AlimYap(self, c):

        self.calisanlar.append(c)
        print(f"""{c.ad} {c.soyAd} isimli çalışan, işe alındı""")

    def IstenCikar(self,c):
        self.calisanlar.remove(c)
        print(f"""{c.ad} {c.soyAd} isimli çalışan, işten çıkartıldı""")
        

c1 = Calisan(ad="Ali",soyAd="ŞAHİN",kimlik=23232323,maas=6750)
c2 = Calisan(ad="Kemal",soyAd="KEL",kimlik=33333333,maas=7500)
c3 = Calisan(ad="Merve",soyAd="Telli",kimlik=11121112,maas=3420)

s1 = Sirket("Bal Kaymak A.Ş", 1912)
s1.AlimYap(c1)
s1.AlimYap(c2)
s1.AlimYap(c3)

for i in s1.calisanlar:
    if i.ad == "Ali":
        s1.IstenCikar(i)

print("-"*20)

for i in s1.calisanlar:
    print(i.BilgiVer())