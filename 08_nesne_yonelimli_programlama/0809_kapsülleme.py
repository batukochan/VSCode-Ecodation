# region

class Ogrenci:
    def __init__(self, ad, soyad, tc,sinif,okul) -> None:
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.setSinif(sinif) 
        self.setOkul(okul)
    
    def setSinif(self,arg):
        if 8 < arg < 13:
            self.__sinif = arg
        else:
            self.__sinif = -1
    
    def setOkul(self,arg):
        if arg != "KTÜ":
            self.__okul = -1
        else:
            self.__okul = arg
    
    def getOkul(self):
        return self.__okul
    
    def getSinif(self):
        return self.__sinif

    def BilgiVer(self):
        if self.getSinif() == -1:
            return "Üzgünüm!!! 9-12 sınıflar dışında kayıtlar bitmiştir."
        if self.getOkul()==-1:
            return "Ktü dışı kayıt olmaz"
        return f"{self.ad} {self.soyad} {self.tc} {self.__sinif} {self.__okul}"



ogr1 = Ogrenci("Batu", "Koçhan", 12345,10,"Ktü")
# ogr1.setSinif(14)
ogr1.setOkul("krü")
print(ogr1.BilgiVer())

# if ogr1.sinif != "Ekonomi 101":
#     print("bu sınıfta olamasın")
# endregion

