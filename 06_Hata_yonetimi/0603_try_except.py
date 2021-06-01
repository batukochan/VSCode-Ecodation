# region

"""
try:
    ........
    ........
except:
    ........
    ........

try: 
    - Kodu çalıştırmaya çalışır
    - Hata yoksa try bloğunun sonuna kadar gelir
    - Kod hata alırsa, kod try'dan çıkar
except:
    - Kod hata alırsa except'e gelir
    - derleyici hata olan yerden except içine atlar
    - Hatanın yakalandığı yer except bloğudur.
"""

# örnek 1

#  Hatanın yönetilmediği durum


def karesiniAl():

    girdi = input("Lütfen bir tam sayı giriniz: ")
    sayi = int(girdi)  # hatalı işlem

    print(sayi)

# karesiniAl()


def karesiniHesapla():

    try:
        girdi = input("Lütfen bir tam sayı giriniz: ")
        sayi = int(girdi)  # hatalı işlem

        print(sayi**2)
    except:
        print("Lütfen sayı giriniz...")
        karesiniHesapla()


# karesiniHesapla()

# örnek 2

""" olmayan bir dosyayı açmaya çalışalım """

def dosyaAc(file):
    try:
        dosya = open(file)

        for satir in dosya:
            print(satir.split())
    except:
        print("Dosya Bulunamadı")

# dosyaAc("ahmet.txt")

def bolme():

    try:
        bolunen = int(input("Bölüneni giriniz: "))
        bolen = int(input("Böleni giriniz: "))

        bolum = bolunen/bolen
        print(bolum)
    except ValueError:
        print('Tam sayı giriniz...')
        bolme()
    except ZeroDivisionError:
        print('Bölen sıfır olamaz...')
        bolme()
    

bolme()
