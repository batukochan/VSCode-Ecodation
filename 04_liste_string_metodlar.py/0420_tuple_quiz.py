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
