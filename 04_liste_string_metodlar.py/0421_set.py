# region set

"""
set → küme
- Birden çok değeri tek bir değişkende tutmak için kullanılır.
- sırasız ve indexlenmemiş koleksiyonlardır. (unordered,unindexed)
- İki şekilde oluşturulabilir.
  - süstlü parantez ve içinde eleman kullanarak
  - set() constructor ile
- Set elemanları tekildir.
"""

# endregion

# region set yaratma

kume = {'direnç', 'kondansatör', 'bobin'}
# print(type(kume))

harfler = set({'a', 'b', 'c'})
# print(harfler)
# print(type(harfler))

# endregion

# region aynı eleman

"""
Bir eleman ikinci defa kullanılamaz.
"""
notlar = [23, 24, 25, 26, 27, 28, 23]
notlarKumesi = set(notlar)
# print(notlarKumesi)
"""her elemanı 1 kere yazdı.(tekilleştirdi)"""
# indexli yapısı yoktur.
# endregion

# region set metodları

"""
KESİŞİM
iki set'in (kümenin) ortak elemanlarını bulmak için (kesişim kümesi)
intersection
"""

notlar = [23, 74, 65, 96, 17, 458, 53, 'A', 'B', 'C']
notlarKumesi = set(notlar)
dereceler = ['A', 'B', 'C', 'D', 'E', 'F']
dereceKumesi = set(dereceler)

# print(notlarKumesi.intersection(dereceKumesi)) # kesişen elemanları verir.

"""
BİRLEŞİM
union
"""

# print(dereceKumesi.union(notlar)) # birleştirir

"""
Kümelerin eleman farkı
differance
"""

# print(notlarKumesi.difference(dereceKumesi))
# print(dereceKumesi.difference(notlarKumesi))

"""
ALT KÜME
issubset
"""

# print(set({'F','E'}).issubset(dereceKumesi))

# endregion

# region ELEMAN VE ATAMA İŞLEMLERİ


siniflar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sinifKumesi = set(siniflar)

sinifAdlari = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
sinifAdiKumesi = set(sinifAdlari)

sinifKumesi.add('Üni-1')
sinifAdiKumesi.remove('G')
sinifAdiKumesi.add('D5')
# print(sinifKumesi)
# print(sinifAdiKumesi)

# endregion

# region döngü
"""
for eleman in sinifAdiKumesi:
    print(eleman)
"""
# endregion

# region setlerde atama işlemi

"""
'''
ALising
'''
Setlerde atama işlemi, aslında bir alising işlemidir.
"""

a = {1, 2, 3}
b = a
"""
b.add('yeni')
print(a)
print(b)
"""
'''
a ile b aynı yerde saklanır. b üerindeki değişim a'da da gerçekleşir
'''

# endregion

# region sete birden fazla eleman ekleme

c = [7,8,9,10]
a.update(c)
print(a)

# endregion