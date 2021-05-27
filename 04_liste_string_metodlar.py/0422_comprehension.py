# region

"""
1-10 arası sayıların karelerini içeren liste oluştur.
"""

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
print(dilYil2)

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
        tup = (harf,sayi)
        sozluk.append(tup)

#print(sozluk)


harfleri = ['a', 'b']
sayilari = [1, 2, 3]

sonuc =  [
    (harf,sayi)
    for harf in harfleri
    for sayi in sayilari
]

#print(sonuc)

"""
1-10 arası sayıları, kendileri key ve kendinden küçük pozitif sayılar value listesi
"""
sayilarSozlugu = {}
for i in range(1,11):
    for j in range(1,i+1):
        if not i in sayilarSozlugu:
            sayilarSozlugu[i] = [j]
        else:
            sayilarSozlugu[i].append(j)

#print(sayilarSozlugu)

sayilarSozlugu2 = {
    i:[ j for j in range(1,i+1)]
    for i in range(1,11)
}


#print(sayilarSozlugu2)

# endregion

# region if-else yapısı
"""
tekler = []

for i in range(1,21):
    if i % 2 == 0:
        tekler.append(i)
"""

tekler = [i
    for i in range(1,21) if i % 2 != 0 
]
#print(tekler)

carpanlar = {
    i: [j for j in range(2,i+1) if i % j ==0]
    for i in range(2,21) 
}

#print(carpanlar)
