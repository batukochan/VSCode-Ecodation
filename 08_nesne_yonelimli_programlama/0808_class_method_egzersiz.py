

class User:
    userListe = []

    def __init__(self, kullaciNick, kullaniciPass) -> None:
        self.kullaniciNick = kullaciNick
        self.kullaniciPass = kullaniciPass
        User.ekle(self)

    @classmethod
    def ekle(cls, us):
        cls.userListe.append(us)

    @classmethod
    def olustur(cls, string=str()):
        liste = string.split(",")
        return cls(liste[0], liste[1])

class Sistem:
    def __init__(self,ad) -> None:
        self.ad = ad

    def Login(self,kulAd,kulSifre):
        isLogin = False
        for item in User.userListe:
            if item.kullaniciNick == kulAd and item.kullaniciPass == kulSifre:
                isLogin = True
        if isLogin:
            print(f"{self.ad} Sistemine hoşgeldiniz {kulAd}")
        else:
            print("Hatalı giriş")

# u1 = User('admin', '123')
# u2 = User('admin', '123456')
User.olustur("admin,123")
User.olustur("admin,123456")
s1=Sistem("windows")
ad=input("Ad: ")
pw=input("Şifre: ")
s1.Login(ad,pw)
for item in User.userListe:
    print(item.kullaniciNick, item.kullaniciPass)
