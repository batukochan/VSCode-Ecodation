# region built in

"""
getattr(nesne,nesneninÖzelliği)
setattr(nesne,özellik,özelliğeYapılacakAtama)
hasattr(nesne,varMıYokMu) True False döner
"""




class Derslik:
    def __init__(self, derslik, ogrenciSayisi, egitmenSayisi) -> None:

        self.derslik = derslik
        self.ogrenciSayisi = ogrenciSayisi
        self.egitmenSayisi = egitmenSayisi

    def Yazdir(self):

        return f"""
Derslik: {self.derslik}
Öğrenci Sayısı:{self.ogrenciSayisi}
Eğitmen Sayısı:{self.egitmenSayisi}
        """

d5 = Derslik(derslik=5,ogrenciSayisi=48,egitmenSayisi=3)
"""
print(getattr(d5,"derslik")) # 5
setattr(d5,"egitmenSayisi",2)
print(getattr(d5,"egitmenSayisi")) # 2

print(hasattr(d5,"isim")) # False
print(hasattr(d5,"derslik")) # True
"""
"""
print(d5.__doc__)
print(d5.__dict__)
print(d5.__module__)
"""