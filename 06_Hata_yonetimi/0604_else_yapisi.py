# region


"""
try:
    ........
    ........
    ........
except:
    ........
    ........
except:
    ........
    ........
else:
    Kod hata almazsa bu bloğa girilir
"""

# örnek 1




def dosyaAc(file):

    try:
        dosya = open(file)

    except:
        print("dosya bulunamadı")

    else:
        print(dosya.read())

# dosyaAc('kelimeler.txt')

# örnek 2 orjinal hata metni


def dosyaAc1(file):

    try:
        dosya = open(file, encoding='utf-8')

    except ModuleNotFoundError as ex:
        print(ex)

    else:
        print(dosya.read())

# dosyaAc1('kelimeler.txt')

# pass


def bolme():

    try:
        bolunen = int(input("bolunen: "))
        bolen = int(input("bolen: "))

        bolum = bolunen/bolen

    except:
        pass

    else:
        print(bolum)


# bolme()
