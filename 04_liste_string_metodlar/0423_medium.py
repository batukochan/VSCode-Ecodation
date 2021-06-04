
# region liste oluşturma ve index yapısı

"""
Liste nasıl oluşturulur  ?
1 → dogaListesi = ['hayvanlar','ağaçlar','denizler']
"""
# liste oluşturma

dogaListesi = ['hayvanlar', 'ağaçlar', 'denizler']

"""
print(dogaListesi) # ['hayvanlar','ağaçlar','denizler']

print(dogaListesi[2]) # denizler
"""
# endregion

# region type

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
print(type(sayilar)) # <class 'list'>
"""

# endregion

# region eleman farklılığı

elemanlar = [
    11, 15, 12, 8.9,
    "ahmet", "50 sayfa",
    True, False
]  # elemanlar farklı tipte olabilir.

# print(elemanlar)

"""
→ Çıktı: [11, 15, 12, 8.9, 'ahmet', '50 sayfa', True, False]
"""

# endregion

# region eleman degistirme

"""
# Aynı elemanlar, aynı listede bulunabilir.
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 12, 13, 15]
sayilar[2] = "yedi"  # index 2'deki '7' elemanı yerine 'yedi' elemanı atanır.
print(sayilar)
# → [11, 15, 'yedi', 12, 1, 0, 3.14, 12, 13, 15]
"""
"""
sayilar = [11, 15, 7, 12]
print(sayilar)
# → [11, 15, 7, 12]
sayilar[1] = sayilar[3]
print(sayilar)
# → [11, 15, 7, 12]
"""
# endregion

# region listenin uzunluğu len
"""

sayilar = [1, 2, 7, 132, 5]
print(len(sayilar))  # eleman sayı olarak da düşünülebilir.
print(sayilar[len(sayilar)//2])
"""
# endregion

# region del talimatı
"""
sayilar=[11,15,7,12,15]

print(sayilar)
# Çıktı → [11, 15, 7, 12, 15]
print(len(sayilar)) # 5
del sayilar[-2] # 12 elemanını sildi.

print(sayilar)
# Çıktı → [11, 15, 7, 15]

'''
del sayilar #intellisense dersek listeyi siler ve nameerror verir.
'''
print(sayilar[len(sayilar)-1]) #son elemanı bize verir.
"""
# endregion

# region liste üzerinde gezme
"""
evcilHayvalar = ['kedi', 'köpek', 'muhabbet kuşu', 'hamster']

for i in evcilHayvalar:
    print(i,end=' ')
# Çıktı → kedi köpek muhabbet kuşu hamster 

print() # bir sonraki yapı ile karışmasın diye eklendi.

''' Eğer listenin indexini almak istersek enumerate kullanılır.'''

for index ,hayvan in enumerate(evcilHayvalar):
    print(f"{index}-{hayvan}")


for i,j in enumerate(evcilHayvalar):
    print(i,j,end=' ')
# Çıktı → 0 kedi 1 köpek 2 muhabbet kuşu 3 hamster
"""
# endregion

# region liste içinde dönerken eleman değiştirme

bilgisayarBilesenleri = [
    'monitör', 'anakart',
    'ekran kartı', 'mause'
    'ram', 'ssd', 'işlemci'
]
"""
for i, bilesen in enumerate(bilgisayarBilesenleri):
    if bilesen == bilgisayarBilesenleri[(len(bilgisayarBilesenleri)-1)]:
        bilesen = '***yeni*** ' + bilesen
    print(i,bilesen)
"""
"""
0 monitör
1 anakart
2 ekran kartı
3 mauseram
4 ssd
5 ***yeni*** işlemci
"""

# endregion

# region liste elemanlarını topla

liste = [1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10]
toplam = 0

for eleman in liste:
    if type(eleman) == int:
        toplam += eleman

# print(f"Listedeki sayıların toplamı {toplam}")

# endregion

# region steak heap

list1 = [1, 2]
list2 = [3, 4]
# -------------
list1 = list2
"""
Bu işlem iki listeyi aynı adrese kaydeder.
iki listenin de değeri şu andan itibaren → [3,4]
"""
print(list1)  # [3,4]
print(list2)  # [3,4]
list2[0] = 2
print(list1)  # [2,4]

# endregion