# region soru 1

'''
Soru 1:

Aşağıdaki şekilde bir fonksiyon yazın. Adı tuple_yarat olsun.
Fonksiyonumuz önce içinde 1'den 10'a kadar değerlerin olduğu bir Tuple yaratsın.
Ardından bu Tuple'a 11'den 20'ye kadar olan sayıları eklesin ve Tuple'ın son halini dönsün.

İpuçları:

Tuple'lar Immutable'dır. O Tuple'a nasıl yeni eleman eklenir?
for döngüsü ve range() kullanın
Sonuc: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
'''


def tupleYarat():

    t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for i in range(11, 21):

        # tuple değiştirilemez
        t2 = t1 + (i,)
        t1 = t2
    return t2

# print(tupleYarat())


"""
Soru 2:

Parametre olarak verilen bir Tuple'ı String'e dönüştüren ve bu String'i geri dönen bir fonksiyon yazın.
Adı tuple_to_string olsun.
"""


def tupleToString(t1):
    sonuc = ''
    for i in t1:
        sonuc += i
    return sonuc


t = ('Y', 'a', 'p', 'a', 'y', ' ', 'Z', 'e', 'k', 'a')
# print(tupleToString(t))


def tTs(t1):
    metin = ''.join(t1)
    return metin


t1 = ('Y', 'a', 'p', 'a', 'y', ' ', 'Z', 'e', 'k', 'a')
# print(tTs(t1))

"""
Soru 3:

Parametre olarak verilen bir String'i önce List'e sonra da bu List'i Tuple'a dönnüştüren bir fonksiyon yazın.
Adı string_to_list_to_tuple olsun ve Tuple'ı geri dönsün.

İpuçları:

sadece constructor metodlarını kullanın
list()
tuple()
Parametre:
python_babasi = 'Guido van Rossum'
"""


def stringToListToTuple(st: str):

    stListe = list(st)
    tp1 = tuple(stListe)

    return tp1


metin = "Hey You!"
# print(stringToListToTuple(metin))

"""
Soru 4:

Parametre olarak bir Tuple ve bir index alan bir fonksiyon yazın.
Fonksiyon, verilen index'te yer alan elemanın tüm Tuple içinde kaç sefer yer aldığını bize dönsün. Adı kac_kere_geciyor olsun.

İpuçları:

count()
Parametreler:
t = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
i = 1

kac_kere_geciyor(t, i)

Sonuc: 4
"""


def kacAdetVar(tp1, i):

    tupleListesi = list(tp1)
    sayilacakSayi = tupleListesi[i]
    return tupleListesi.count(sayilacakSayi)


""" YA DA """


def kacAdet(tp1, i):
    eleman = tp1[i]
    return tp1.count(eleman)


t = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
i = 0

# print(kacAdetVar(t,i))
#print(kacAdet(t, i))

"""
Soru 5:

Tuple üzerinde dilimleme işlemleri daha önce String ve List'lerde gördüğümüz gibidir.

Elimizde şu şekilde bir Tuple olsun:

 tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j') 
Aşağıdaki sorulara slicing yani dilimleme ile (index bazlı) cevap veriniz:

4'cü eleman (dahil) ile 7'ci eleman (dahil) arasını bulun
İlk 5 elemanı bulun
6'cı elemandan (dahil) sonrasını bulun
Tüm elemanları bulun
Sondan 2. elemanı bulun
Son 4 elemanı bulun
2'ci elemandan başlayıp, 8'ci elemana kadar 2'şer atlayarak yazın
Tüm elemanları 3'er atlayarak yazın
9'uncu elemandan, 3'cü elemana (hariç) kadar tersten yazın
tup'u tersten yazın
tup'u tersten 2'şer atlayarak yazın
Son elemana (hariç) kadar olan tüm elemanlarını ters index ile alınız
"""

tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
"""
print(tup[3:7])
print(tup[:5])
print(tup[7:])
print(tup[::])
print(tup[-2])
print(tup[-4:])
print(tup[1:8:2])
print(tup[8:2:-1])
print(tup[::-1])
print(tup

[::-2])
print(tup[:-1])
"""

"""
Soru 6:

Parametre olarak bir liste alan bir fonksiyon yazın. Fonksiyonun adı, tuple_sonunu_degistir olsun.
Bu listenin elemanları birer Tuple olsun.
Her bir tuple farklı uzunlukta olabilir. Dolayısı ile Listenin elemanlarının uzunlukları sabit değil.
Yazacağınız fonksiyon, Liste içindeki her bir Tuple elamanının son üyesini silsin, yerine karesini yazsın.

İpuçları:

Liste yerinde değişsin, yani parametre olarak gelen orjinal liste değişsin
Tuple'ın son elemanını index ile nasıl alacağınızı düşünün
Listenin içinde for ile dönerken, döngüdeki elemanı değiştirseniz de liste değişmez.
Listeyi değiştirmenin bir yolunu bulmalısınız (enumerate())
Tuple birleştirmeye dikkat ediniz (tek elemanlı bir Tuple nasıl olur?)
Parametre:
tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]

Sonuc:
tuple_listesi = [(2,5,64), (4,9), (1,7,9,36), (25,)]
"""


