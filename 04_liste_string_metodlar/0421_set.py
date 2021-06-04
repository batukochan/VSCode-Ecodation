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


c = [7, 8, 9, 10]
a.update(c)
# print(a)

# endregion

""" QUIZ """

# region soru 1
"""
Soru 1:

Adı kume_yarat_ve_ekle olan bir fonksiyon yazın. Parametre olarak bir liste alsın.

Bu fonksiyon önce içinde aşağıdaki elemanlar olan bir Set yaratsın.

"Elma", "Armut", "Karpuz", "Çilek"

Ardından parametre olarak gelen listenin elemanlarını tek tek bu kümeye eklesin ve kümeyi geri dönsün.

İpuçları:

{}
add()
Parametre:
eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']

Sonuç:
{'Vişne', 'Elma', 'Karpuz', 'Karadut', 'Çilek', 'Kayısı', 'Armut', 'Kiraz'}
"""


def kumeYaratEkle(l1: list):

    meyvelerKumesi = {
        "Elma", "Armut", "Karpuz", "Çilek"
    }
    for eleman in l1:
        meyvelerKumesi.add(eleman)

    return meyvelerKumesi


eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']

# print(kumeYaratEkle(eklenecekler))

# endregion

# region soru 2

"""
Soru 2:

Adı kume_yarat_ve_tek_seferde_ekle olan bir fonksiyon yazın. Parametre olarak bir liste alsın.

Bu fonksiyon önce içinde aşağıdaki elemanlar olan bir Set yaratsın.

"Elma", "Armut", "Karpuz", "Çilek"

Ardından parametre olarak gelen listenin elemanlarını tek seferde bu kümeye eklesin ve kümeyi geri dönsün.

İpuçları:

set() constructor'ı
update()
Parametre:
eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']

Sonuç:
{'Vişne', 'Elma', 'Karpuz', 'Karadut', 'Çilek', 'Kayısı', 'Armut', 'Kiraz'}
"""


def kumeYaratTekSeferdeEkle(l1: list):

    meyvelerKume = set({"Elma", "Armut", "Karpuz", "Çilek"})
    l2 = l1
    meyvelerKume.update(l2)
    return meyvelerKume


eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']

# print(kumeYaratTekSeferdeEkle(eklenecekler))

# endregion

# region soru 3

"""
Soru 3:

Parametre olarak iki Set alan bir fonksiyon yazın. Adı ayni_elemenlar olsun.

Fonksiyon bu iki küme içindeki ortak elemanları (kesişim kümesini) bir liste olarak dönsün.

Bu listenin elemanları küçükten büyüğe sıralı dönsün.

İpuçları:

döngü kullanmayın
intersection()
sorted()
Parametre:
set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {20, 40, 60, 80, 90, 100}

Sonuç:
[20, 40, 60]
"""


def ayniElemanlar(s1: set, s2: set):

    ortakElemanlar = s1.intersection(s2)
    ortakElemanlar = sorted(ortakElemanlar)
    return ortakElemanlar


set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {20, 40, 60, 80, 90, 100}

# print(ayniElemanlar(set_1,set_2))

# endregion

# region soru 4
"""
Soru 4:

Parametre olarak iki Set alan bir fonksiyon yazın. Adı tum_elemanlar olsun.

Fonksiyon bu iki küme içindeki tüm elemanları (birleşim kümesi) bir liste olarak versin.

Bu listede aynı olan elemanlar sadece bir kere geçmek zorunda.

Bu liste büyükten küçüğe sıralı olmak zorunda.

İpuçları:

döngü kullanmayın
unioun()
sort()
Parametre:
set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {20, 40, 60, 80, 90, 100}

Sonuç:
[100, 90, 80, 60, 50, 40, 30, 20, 10]
"""


def tumElemanlar(s1: set, s2: set):

    tumElemanlari = s1.union(s2)
    tumElemanlari = list(tumElemanlari)
    tumElemanlari.sort(reverse=True)
    return tumElemanlari


set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {20, 40, 60, 80, 90, 100}

#print(tumElemanlar(set_1, set_2))

# endregion

# region soru 5

"""
Soru 5:

Paramere olarak iki liste bir fonksiyon yazın. Fonksiyonun adı farki_ver olsun.

Fonksiyon bu iki liste arasındaki farklı elemanları bir Set olarak dönsün.

Yani birinci listede olup ikinci listede olmayan elemanları.

İpuçları:

döngü kullanmayın
set()
difference()
Parametre:
l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_2 = [2, 4, 6, 8]

Sonuç:
{1, 3, 5, 7, 9}
"""


def farkiVer(l1: list, l2: list):

    s1 = set(l1)
    s2 = set(l2)

    farkliElemanlar = s1.difference(s2)

    return farkliElemanlar


l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_2 = [2, 4, 6, 8]

# print(farkiVer(l_1,l_2))

# endregion

# region soru 6

