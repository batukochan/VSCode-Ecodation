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


d1 = {'wer:22': '22'}
d2 = {'wer:2': '12'}
d3 = {'wer:21': '22'}

print(sozlukBirlestir(d1, d2, d3))


def ayniKeyToplamlariFarkliKeyKendileri(d1, d2):

    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise Exception('Parametrelerin ikisi de sözlük olamalıdır.')

    if len(d1) != len(d2):
        raise Exception('Sözlük uzunlukları aynı olmalıdır.')

    sozluk = dict()

    for key in d1:
        if key in d2:
            sozluk[key] = d1[key] + d2[key]
        else:
            sozluk[key] = d1[key]
    for key in d2:
        if not key in d1:
            sozluk[key] = d2[key]
    return sozluk


d1 = {

    'a': 10,
    'b': 30,
    'c': 50

}

d2 = {

    'a': 40,
    'b': 60,
    'd': 90
}

a = ayniKeyToplamlariFarkliKeyKendileri(d1, d2)
# print(a)

# endregion

# region


def listToDict(l1, l2):
    sozluk = dict()

    for i, j in enumerate(l1):
        sozluk[j] = l2[i]

    return sozluk


l1 = ['ad', 'soyad', 'numara']
l2 = ['batu', 'koçhan', '348165']

print(listToDict(l1, l2))


# alfanumerik

def alfanumerik(sozluk):

    silinecekKeytler = []
    for key in sozluk.keys():
        if not str(key).isalpha():
            silinecekKeytler.append(key)
    # silinecek keyler doldu
    for key in silinecekKeytler:
        if key in sozluk.keys():
            sozluk.pop(key)

    return sozluk


d1 = {

    'a': 'A',
    1: 100,
    'b': 'B',
    3: 200
}
print(alfanumerik(d1))
