# atm örneği

"""
- Kart >> class adı. Özellikleri :  ad,soyad,bankaAdi,para
    -BilgiVer()
-Atm >> class adıç Özellikleri : ad,para
-paraCek(),paraYatir(),BilgiVer(),AyniMi()
paraCek >>
    -farklı bankadan yapılan işlemden %3 faiz al
ParaYatir
    -farklı bankadan yatırılan para için %3 ek ücret talep et onaylattır.
"""


class Kart():
    def __init__(self, ad, soyad, bankaAdi, para) -> None:
        self.ad = ad
        self.soyad = soyad
        self.bankaAdi = bankaAdi
        self.para = para
        pass

    def BilgiVer(self):
        return f''' 
-------------------------------------------------
Ad = {self.ad}
Soyad = {self.soyad}
Banka adı = {self.bankaAdi}
Para = {self.para}
-------------------------------------------------'''


k1 = Kart('Batu', 'Koçhan', 'ING', 150)
# print(k1.BilgiVer())


class Atm():
    def __init__(self, ad, para) -> None:
        self.ad = ad
        self.para = para

    def AynıMi(self,kart):
            if self.ad == kart.bankaAdi:
                return True
            else:
                return False

    def BilgiVer(self):
        return f'''
-------------------------------------------------
Atm : {self.ad}
Atm Bakiyesi: {self.para} TL
-------------------------------------------------'''
    def ParaYatir(self,kart,miktar):
        kart.para += miktar
        self.para += miktar
        if not self.AynıMi(kart):
            kart.para -= miktar*0.03
            self.para += miktar*0.03
        print(f"{miktar} TL yatırıldı\nAtm Bakiyesi: {self.para}")
    def ParaCek(self,kart,miktar):
        if self.para >= miktar:
            if kart.para >= miktar:
                kart.para -= miktar
                self.para -= miktar
                if not self.AynıMi(kart):
                    kart.para -= miktar*0.03
                    self.para += miktar*0.03
                    print(f"{miktar*0.03} TL işlem ücreti alındı")
            else:
                print(f"Kart bakiyeniz yetersiz...\nBakiyeniz: {kart.para}")
        else:
            print(f"ATM Bakiyesi yetersiz...\nAtm Bakiyesi: {self.para}")

atm1 = Atm('Garanti',500)
# print(atm1.BilgiVer())
atm1.ParaCek(k1,100)
print(k1.BilgiVer())

