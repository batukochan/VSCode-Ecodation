# region

"""
1-10 arası sayıların karelerini içeren liste oluştur.
"""

from typing import Any


kareler = []
for i in range(11):
    kareler.append(pow(i, 2))
# print(kareler)

# comprehension

karaelerComp = [pow(i, 2) for i in range(11)]
# print(karaelerComp)

"""
isminizin harflerini büyük yazıp listeye ekleyin.
"""

isim = 'Batuhan Koçhan'

liste = [i.upper()
         for i in isim
         ]
# print(liste)

"""
programlama dilleri ve çıkış yılları
"""

diller = ['python', 'java', 'javascript', 'C#']
yillar = [1989, 1995, 1995, 2000]
dilYil = dict()
for dil, yil in zip(diller, yillar):
    dilYil[dil] = yil

# print(dilYil)

dilYil2 = {dil: yil for dil, yil in zip(diller, yillar)}
# print(dilYil2)

"""
en sevdiğiniz çiçeğin isminin harflerini bir kümede gösterin.
"""

cicek = "orkide"

cicekHarfler = {harf for harf in cicek}
# print(type(cicekHarfler))

# endregion

# region iç içe comp

""" 
verilen iki listeyi birleştir
elemanlar ikili kombinasyon (tuple)
yeni listeye ekle
"""

harfler = ['a', 'b', 'c', 'd', 'e', 'f']
sayilar = [1, 2, 3, 4, 5, 6]

sozluk = []

for harf in harfler:
    for sayi in sayilar:
        tup = (harf, sayi)
        sozluk.append(tup)

# print(sozluk)


harfleri = ['a', 'b']
sayilari = [1, 2, 3]

sonuc = [
    (harf, sayi)
    for harf in harfleri
    for sayi in sayilari
]

# print(sonuc)

"""
1-10 arası sayıları, kendileri key ve kendinden küçük pozitif sayılar value listesi
"""
sayilarSozlugu = {}
for i in range(1, 11):
    for j in range(1, i+1):
        if not i in sayilarSozlugu:
            sayilarSozlugu[i] = [j]
        else:
            sayilarSozlugu[i].append(j)

# print(sayilarSozlugu)

sayilarSozlugu2 = {
    i: [j for j in range(1, i+1)]
    for i in range(1, 11)
}


# print(sayilarSozlugu2)

# endregion

# region if-else yapısı
"""
tekler = []

for i in range(1,21):
    if i % 2 == 0:
        tekler.append(i)
"""

tekler = [i
          for i in range(1, 21) if i % 2 != 0
          ]
# print(tekler)

carpanlar = {
    i: [j for j in range(2, i+1) if i % j == 0]
    for i in range(2, 21)
}

# print(carpanlar)
# endregion

""" QUIZ """

# region soru 1

"""
Soru 1:

Önce for dögüsü ile 1 den 10'a (hariç) kadar olan sayıların karelerini veren bir fonksiyon yazın. Adı kareleri_ver olsun.

Ardından aynı fonksiyonu comprehension ile yazın. Adı kareleri_ver_comp olsun.

[1, 4, 9, 16, 25, 36, 49, 64, 81]
"""


def karesi():
    kareListe = []
    for i in range(1, 10):
        kareListe.append(pow(i, 2))
    return kareListe


"""
a = karesi()
print(a)
"""


def kareListeComp():

    kareListe = [pow(i, 2) for i in range(1, 10)]
    return kareListe


"""
b = kareListeComp()
print(b)
"""
# endregion

# region soru 2

"""
Soru 2:

Parametre olarak bir cümlelerden oluşan bir paragraf listesi alan bir fonksiyon yazın. Adı cumleleri_ver olsun.

Fonksiyon bu paragraf listesi içindeki cümleleri dönsün.

Önce for döngüsü sonra comprehension ile yapınız. Comprehension ile fonksiyon adı cumleleri_ver_comp olsun.

paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]
"""


def cumleleriVer(liste: list):
    sozlukListesi = []
    for cumle in liste:
        sozlukListesi.append(cumle)
    return sozlukListesi


paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]
"""
a = cumleleriVer(paragraph)
print(a)
"""


def cumleleriVerComp(liste: list):

    cumleler = [cumle for cumle in liste]
    return cumleler


"""
a = cumleleriVer(paragraph)
print(a)
"""

# endregion

# region soru 3

