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

# print(prideKelimeleri[:20])

# KELİMELERİ UZUNLUK SIRASINA GÖRE DİZELİM.


def listeleriSirala(liste, azalanMi):
    # uzunluk ile sıralayacaksak -> key parametresini vermemiz lazım
    return sorted(liste, reverse=azalanMi, key=lambda z: len(z))


"""
prideKelimeleri = listeleriSirala(prideKelimeleri,azalanMi=False)
print(prideKelimeleri[:20]) # en kısa kelimeler (kısadan->uzuna)
prideKelimeleri = listeleriSirala(prideKelimeleri,azalanMi=True)
print(prideKelimeleri[:20])# en uzun kelimeler (uzundan->kısaya)
"""


def tekrarlariSil(liste: list):

    kume = set(liste)

    return list(kume)


"""
prideKelimeleriFarkli = tekrarlariSil(prideKelimeleri)

print(prideKelimeleri[:20]) # en kısa kelimeler (kısadan->uzuna)
"""


def kelimeSayisi(liste: list):
    return len(liste)


"""
prideKelimeleriSayisi = kelimeSayisi(prideKelimeleri)
print(prideKelimeleriSayisi)
"""

# farklı kelime sayısı
"""
prideKelimeleriFarkli = tekrarlariSil(prideKelimeleri)
prideKelimeleriFarkliSayisi = len(prideKelimeleriFarkli)
print(prideKelimeleriFarkliSayisi)
"""

# Hangi kelime kaç kere geçiyor ?


def sozluksirala(sozluk: dict):

    # value sırası
    siraliListe = sorted(sozluk.items(), key = lambda x: x[1], reverse=True)
    return siraliListe


def enYuksekAdetli(liste: list, n=20):

    # sözlük olarak dönecek
    sozluk = {
        kelime: liste.count(kelime)
        for kelime in liste
    }

    siraliListe = sozluksirala(sozluk)
    siraliListeTopn = siraliListe[:n]

    return dict(siraliListeTopn)

kitapAdi = "Alice_Adventures_in_Wonderland"
"""
aliceKelimeleri = kitapOku(kitapAdi)

aliceKelimeAdetleri = enYuksekAdetli(aliceKelimeleri)
print(aliceKelimeAdetleri)
"""
# doğrusu counter kullanmak
"""
prideKelimeAdetleri = Counter(prideKelimeleri).most_common(40) # en fazla geçen 40 kelime
print(prideKelimeAdetleri)
"""

# endregion