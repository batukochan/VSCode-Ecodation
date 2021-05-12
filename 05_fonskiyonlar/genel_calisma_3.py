# region bool fonksiyonlar
'''
def ciftMi(x):
    """fonksiyon içerisinde verilen sayının
    tek ya da çift olma durumuna göre boolean 
    bir değer döndürür."""
    if x % 2 == 0:
        return True
    return False

deger = ciftMi(11)
a = ciftMi
print(a(12)) # True → a aslında ciftMi fonksiyonu olmuştur. Yeniden adlandırma!
print(deger) # False
print(a) # function ciftMi at adress
print(type(a)) # class <function>
'''
# endregion

# region *args
'''
Fonksiyonumuzun alacağı parametreleri bilemediğimiz 
durumda '*args' parametresini alır.
'''
"""
def topla(*args):
    return sum(args)
    
print(topla(2,3,4,5,6,7,8,9))
"""
# endregion

# region


def girdiAl(metin):
    girdi = input(metin)
    return girdi


"""
sayi = girdiAl("Lütfen br sayı giriniz: ")
print(sayi)
print(type(sayi))
"""
# endregion

# region
'''
olasılık 1 - girdinin başında ya da sonunda boşluk olabilir. (strip)
olasılık 2 - sayının başına +/- yazılmış olabilir. strip(kesilecek karakterler)
'''


def tamSayiMi(girdi):
    girdi = girdi.strip()
    girdi = girdi.strip('+-')
    if girdi.isdigit():
        return True
    else:
        return False


"""
aciklama = "Lütfen bir tam sayı giriniz...\nSayı: "
sayi = girdiAl(aciklama)
print(tamSayiMi(sayi))
print(tamSayiMi(girdiAl("Lütfen bir sayı giriniz: ")))  # tek satırda
"""
# endregion

# region


def tamSayiDongusu():
    deger = tamSayiMi(girdiAl("Lütfen bir sayi giriniz: "))
    if deger:
        return f"Girilen veri tam sayısıdır {deger}"
    else:
        return tamSayiDongusu()


"""
print(tamSayiDongusu())
"""

# endregion

# region


def hangiGun():
    gunler = ["", "Pazartesi", "Salı", "Çarşamba",
              "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    gun = int(input("1 ile 7 arasında bir gün seçiniz...\Gün: "))
    if 0 < gun <= len(gunler):
        print(gunler[gun])
    else:
        print("Hatalı seçim")
        return hangiGun()


"""        
hangiGun()
"""
# endregion

# region


def aritmatikOrt(*args):
    toplam = sum(args)
    elemanSayisi = len(args)
    ort = toplam/elemanSayisi
    return f"{elemanSayisi} adet sayının aritmatik ortalaması → {round(ort,2)}"

print(aritmatikOrt(12,17,11))