# region

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


class Kart:
    def __init__(self, ad, soyad, bankaAdi, bakiye) -> None:
        self.ad = ad
        self.soyad = soyad
        self.bankaAdi = bankaAdi
        self.bakiye = bakiye
    
    def BilgiVer(self):
        return f"""
Ad: {self.ad}
Soyad: {self.soyad}
Banka Adı: {self.bankaAdi}
Bakiye: {self.bakiye}
        """
k1 = Kart("batu","Koçhan","ING",500)
# print(k1.BilgiVer())
class Atm:

    def __init__(self,ad,para) -> None:
        self.ad = ad
        self.para = para

    def BilgiVer(self):
        return f"""
Atm: {self.ad}
Para: {self.para}
        """   
    def AyniMi(self,kart):
        if self.ad == kart.bankaAdi:
            return True
        else:
            return False
    def ParaYatir(self,kart,tutar):
        kart.bakiye += tutar
        self.para += tutar
        if not self.AyniMi(kart):
            kart.bakiye -= tutar*0.03
            self.para += tutar*0.03
        print(f"{tutar} Tl yatırıldı\nAtm'de {self.para} Tl oldu. ")

    def ParaCek(self,kart,tutar):
        if self.para >= tutar:
            if kart.bakiye >= tutar:
                kart.bakiye -= tutar
                self.para -= tutar
                if not self.AyniMi(kart):
                    kart.bakiye -= tutar*0.03
                    self.para += tutar*0.03
                    print(f"{tutar*0.03} Tl işlem ücreti alındı.")
                print(f"{tutar} Tl para çekildi.\nAtm'de {self.para} Tl kaldı")
                pass
            else:
                print("Kartınızda yeterli bakiye yok!")
        else:
            print(f"Atm bakiyesi yetersiz..{self.para}")
        



atm1 = Atm("ING",1000)
# print(atm1.BilgiVer())

atm1.ParaYatir(k1,1000)
atm1.ParaCek(k1,1300)
print(k1.BilgiVer())
print(atm1.BilgiVer())
