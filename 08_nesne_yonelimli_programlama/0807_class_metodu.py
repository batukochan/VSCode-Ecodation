# region class metod

class Insan:
    insanlar = []

    def __init__(self, ad, soyad) -> None:

        self.ad = ad
        self.soyad = soyad
        Insan.Ekle(self)

    @classmethod  # dekorator
    def Ekle(cls, insanNesnesi):
        Insan.insanlar.append(insanNesnesi)

    def __str__(self) -> str:
        return f"{self.ad} {self.soyad}"

    @classmethod
    def Parcala(cls, string):
        liste = string.split(",")
        return cls(liste[0], liste[1])


i1 = Insan("ali", "veli")

print(i1)

for i in Insan.insanlar:
    print(i)