"""
Soru 3:

Soru 2'deki paragrafı alıp bu sefer tüm cümlelerdeki tüm kelimeleri tek bir
liste içinde dönen bir fonksiyon yazalım. Adı kelimeleri_ver olsun.
cumleleriVer() fonksiyonunu kullanarak...

Önce for döngüleri ile sonra comprehension ile yapınız. Comprehension ile adı
kelimeleri_ver_comp olsun.

paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]

Sonuç:
['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 
'adipiscing', 'elit.', 'Ut', 'enim', 'ad', 'minim', 'veniam,',
'quis', 'nostrud', 'exercitation', 'ullamco.', 'Duis', 'aute',
'irure', 'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 
'velit', 'esse.', 'Excepteur', 'sint', 'occaecat', 'cupidatat',
'non', 'proident.']
"""


def kelimeleriVer(liste: list):
    kelimeler = []
    cumleler = cumleleriVer(liste)
    for cumle in cumleler:
        for kelime in cumle.split():
            kelimeler.append(kelime)
    return kelimeler


paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]
"""
a = kelimeleriVer(paragraph)
print(a)
"""


def kelimeleriVerComp(liste: list):
    cumleler = cumleleriVer(liste)
    kelimeler = [kelime for cumle in cumleler for kelime in cumle.split()]
    return kelimeler


"""
a = kelimeleriVerComp(paragraph)
print(a)
"""

# endregion

# region soru 4

"""
Soru 4:

Soru 2'deki paragrafı alıp bu sefer tüm cümlelerdeki sadece sesli harfle 
başlayan kelimeleri tek bir liste içinde dönen bir fonksiyon yazalım. 
Adı sesli_kelimeleri_ver olsun.

Önce for döngüleri ile sonra comprehension ile yapınız. Comprehension 
ile adı sesli_kelimeleri_ver_comp olsun.

paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]

Sonuç:
['ipsum', 'amet,', 'adipiscing', 'elit.', 'Ut', 'enim', 'ad', 'exercitation', 'ullamco.', 'aute', 'irure', 'in', 'in', 'esse.', 'Excepteur', 'occaecat']
"""

paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]


def sesliHarfleriVer(liste: list):
    kelimeler = kelimeleriVerComp(liste)
    sesliHarfler = ('a', 'e', 'u', 'i', 'o')
    sesliKelimeler = []
    for i in kelimeler:
        if i.startswith(sesliHarfler):
            sesliKelimeler.append(i)
    return sesliKelimeler


"""
a = sesliHarfleriVer(paragraph)
print(a)
"""


def sesliHarfleriVerComp(liste: list):
    kelimeler = kelimeleriVerComp(liste)
    sesliHarfler = ('a', 'e', 'u', 'i', 'o')
    return [i for i in kelimeler if i.startswith(sesliHarfler)]


"""
a = sesliHarfleriVerComp(paragraph)
print(a)
"""

# endregion

# region soru 5

"""
Soru 5:

Sıfırdan 20'e (dahil) kadar olan tüm sayıların karesini alan bir fonksiyon yazın. 
Adı kareler_sozlugu olsun.

Fonksiyon kareleri bir Dictionary olarak dönsün. Dictionary'nin key'i sayının 
kendisi, value'su ise sayının karesi olsun.

{sayi: karesi} şeklinde.

İpuçları:

döngü kullanmayın
direk comprehension ile yapın
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 
6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 
11: 121, 12: 144, 13: 169, 14: 196, 
15: 225, 16: 256, 17: 289, 18: 324, 
19: 361, 20: 400}
"""


def karelerSozlugu():

    kareler = {a: pow(a, 2) for a in range(21)}
    return kareler


"""
a = karelerSozlugu()
print(a)
"""
# endregion

# region soru 6

"""
Soru 6:

Parametre olarak bir sözlük alan bir fonksiyon yazın. Adı numaralari_ve_adlar olsun.

Parametre olarak gelen sözlük şu şekilde olacak:

{1: ['Aziz Vefa', 24],
 2: ['Kaiser Soze', 100],
 3: ['Zozo The Kid', 45],
 4: ['Jonny Lash', 70]}
Fonksiyonunuz sadece numaraları ve adları alarak yeni bir sözlük yaratacak ve bu sözlüğü dönecek.

Önce for döngüsü sonra comprehension ile yapınız. Comprehension ile fonksiyon adı numaralari_ve_adlar_comp olsun.

Sonuc:
{1: 'Aziz Vefa', 2: 'Kaiser Soze', 3: 'Zozo The Kid', 4: 'Jonny Lash'}
"""


def numaralariAdlari(sozluk: dict):
    yeniSozluk = {}
    for key, value in sozluk.items():
        yeniSozluk[key] = value[0]

    return yeniSozluk


sozluk = {1: ['Aziz Vefa', 24],
          2: ['Kaiser Soze', 100],
          3: ['Zozo The Kid', 45],
          4: ['Jonny Lash', 70]}
"""
a = numaralariAdlari(sozluk)
print(a)
"""


