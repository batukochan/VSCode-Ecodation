# region Ödev Giriş

"""
Ödev 3 - Veri Yapıları
Telif hakkı olmadan yazılı metin kaynağı: http://gutenberg.org/

Pride and Prejudice by Jane Austen: http://gutenberg.org/ebooks/1342

Alice's Adventures in Wonderland by Lewis Carroll: http://gutenberg.org/ebooks/11

Bu ödevde iki farklı kitap üzerinde, Python kullanarak çeşitli bilgiler toplayacaksın.

Bu sayede hem şimdiye kadar öğrenmiş olduğun kavramları (değişkenler, fonksiyonlar, veri yapıları ...) 
tekrar etmiş olacak hem de bu kavramları gerçek bir uygulama üzerinde görmüş olacaksın.

Kullanacağın ana fonksiyonlar, başta tanımlanmış olarak verilecek. Bu fonksiyonları anlamak ve kullanmak sana kalmış.

İyi eğlenceler :)

# TO-DO olarak gördüğün yerlerde gerekli kodları yaz.

Kitapları Okuyalım:

Bu iki kitabı Python'a okutarak kitaplarda geçen tüm kelimeleri bulalım:

Bunu yaparken:

noktalama işaretlerini çıkaralım -> string.punctuation
boşluk karakterlerini (boşluk, yeni satır, tab vs.) çıkaralım -> string.whitespace
kitapların başlangıç ve sonunu bulalım
her işlemi kendi fonksiyonunda yapalım
string modülünü kullanalım
"""

import string
from collections import Counter

noktalamaIsaretleri = string.punctuation
boslukkarakterleri = string.whitespace


def kelimeleriDoldur(file, kelimeler):

    # Python dosyayı satır satır okuyacak
    for satir in file:

        # sona gelmiş miyiz diye kontrol et
        if not sonaGelindiMi(satir):
            # satır içindeki kelimeleri alalım
            satirKelimeleri = satirdakiKelimeler(satir)

            # şimdi kelimeler listemize satir_kelimeleri'ni ekleyelim
            # ikisi de liste olduğu için -> extend()
            kelimeler.extend(satirKelimeleri)


def dosyadanOku(kitapAdi):

    kitapYolu = "C:\\Users\\batuh\\Downloads\\" + kitapAdi + '.txt'

    return open(kitapYolu, encoding="utf-8")


def baslangiciAtla(file):

    atlamaMetni = '*** START OF THIS PROJECT'

    # file her okumada okunduğu yere kadar ilerlediği için
    # '*** START OF THIS PROJECT' ile başlayan bölüme kadar okutup
    # dönsek, okuma yeri olması gereken yere gelir

    for satir in file:
        if satir.startswith(atlamaMetni):
            break

# sona gelinip gelinmediğini kontrol eder
# bu bölümden sonrası kitaba dahil değildir


def sonaGelindiMi(satir):

    bitirmeMetni = '*** END OF THIS PROJECT'

    # eğer mevcut satır bitirme metnine geldiyse true dön
    # '*** END OF THIS PROJECT' ile başlayan satır

    return satir.startswith(bitirmeMetni)

# Kitap Okuma Fonksiyonu


def kitapOku(kitapAdi):
    """
        Verilen kitap adına sahip kitabı okur
        Parametre: str kitap_adi
        Sonuc: list kelimeler
    """

    # kelimeleri tutalım
    kelimeler = list()

    # önce file olarak okuyalım
    file = dosyadanOku(kitapAdi)

    # şimdi '*** START OF THIS PROJECT' kısmına kadar atlayalım
    baslangiciAtla(file)

    # şimdi kelimeleri dolduralım
    kelimeleriDoldur(file, kelimeler)

    return kelimeler

# Satırdaki Kelimeleri getiren fonksiyon


def satirdakiKelimeler(satir):

    # satırdaki kelimeleri tutan liste
    satirKelimeleri = []

    # satir'i kelime dizisine dönüştürelim
    kelimeDizisi = satir.split()

    # şimdi kelimeler üzerinde dönelim
    for kelime in kelimeDizisi:
        # eğer kelime'de noktalama işareti varsa silelim
        kelime = kelime.strip(noktalamaIsaretleri)

        # küçük harf yapalım
        kelime = kelime.lower()

        if len(kelime) and kelime.isalpha() > 0:
            # kelime'yi, satirdaki_kelimeler'e ekeleyelim
            satirKelimeleri.append(kelime)

    return satirKelimeleri


"""
Alıştırma 1:

Pride and Prejudice ve Alice Adventures in Wonderland kitaplarını Python ile okuyup içindeki kelimelere bakacaksın.
"""

kitapAdi = "Pride_and_Prejudice"

prideKelimeleri = kitapOku(kitapAdi)

# print(prideKelimeleri[:20])

kitapAdi2 = 'Alice_Adventures_in_Wonderland'

aliceKelimeleri = kitapOku(kitapAdi2)
# print(aliceKelimeleri[:20])


"""
Alıştırma 2:

Şimdi kelimleri uzunluk sırasına göre, her iki yönlü sırala. (azalan ya da artan olarak)
"""


def listeSirala(liste: list, azalanMi):

    return sorted(liste, key=lambda x: len(x), reverse=azalanMi)


prideKelimeleriA = listeSirala(prideKelimeleri, False)
# print(prideKelimeleriA[:20])
prideKelimeleriB = listeSirala(prideKelimeleri, True)
# print(prideKelimeleriB[:20])

