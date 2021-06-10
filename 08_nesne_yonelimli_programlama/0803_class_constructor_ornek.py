# region örnek
"""
araba galerisi için mimari oluşturulacak
marka-model-yıl girilmek zorunda
renk zorunlu değil, eğer yazılmadıysa tanımsız renk olarak atama yapılacak
aynı zamanda yaş değeri kullanıcıdan alınmayacak
constructor içinde hesaplama ile atama yapılacaktır Ör. 2019 yılı
show() fn kullanılacaki show() içinde arabanı tüm detayları düzgün biçimde formatlayarak gösterilecek
"""

import datetime


class Galeri:

    def __init__(self, marka, model, motor, yil, renk="Tanımsız") -> None:
        self.yil = yil
        self.arabaninYasi = datetime.datetime.now().year - int(self.yil)
        self.marka = marka
        self.model = model
        self.motor = motor
        self.renk = renk

    def Show(self):
        return f"""
Marka: {self.marka}
Model: {self.model}
Motor: {self.motor}
Renk : {self.renk}
Yıl  : {self.yil}
Yaş  : {self.arabaninYasi}
"""


araba1 = Galeri(marka="Audi", model="A6",
                motor="2 TDI", yil=2018, renk="Siyah")

print(araba1.Show())

# endregion