def numaralariAdlariComp(sozluk: dict):

    return {key: value[0] for key, value in sozluk.items()}


"""
a = numaralariAdlariComp(sozluk)
print(a)
"""
# endregion

# region soru 7

"""
Soru 7:

Parametre olarak bir sözlük alan bir fonksiyon yazın. Adı tek_numarali_adlar olsun.

Parametre olarak gelen sözlük şu şekilde olacak:

{1: ['Aziz Vefa', 24],
 2: ['Kaiser Soze', 100],
 3: ['Zozo The Kid', 45],
 4: ['Jonny Lash', 70]}
Fonksiyonunuz sadece tek numaraları ve adları alarak yeni bir sözlük yaratacak ve bu sözlüğü dönecek.

İpuçları:

dongu kullanmayın
direk comprehension ile yapınız
Sonuc:
{1: 'Aziz Vefa', 3: 'Zozo The Kid'}
"""


def tekNumaraliAd(sozluk: dict):
    yeniSozluk = {}
    for key, value in sozluk.items():
        if key % 2 != 0:
            yeniSozluk[key] = value[0]
    return yeniSozluk


sozluk = {1: ['Aziz Vefa', 24],
          2: ['Kaiser Soze', 100],
          3: ['Zozo The Kid', 45],
          4: ['Jonny Lash', 70]}
"""
a = tekNumaraliAd(sozluk)
print(a)
"""


def tekNumaraliAdComp(sozluk: dict):

    return {key: value[0] for key, value in sozluk.items() if key % 2 != 0}


"""
a = tekNumaraliAdComp(sozluk)
print(a)
"""

# endregion

# region soru 8

"""
Soru 8:

Parametre olarak İngilizce bir metin alan bir fonksiyon yazınız. Fonksiyonun adı kelime_uzunluklari olsun.

Fonksiyon iki liste dönsün. Listelerden biri kelimeleri içersin. Diğer liste ise kelime uzunluklarını.

Eğer kelime ('the', 'in', 'as', 'at') kelimelerinden biri ise onu almasın.

İpuçları:

bir fonksiyon nasıl iki liste döner? -> Tuple
döngü kullanmayın
comprehension ile yapın
Parametre:
"It takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!"

Sonuc:
['It', 'takes', 'all', 'running', 'you', 'can', 'do,', 'to', 'keep', 'same', 'place.', 'If', 'you', 'want', 'to', 'get', 'somewhere', 'else,', 'you', 'must', 'run', 'least', 'twice', 'fast', 'that!']
[2, 5, 3, 7, 3, 3, 3, 2, 4, 4, 6, 2, 3, 4, 2, 3, 9, 5, 3, 4, 3, 5, 5, 4, 5]
"""


def kelimeUzunlugu(metin: str):

    yasak = ('the', 'in', 'as', 'at')
    kelimeler = metin.split()
    kelimeList = [kelime for kelime in kelimeler if kelime not in yasak]
    uzunlukList = [len(kelime) for kelime in kelimeler if kelime not in yasak]
    return (kelimeList, uzunlukList)


metin = "It takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!"
"""
a = kelimeUzunlugu(metin)
print(a)
"""
# endregion

# region soru 9

"""
Soru 9:

Parametre olarak bir sayı listesi alan bir fonksiyon yazın. Adı sadece_pozitifler olsun.

Fonksiyon liste içinden sadece pozitif sayıları alsın, tam sayı yapsın ve yeni bir liste olarak dönsün. Comprehension ile yapınız.

Parametre:
[12.8, -27.2, -34.5, 58.4, -82.0, 66.6, 14.9]

Sonuc:
[12, 58, 66, 14]
"""


def sadecePozitif(l1: list):

    return [int(sayi) for sayi in l1 if sayi > 0]


parametre = [12.8, -27.2, -34.5, 58.4, -82.0, 66.6, 14.9]
"""
a = sadecePozitif(parametre)
print(a)
"""
# endregion

# region soru 10

"""

Soru 10:

Parametre olarak içinde listeler olan, iki seviyeli bir liste alan fonksiyon yazın. Adı listeyi_duzlestir olsun.

Fonksiyon listenin altındaki tüm listleri düzleştirip, geriye tek seviyeli bir liste dönsün.

İpuçları:

döngü kullanmayın
comprehension ile yapın
Parametre:
listeler_listesi = [[8,6], [3,1,4], [2,0,9], [5]]

Sonuc:
[8, 6, 3, 1, 4, 2, 0, 9, 5]
"""


def listeyiDuzlestir(l1: list):

    return [sayi for liste in l1 for sayi in liste ]

listeler_listesi = [[8,6], [3,1,4], [2,0,9], [5]]
"""
a = listeyiDuzlestir(listeler_listesi)
print(a)
"""

# endregion