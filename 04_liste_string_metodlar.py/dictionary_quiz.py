# region quiz

def kelimelerSozlugu():
    MINKARAKTERUZUNLUGU = 19  # CONSTANT
    # boş sözlük yaratıyoruz
    sozluk = dict()
    dosya = open('C:\\Users\\batuh\\Downloads\\kelime.txt')
    for i, satir in enumerate(dosya):
        # satır içerisindeki \n karakterleri silmeliyiz
        satirDizisi = satir.split()
        kelime = satirDizisi[0]
        if len(kelime) >= MINKARAKTERUZUNLUGU:
            # print(kelime)
            if not kelime in sozluk:
                sozluk[kelime] = len(kelime)
    return sozluk

# print(kelimelerSozlugu())

# endregion

# region


def kelimelerSozlugu2():
    MINKARAKTERUZUNLUGU = 19  # CONSTANT
    # boş sözlük yaratıyoruz
    sozluk = dict()
    dosya = open('C:\\Users\\batuh\\Downloads\\kelime.txt')
    for i, satir in enumerate(dosya):
        # satır içerisindeki \n karakterleri silmeliyiz
        satirDizisi = satir.split()
        kelime = satirDizisi[0]
        uzunluk = len(kelime)
        if uzunluk >= MINKARAKTERUZUNLUGU:
            # print(kelime)
            if not uzunluk in sozluk:
                sozluk[uzunluk] = [kelime]
            else:
                sozluk[uzunluk].append(kelime)

    return sozluk

# print(kelimelerSozlugu2())

# endregion

# region 3


def aracYarat1():
    arac = dict()
    #arac = {}

    arac['model'] = 'mustang'
    arac['yıl'] = '78'
    arac['koltuk'] = '2'
    arac['renk'] = 'kırmızı'
    arac['fiyat'] = '30k $'
    arac['km'] = '32000'

    return arac

# print(aracYarat1())

# update


def yeniArac():

    arac = aracYarat1()

    # ilk olarak arac sözlüğü kopyalanır.
    yeniArac = arac.copy()

    for items in arac.items():
        key = items[0]
        value = items[1]
        key += '_2'

        yeniArac[key] = value

    return yeniArac

# print(yeniArac())


def sozlukBirlestir(d1, d2, d3):
    # python'da birden fazla sözlük üzerinde tek seferde dönülebilir.
    sozluk = dict()

    for i in (d1, d2, d3):
        sozluk.update(i)

    return sozluk

d1 = {'wer:22':'22'}
d2 = {'wer:2':'12'}
d3 = {'wer:21':'22'}

print(sozlukBirlestir(d1,d2,d3))
