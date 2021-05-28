import string
from collections import Counter
from typing import ByteString, KeysView

"""
    global değişken, bütün çalışan kod ortamımızda her yerden 
ulaşabileceğimiz değişken olarak düşünebiliriz.
"""

noktalamaİsaretleri = string.punctuation
"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
boslukKarakterleri = string.whitespace

# region okuma işlemi



def dosyaCagir(kitapAdi):
    kitaYolu = "C:\\Users\\batuh\\Downloads\\" + kitapAdi + '.txt'
    return open(kitaYolu, encoding='utf-8')


def baslangiciAtla(file):
    # başlangıç bölümünü atlar.
    atlamaMetni = '*** START OF THIS PROJECT'
    for satir in file:
        if satir.startswith(atlamaMetni):
            break


def sonaGelindiMi(satir):

    bitirmeMetni = '*** END OF THIS PROJECT'
    return satir.startswith(bitirmeMetni)


def satirdekiKelimeler(satir):
    """
    Satırdaki kelimeleri getirir.
    """
    satirKelimeleri = []
    kelimeDizisi = satir.split()
    for kelime in kelimeDizisi:
        # eğer kelimede noktalamaişareti varsa atmalıyız.
        
        kelime = kelime.strip(noktalamaİsaretleri)
        kelime = kelime.lower()
        if kelime.isalpha() and len(kelime) > 0:
            satirKelimeleri.append(kelime)
    
    return satirKelimeleri


def kelimeleriDoldur(file, kelimeler):
    """
    Kelimeleri doldurur.
    parametre: file, kelimeler
    """
    # python dosyayı satır satır okur
    for satir in file:
        # son cümlede okumayı bitirmeliyiz.
        if not sonaGelindiMi(satir):
            satirKelimeleri = satirdekiKelimeler(satir)

            # kelimeler listesine eklenir
            kelimeler.extend(satirKelimeleri)


def kitapOku(kitapAdi: str):
    """
    Girilen kitap için okuma yapar.
    Parametre: string
    Return: list kelimeler
    """

    # kelimeleri tutacağımız listeyi yaratırız.

    kelimeler = []
    file = dosyaCagir(kitapAdi)

    # kitabın başlığına kadar olan kısmı atlayalım.
    baslangiciAtla(file)

    # kitabın içindeyiz
    # kelimeleri dolduracağız

    kelimeleriDoldur(file, kelimeler)

    return kelimeler

kitapAdi = "Pride_and_Prejudice"

prideKelimeleri = kitapOku(kitapAdi)

#print(prideKelimeleri[:20])