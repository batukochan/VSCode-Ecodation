# region open()

# open() fonksiyonu bize bir file nesnesi döner

file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')
'''
print(file.readline())
print(file.readline())
a = file.readline()
a = a.split()
print(a) # ['dolor']
'''
"""
   kernel dosyayı satır satır okuyup kaldığı yerde durduğu için,
tüm dosyaya bakmak için tekrar okumamız lazım...
→ file = open('kelimeler.txt')
"""
'''
for index, line in enumerate(file):
    if index <= 20:
        kelimeDizisi = line.split()   
        print(kelimeDizisi)
    else:
        break
'''

# endregion

# region uzunluğu 10 karakterden uzun kelimeleri yazdır

"""
file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')
for i in file:
    kelime = i.split() #liste döner
    sozcuk = kelime[0] #listemizde bir adet veri var.
    if len(sozcuk) > 10:
        print(kelime)
"""

# endregion

# region içinde ingilizce sesli harf olmasın

"""
file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')

sesliHarf = ['a', 'e', 'i', 'o', 'u']

for satir in file:
    kelime = satir.split()
    sozcuk = kelime[0]
    for i in range(len(sesliHarf)):
        if sesliHarf[i] in sozcuk.lower():
            break
    else:
        print(kelime)
"""

# endregion

# region 'ae' geçen

"""
file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')

for satir in file:
    kelime = satir.split()
    sozcuk = kelime[0]
    if 'ae' in sozcuk:
        print(kelime)
"""

# endregion

# region yasak harf bulma (function)


def yasakHarfVarMi(metin, yasakHarf):

    for harf in metin:
        if harf in yasakHarf:
            return True
    else:
        return False


""" 
cumle = 'Bu bir normal metindir.'
yasakHarf = 'x'
print(yasakHarfVarMi(cumle,yasakHarf))
"""

# endregion

# region sadeceSunlariKullanir()
"""
    Bu fonksiyon bir metin ve harflerden oluşan bir string alsın.
Ve eğer metin sadece bu harfleri kullanıyosa True, bunlardan başka 
bir harf kullanıyorsa False dönsün.
"""


def sadeceSunlariKullanir(metin, harfler):

    for harf in metin:
        if harf.isalpha() and harf not in harfler:
            return False
    else:
        return True


"""
cumle = 'ey edip adanada pide ye'
harfler = 'adeinpy'
print(sadeceSunlariKullanir(cumle,harfler))
cumle = 'kartal kalkar dal salkar'
harfler = 'kartlds'
print(sadeceSunlariKullanir(cumle,harfler))
"""

# endregion

# region alıştırma 5

"""
Alıştırma 5:
    4 numaralı Alıştırma'daki sadece_sunlari_kullanir fonksiyonunu 
kullanarak; Lorem Ipsum kelimelerinden (1. Alıştırma) sadece 'ens' 
harflerini kullanan kelimeleri bulabilir misin?
"""

file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')


def loremSadeceBunlariKullanir(harfler):
    for satir in file:
        kelime = satir.split()
        sozcuk = kelime[0]
        if sadeceSunlariKullanir(sozcuk, harfler):
            print(kelime)


"""
harfler = "ens"
loremSadeceBunlariKullanir(harfler)
"""

# endregion

# region alıştırma 6

"""
Alıştırma 6:
    Adı hepsini_kullanir olan bir fonksiyon yaz.Bu fonksiyon bir metin ve 
harflerden oluşan bir string alsın. Eğer metin bu harfleri tümünü enaz bir
kere kullanıyosa True, herhangi bir harfi hiç kullanmıyorsa False dönsün.    
"""


def hepsiniKullanir(metin, harfler):
    tumunuKullanir = True
    for harf in harfler:
        if harf not in metin:
            tumunuKullanir = False
    return tumunuKullanir


"""
harfler = 'aecbd'
metin = 'Araba demir yolundan geçti'
print(hepsiniKullanir(metin, harfler))
harfler = 'aecbd'
metin = 'Araba demir yolundan gecti'
print(hepsiniKullanir(metin, harfler))
"""

# endregion

# region

"""
Alıştırma 7:

    6 numaralı Alıştırma'da tanımladığın hepsini_kullanir 
fonksiyonunu kullanarak: Lorem (1. Alıştırma) kelimelerinden 
hangilerinin 'aei' harflerinin tümünü kullandığını bul.
"""
file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')


def hepsiniKullanirLorem(harfler):

    for satir in file:
        kelime = satir.split()
        sozcuk = kelime[0]
        if hepsiniKullanir(sozcuk, harfler):
            print(kelime)


"""
harfler = "aei"
hepsiniKullanirLorem(harfler)
"""

# endregion

# region alıştırma 8
"""
Alıştırma 8:

    4 numaralı Alıştırma'daki sadece_sunlari_kullanir fonksiyonunu ve 6 numaralı 
Alıştırma'da tanımladığın hepsini_kullanir fonksiyonunu beraber kullanarak: Lorem 
(1. Alıştırma) kelimelerinden hangilerinin sadece 'fir' harflerini ama bu harflerin
tümünü kullandığını bul.Yani kelimenin içinde hem 'fir' geçecek hem de sadece f,i,r
harflerinden oluşacak.
    Fonksiyonunun adı sadece_tumunu_kullanir olsun ve parametre olarak harfleri alsın.
"""


def sadeceTumunuKullanir(harfler):
    file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')
    for satir in file:
        kelime = satir.split()
        sozcuk = kelime[0]
        if hepsiniKullanir(sozcuk, harfler) and sadeceSunlariKullanir(sozcuk, harfler):
            print(kelime)


"""
harfler = "fir"
print(sadeceTumunuKullanir(harfler))
"""

# endregion

# region alıştırma 9
"""
Alıştırma 9:

Eğer bir kelimenin harfleri alfabetik sırada ise bu kelimeye düzgün kelime diyelim.
İsmi duzgun_kelime_mi olan ve parametre olarak bir kelime alan, bir fonksiyon yaz.
Eğer kelime düzgün kelime ise True, değilse False dönsün.

Düzgün Kelime Örnekleri: buz, agor
"""


def duzgunKelime(kelime):

    ilkHarf = kelime[0]

    for harf in kelime:

        if ilkHarf > harf:  # harfin indexi daha küçük yani daha önce
            return False

        ilkHarf = harf

    return True


"""
kelime="buz"
print(duzgunKelime(kelime))
"""
# endregion

# region loremdeki kelimelerin düzgün olanlarını bulalm


def duzgunKelimeLorem():

    file = open('C:\\Users\\batuh\\Downloads\\kelimeler.txt')
    for satir in file:
        kelime = satir.split()
        sozcuk = kelime[0]
        if duzgunKelime(sozcuk):
            print(kelime)


duzgunKelimeLorem()

# endregion