def tupleSonunuDegistir(l1):

    for i, tup in enumerate(l1):
        sonEleman = pow(tup[-1], 2)
        sonElemanaKadar = tup[:-1]
        # son eleman tek eleman olduğu için tuple tipine çevirmeliyiz
        tup = sonElemanaKadar + (sonEleman,)
        l1[i] = tup


tuple_listesi = [(2, 5, 8), (4, 3), (1, 7, 9, 6), (5,)]
tupleSonunuDegistir(tuple_listesi)
# print(tuple_listesi)

"""

Soru 7:

Parametre olarak bir liste alan bir fonksiyon yazın. Fonksiyonun adı, tuple_karesi_ile_degistir olsun.
Bu listenin elemanları birer Tuple olsun.
Her bir tuple farklı uzunlukta olabilir. Dolayısı ile Listenin elemanlarının uzunlukları sabit değil.
Yazacağınız fonksiyon, Liste içindeki her bir Tuple elamanının tüm elemanlarının yerine karelerini yazsın.

Ve yeni kareli listeyi geri dönsün.

İpuçları:

Parametre olarak gelen orjinal liste değişmesin
Listenin içinde for ile dönerken, döngüdeki elemanı değiştirseniz de liste değişmez.
Parametre:
tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]

Sonuc:
yeni_tuple_listesi = [(4,25,64), (16,9), (1,49,81,36), (25,)]
"""


def tupleKaresiDegistir(l1):

    yeniListe = l1.copy()
    for i, tup in enumerate(yeniListe):
        tuple1 = tuple()
        for t in tup:
            tuple1 += (pow(t, 2),)

        yeniListe[i] = tuple1
    return yeniListe


tuple_listesi = [(2, 5, 8), (4, 3), (1, 7, 9, 6), (5,)]
# print(tupleKaresiDegistir(tuple_listesi))
"""
Soru 8:

Parametre olarak 4 liste alan bir fonksiyon yazın. Adı oyuncu_film_karakteri_yil olsun.

Gelen 4 liste şu şekilde olacak:

Liste 1 -> Oyuncunun gerçek adı
Liste 2 -> Filmin Adı
Liste 3 -> Filmin Çekildiği Yıl
Liste 4 -> Karakter Adı
Fonksiyon bu 4 listedeki, karşılıklı elemanları alacak ve 2'şer elemanlı 2 Tuple haline getirecek. Ve geriye bir Dictionary dönecek.

İlk Tuple -> (Oyuncu Adı, Karakter Adı)
İkinci Tuple -> (Film Adı, Çekim Yılı)
Bu Dictionary'nin key'leri İlk Tuple, value'ları ise İkinci Tuple olacak.

İpuçları:

zip()
Parametreler:
oyuncular = ['Marlon Brando', 'Heath Ledger', 'Natalie Portman', 'Emma Stone']
karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Queen', 'Mia']
filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La Land']
yillar = [1972, 2008, 2010, 2016]

Sonuc:
{('Marlon Brando', 'Don Vito Corleone'): ('The Godfather', 1972),
 ('Heath Ledger', 'Joker'): ('The Dark Knight', 2008),
 ('Natalie Portman', 'The Swan Queen'): ('Black Swan', 2010),
 ('Emma Stone', 'Mia'): ('La La Land', 2016)}
 """


def filmKarakteriYil(l1, l2, l3, l4):
    sozluk = dict()

    for oyuncu, karakter, film, yil in zip(l1, l2, l3, l4):

        #ikili tuple
        sozluk[(oyuncu,karakter)] = (film,yil)

    return sozluk

oyuncular = ['Marlon Brando', 'Heath Ledger', 'Natalie Portman', 'Emma Stone']
karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Queen', 'Mia']
filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La Land']
yillar = [1972, 2008, 2010, 2016]

#print(filmKarakteriYil(oyuncular, karakterler, filmler, yillar))
"""
Soru 9:

Parametre olarak bir Tuple alan bir fonksiyon yazın. Adı tuple_sirala olsun.

Parametre olarak gelen Tuple, içinde Tuple'lar tutan bir yapı olsun. Yani elemanlar da Tuple olsun. Ve bu elemanlardan herbiri 2 elemanlı bir Tuple olacak.

Fonksiyon, parametre olarak gelen Tuple'i sıralayacak ve sıralı bir Tuple dönecek.

Sıralama kuralı, 2. eleman olacak. Yani içerideki Tuple'ların 2. elemanına bakıp ona göre sıralayacak.

İpuçları:

lambda fonksiyon kullanınız
Parametre:
tuple_of_tuples = (('a', 12), ('e', 8), ('b', 16), ('c', 22))

Sonuc:
[('e', 8), ('a', 12), ('b', 16), ('c', 22)]
"""

def tupleSirala(t1):

    return sorted(t1, key = lambda x: x[1])

tuple_of_tuples = (('a', 12), ('e', 8), ('b', 16), ('c', 22))
#print(tupleSirala(tuple_of_tuples))