"""
Soru 6:

Parametre olarak iki küme alan bir fonksiyon yazın. Adı tamamen_farkli_mi olsun.

Fonksiyon bu iki küme arasında hiç ortak eleman olup olamadığını kontrol etsin:

Eğer hiç ortak eleman yoksa, şöyle dönsün -> "Bu iki Küme tamamen farklı"
Eğer en az bir elemanları ortaksa, şöyle dönsün -> "Bu iki Küme tamamen farklı değil"
Fonksiyon ayrıca parametre olarak gelen iki kümenin gerçekten Set tipinde olup olmadığını kontrol da etsin. 
Eğer herhangi biri Set tipinde değilse, "Parametreler Set tipinde değil" hatası fırlatsın.

İpuçları:

döngü kullanmayın
tamamen farklı için: isdisjoint()
isinstance()
raise Exception()
Parametre:
set_1 = {20, 10, 40, 30, 50}
set_2 = {60, 80, 70, 100, 90}
Sonuç:
'Bu iki Küme tamamen farklı'

----------------------------------------
Parametre:
set_1 = {20, 10, 40, 30, 50, 60}
set_2 = {60, 80, 70, 90, 40, 10}
Sonuç:
'Bu iki Küme tamamen faklı değil'
"""
def tamamenFarkliMi(s1: set, s2: set):
    
    if not isinstance(s1,set) or not isinstance(s2,set):
        raise Exception('Parametlerin her ikisi de set tipinde olmalı!')
    else:
        farkliMi  = s1.isdisjoint(s2)
        if farkliMi:
            return "Bu iki Küme tamamen farklı"
        else:
            return "Bu iki Küme tamamen farklı değil"
"""
set_1 = {20, 10, 40, 30, 50}
set_2 = {60, 80, 70, 100, 90}
print(tamamenFarkliMi(set_1,set_2))"""
"""
set_1 = {20, 10, 40, 30, 50, 60}
set_2 = {60, 80, 70, 90, 40, 10}
print(tamamenFarkliMi(set_1,set_2))"""
"""
set_1 = {20, 10, 40, 30, 50, 60}
set_2 = (60, 80, 70, 90, 40, 10)
print(tamamenFarkliMi(set_1,set_2))"""

# endregion

# region soru 7

"""
Soru 7:

Parametre olarak iki küme alan bir fonksiyon yazın. Adı tamamen_farkli_mi_2 olsun.

Fonksiyon bu iki küme arasında hiç ortak eleman olup olamadığını kontrol etsin:

Eğer hiç ortak eleman yoksa, şöyle dönsün -> "Bu iki Küme tamamen farklı"
Eğer en az bir elemanları ortaksa, şöyle dönsün -> "Bu iki Kümenin ortak elemanları var:"
ve ortak eleman kümesini beraber dönsün
Fonksiyon ayrıca parametre olarak gelen iki kümenin gerçekten Set tipinde olup olmadığını kontrol da etsin. 
Eğer herhangi biri Set tipinde değilse, "Parametreler Set tipinde değil" hatası fırlatsın.

İpuçları:

döngü kullanmayın
tamamen farklı için: isdisjoint()
isinstance()
raise Exception()
Parametre:
set_1 = {20, 10, 40, 30, 50}
set_2 = {60, 80, 70, 100, 90}
Sonuç:
'Bu iki Küme tamamen farklı'

----------------------------------------
Parametre:
set_1 = {20, 10, 40, 30, 50, 60}
set_2 = {60, 80, 70, 90, 40, 10}
Sonuç:
'Bu iki Kümenin ortak elemanları var: {40, 10, 60}'
"""

def tamamenFarkliMi2(s1: set, s2: set):
    
    if not isinstance(s1,set) or not isinstance(s2,set):
        raise Exception('Parametlerin her ikisi de set tipinde olmalı!')
    else:
        farkliMi  = s1.isdisjoint(s2)
        if farkliMi:
            return "Bu iki Küme tamamen farklı"
        else:
            return "Bu iki Küme tamamen farklı değil" + f"""
ortak elemanlar = {s1.intersection(s2)}"""
        
set_1 = {20, 10, 40, 30, 50, 60}
set_2 = {60, 80, 70, 90, 40, 10}
#print(tamamenFarkliMi2(set_1,set_2))

# endregion

# region soru 8
"""
Soru 8:

Parametre olarak bir küme alan bir fonksiyon yazın. Adı kopyala_ve_temizle olsun.

Fonksiyon parametre olarak gelen kümeyi boşaltsın ama değerlerini yeni bir küme olarak geri dönsün.

Yani parametre yerinde değişip boş küme olacak ama değerleri ise başka bir küme olarak geri dönecek.

İpuçları:

döngü kullanmayın
copy()
clear()
Parametre:
set1 = {'A', 'B', 'C', 'D', 'E'}

Sonuç:
fonksiyon çağırmadan önce set1: {'E', 'C', 'D', 'B', 'A'}
fonksiyon çağırdıktan sonra set1: set()
set1_kopyasi: {'D', 'B', 'E', 'A', 'C'}
"""

def kopyalaTemizle(s1:set):
    
    kopyaKume = s1.copy()
    s1.clear()
    return kopyaKume
