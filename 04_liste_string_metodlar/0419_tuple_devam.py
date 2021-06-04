# region tuple yaratmak
"""
tuple1 = 'a', 'b', 'c', 'd'
print(tuple1)
print(type(tuple1))

tuple2 = ('a', 'b', 'c', 'd', '3', '23')
print(isinstance(tuple2, tuple))  # True

# tek elemanlı tuple

tuple3 = 'a',
'''
a = 'x' # str
b = ('x') # str
'''
print(isinstance(tuple3, tuple))  # True

tuple4 = tuple()

print(isinstance(tuple4, tuple))  # True

dil = tuple('Python')
# print(dil,type(dil)) # ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'>

print(dil[3])  # h, index ile kullanılabilir.

'''
tuple, değiştirilemez.
'''
print(dil[::])
print(dil[::-1])  # tersten yazabiliriz.

# tuple karşılaştırma

print((0, 1, 2) < (3, 4, 5))

# ilk önce 5 ile 6yı karşılaştırır gerisine bakmaz.
print((5, 40, 200) < (6, 3, 5))

print(('abcd2',) < ('abcd3',))
"""

# endregion

# region tuple atama
"""
a = 99
b = 1
a, b = b, a
print('a:', a)
print('b:', b)
'''
değişken sayısı eşit olmalıdır.
a, b = 300, 400, 500
'''
"""

"""
a = (32, 74, 23)
b = (10, 20, 30)
a, b = b, a
# print(a,b)
c = (22, 23, 24, 25)
a, c = c, a
print(a, c)
"""
"""
a, b, c, d, e = ['her', 'şey', 'çok', 'güzel', 'olacak']
print(a,type(a)) #str
print(b)
print(c)
print(d)
print(e)
"""
# endregion

# region return tuple

'''
Çoklu değer döndürmek amacıyla kullanılabilir.
'''
"""
sonuc = divmod(32, 3)
print(sonuc)  # (10,2) bölüm,kalan
print('kalan = ',sonuc[1]) # kalan =  2

bolum, kalan = divmod(32,3)
print(f'bölüm = {bolum}, kalan = {kalan}') # bölüm = 10, kalan = 2
"""

# endregion

# region örnek

'''
parametre sayısı belli olmayan bir fonksiyon yazalım.
'''


def toplamCarpim(*args):
    '''
    *args yapısı bir tuple'dır.
    '''
    toplam = sum(args)
    carpim = 1
    for arg in args:
        carpim *= arg

    return (toplam, carpim)


toplam, carpim = toplamCarpim(2, 4, 6, 8, 10)

#print(f"Sayıların toplamı {toplam}, sayıların çarpımı {carpim}")

# endregion

# region örnek 2

'''
Parametre olarak bir tam sayı listesi alan ve bu listenin minimum maksimum 
ve aritmetik ortalamasını veren bir fonk yazın.
'''


def minMaxAort(l1: list):
    import statistics

    minimum = min(l1)
    maksimum = max(l1)
    """
    toplam = 0
  
    for sayi in l1:
        toplam += sayi
    aOrt = toplam/len(l1)
    """
    aOrt = statistics.mean(l1)  # paket ile işler daha kolay!

    return (minimum, maksimum, aOrt)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi, ma, ort = minMaxAort(l1)
"""
print(f'''
listenin en küçük elemanı {mi}
listenin en büyük elemanı {ma}
listenin aritmatik ortalaması {ort}
''')
"""

# endregion

# region zip fonksiyonu

metin = 'fermuar'
listem = [1, 2, 3, 4, 5, 6, 7]

zipNesnesi = zip(metin, listem)
"""
print(zipNesnesi)  # <zip object at 0x0000025C01F0A200>
"""
"""
zip() fonksiyonun geriye döndüğü zip nesnesi bir #iteratör döner.
#iteratörler içinde sayılabilir değerler tutan ve üzerinde döngü kurulabilen (iterate olabilen)
nesnelerdir.
#iteratörler, listelere benzer fakat list'ler gibi onların üzerinde index ile işlem yapılamaz. 
"""

# zipNesnesi bir iterator → döngü kurulabilir.
"""
for i in zipNesnesi:
    print(i)
"""

# zip nesnesi liste çevirip indexlemek
"""
zipNesnesi = list(zipNesnesi)
print(zipNesnesi)  # boş liste döner
"""
# iterator üzerinde 1 kere dönüşlebilir.

# endregion

# region örnek 4 for ile dönmek tuple almak
"""
a = "abcd"
b = [10, 20, 30, 40]

yeniZipNesnesi = zip(a, b)

for aElemani, bElemani in yeniZipNesnesi:
    print(f"aElemanindan gelen {aElemani}, bElemaninden gelen {bElemani}")
"""

# gelen iki parametreyi karşılaştırıp eşit olanları yazdıralım.

a = [1, 3, 5, 7, 2, 7, 45, 96, 12, 123, 45, 121, 12, 56]
b = [3, 5, 5, 2, 7, 7, 96, 54, 12, 122, 34, 121, 12, 34]

yeniZipNesnesi = zip(a, b)
"""
for aElemani, bElemani in yeniZipNesnesi:
    if bElemani == aElemani:
        print(aElemani, '=', bElemani)
"""
# endregion

# region ord

sozluk = {
    'A': ord('A'),
    'B': ord('B'),
    'C': ord('C'),
    'a': ord('a'),
    'b': ord('b'),
    'c': ord('c')
}
"""
print(sozluk)

for key,value in sozluk.items():
    print(key,value)
    # hatırlatma : dict sıra olmaz, bu örnekte denk geldi.
"""

# endregion

# region tuple to dict

aylarGunler = [
    ('ocak', 31),
    ('Şubat', 28),
    ('Mart', 31),
    ('Nisan', 30)
]

aylarGunlerSozluk = dict(aylarGunler)

print(aylarGunlerSozluk)

# endregion

# region örnek 5

'''
zip() ve range kullanrak haftanın günlerini bir dictionary içinde indexliyelim
1:Pazartesi
2:Salı...
'''

gunler = ['Pazartesi', 'Salı', 'Çarşamba',
          'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
sira = [1, 2, 3, 4, 5, 6, 7]

gunlerSirasi = zip(sira, gunler)

gunlerSozlugu = dict(gunlerSirasi)
print(gunlerSozlugu)

# endregion

# region

isimler = ["Ahmet", "Mehmet", "İrem", "Meryem"]
soyİsimler = ["Kancalı", "Fiyakalı", "NUr", "Su"]
yaslar = [23, 12, 45, 34]
yasSozlugu = dict()
for isim, soyisim, yas in zip(isimler, soyİsimler, yaslar):

    yasSozlugu[(isim, soyisim)] = yas

# print(yasSozlugu)

# endregion

# region lambda

gitarlar = ('ESP', 'LTD', 'Gibson', 'Fender', 'Ibanez')
# harf sayısına göre sıralayalım


def sirala(e):
    return len(e)

# sorted() yeni bir liste yaratır.
#print(sorted(gitarlar, key=sirala))

a = sorted(gitarlar, key= lambda x:len(x))
#print(a)

gitarListesi = list(gitarlar)
gitarListesi.sort(key = lambda x: len(x))
#print(gitarListesi)

# endregion