"""
# TO-DO - Alice Adventures in Wonderland'deki kelimleri kısadan uzuna sırala

alice_kelimeleri = .......

# TO-DO - İlk 20 kelimeyi yazdır
"""


aliceKelimeleriA = listeSirala(aliceKelimeleri, False)
#print(aliceKelimeleriA[:20])
aliceKelimeleriB = listeSirala(aliceKelimeleri, True)
#print(aliceKelimeleriB[:20])

"""
Alıştırma 3:

Güzel! Kelimeleri okudun, fakat ufak bir sorun var: bir kelime birden fazla geçiyor.

Şimdi listeleri Set yapıp tekrarlardan kolayca kurtulabilirsin.

"""

def tekrarlariSil(liste):
    """
        List'i önce Set yapıp tekrarları sil, 
        sonra tekrar List yapıp geri ver.
        Parametre: list liste
        DÖnüş: list tekrarsiz_liste
    """
    # liste'yi set yapıp tekrarlardan kurtul
    kume = set(liste)
    
    #  tekrar list yap
    # böylece tekrarladan kurtulmuş olacaksın
    tekrarsizListe = list(kume)
    
    #  tekrarsiz_liste'yi dön

    return tekrarsizListe

prideKelimeleriTekrarsiz = tekrarlariSil(prideKelimeleri)
#print(prideKelimeleriTekrarsiz[:20])

aliceKelimeleriTekrarsiz = tekrarlariSil(aliceKelimeleri)
#print(aliceKelimeleriTekrarsiz[:20])

"""
Alıştırma 4:

Şimdi her iki kitapta geçen toplam ve farklı kelime sayısını bul.
"""

# Kelime Sayısını Dönen Fonksiyon

def kelimeSayisi(liste):

    # TO-DO - Bir listenin eleman sayısını nasıl bulursun?
    elemanSayisi = len(liste)
    return elemanSayisi

prideKelimeSayisi = kelimeSayisi(prideKelimeleri)
#print(prideKelimeSayisi)

aliceKelimeSayisi = kelimeSayisi(aliceKelimeleri)
#print(aliceKelimeSayisi)

prideKelimeSayisiT = kelimeSayisi(prideKelimeleriTekrarsiz)
#print(prideKelimeSayisiT)

aliceKelimeSayisiT = kelimeSayisi(aliceKelimeleriTekrarsiz)
#print(aliceKelimeSayisiT)

"""
Alıştırma 5:

Şimdi herbir kelimenin kaç sefer geçtiğini bul.

Önce kendin fonksiyonlar ve comprehension'lar yardımı ile yap.

En yüksek adetli olan n (örneğin 20) kelime'yi almak istesen:
"""

# en yüksek adetli n kelimeyi veren fonskyion

def enYuksekAdetli(liste, n=20):
    
    # sözlük olarak dönecek
    prideKelimeAdetleri = {
        kelime: liste.count(kelime)
        for kelime in liste
    }
    
    # bu sözlüğü sıralamamız lazım
    # bize sıralı liste olarak gelecek
    siraliListe = sozlukSirala(prideKelimeAdetleri)
    
    # şimdi en yüksek adetli n tanesini alalım -> slice
    siraliListeTopn = siraliListe[:n]
    
    # şimdi sirali_liste_top_n listemizi dict yapıp geri dönelim
    return dict(siraliListeTopn)

def sozlukSirala(sozluk):
    
    # önce sözlüğü value'larına göre sıralayalım -> sorted()
    # hatırlayalım: sorted() geriye bir liste dönerdi
    # sorted()'a vereceğimiz iterable bir sözlük olacağı için geriye (key, value) şeklinde Tuple'lar dönecek
    
    siraliListe = sorted(sozluk.items(), key=lambda x: x[1], reverse=True)
    
    # şimdi sırali_listeyi dönelim
    return siraliListe
'''
aliceKelimeAdetleriF = enYuksekAdetli(aliceKelimeleri)
#print(aliceKelimeAdetleriF)
'''

"""
Sıralama yapıp en yüksek adetlileri aldık ama biraz zahmetli oldu.

Daha kolay ve Pythonic bir yolu yok mu? Evet, var.

Bunun için Python'un collections modülünden Count class'ını kullanacağız.
"""
'''
aliceKelimeAdetleriA = Counter(aliceKelimeleri)
#print(aliceKelimeAdetleriA)
aliceKelimeAdetleriB = Counter(aliceKelimeleri).most_common(20)
#print(aliceKelimeAdetleriB)
'''
"""
Bakın, birebir bizim comprehension'lar ile bulduğmuz sonuç.

Ama veri tipinde bir fark var. Biz Dictionary olarak aldık, burada ise içinde Tuple'lar olan bir List dönmüş.

Eğer dict tipine çevirmek istersek çok basit olarak cast yapabiliriz:
"""

'''
aliceKelimeAdetleriSozlugu = dict(aliceKelimeAdetleriB)
#print(aliceKelimeAdetleriSozlugu)
'''

"""
# Pride and Prejudice'deki kelimeler ve sayıları
# comprehension ile manuel yapsak onlarca dakika sürebilirdi.
# Ama Counter ile çok kısa

# TO-DO - Pride and Prejudice'deki kelimeler ve sayılarını bul
pride_kelime_adetleri = ........
print(pride_kelime_adetleri)
"""
"""
prideKelimeSayisiCounter = Counter(prideKelimeleri)
print(prideKelimeSayisiCounter)
"""
prideKelimeSayisiCounter = Counter(prideKelimeleri).most_common(20)
print(dict(prideKelimeSayisiCounter))