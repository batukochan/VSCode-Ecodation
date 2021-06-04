# region listeler

"""
    list aslında bir dizidir. List'lerde index yapısı ile içindeki 
karakterlere ulaşılabilir.
→ liste = []
"""
"""
bankalar = ['halk','ziraat','ing']
print(bankalar)
bankalar = ['kamu',['halk','ziraat']]
print(bankalar[1][1])
"""
# endregion

# region liste üzerinde gezme

evcilHayvalar = ['kedi', 'köpek', 'muhabbet kuşu', 'hamster']
"""
for i in evcilHayvalar:
    print(i,end=' ')
"""
''' Eğer listenin indexini almak istersek enumerate kullanılır.'''
"""
for index ,hayvan in enumerate(evcilHayvalar):
    print(f"{index}-{hayvan}")
"""
"""
for i,j in enumerate(evcilHayvalar):
    print(i,j,end=' ')
"""

# endregion

# region liste içinde dönerken eleman değiştirme

bilgisayarBilesenleri = [
    'monitör', 'anakart',
    'ekran kartı', 'mause'
    'ram', 'ssd', 'işlemci'
]
"""
for index, bilesen in enumerate(bilgisayarBilesenleri):
    if bilesen == bilgisayarBilesenleri[(len(bilgisayarBilesenleri)-1)]:
        bilesen = '***yeni*** ' + bilesen
    print(bilesen)
"""
# yukarıda yapılan değişim işlemi bir value kopyalamadır. Listede değşiklik  yapmaz.
"""
print(bilgisayarBilesenleri)

for index, bilesen in enumerate(bilgisayarBilesenleri):
    if bilesen == bilgisayarBilesenleri[(len(bilgisayarBilesenleri)-1)]:
        bilesen = '***yeni*** ' + bilesen
        bilgisayarBilesenleri[(len(bilgisayarBilesenleri)-1)] = bilesen

print(bilgisayarBilesenleri)
"""

# endregion

# region

adaylar = [
    'Mehmet Yağıbasan', 'Metehan Aydemir', 'Musa Dalançıkar',
    'Çağrıhan Akça', 'Burak Yıldırım', 'Batu Koçhan'
]
"""
for i, aday in enumerate(adaylar):
    aday = '30. Dönem Milletvekili adayı ' + aday + ''
    adaylar[i] = aday 
    print(aday)
"""
"""
haftaici = ['pzt','sl','çrş','perş','cuma']
haftasonu = ['cmrtsi','pzr']
hafta = haftaici + haftasonu
print(hafta)
"""
# endregion

# region slice (dilimleme)

ayakkabiNumarasi = [
    '40', '42', '44', '45'
]
"""
print(ayakkabiNumarasi[::1])
print(ayakkabiNumarasi[0:3:1])
print(ayakkabiNumarasi[0:3])
print(ayakkabiNumarasi[0:len(ayakkabiNumarasi)])
print(ayakkabiNumarasi[:])
"""

# endregion

# region liste kopyalama
yeniListe = ayakkabiNumarasi[:]
baskaListe = ayakkabiNumarasi[:]
"""
print(yeniListe)
print(baskaListe)
print('-'*45)
yeniListe[0] = '39'
baskaListe[2] = '44.5'
print(ayakkabiNumarasi)
print(yeniListe)
print(baskaListe)
"""
'''
Eğer [:] kullanmadan kopyalasaydık yapılan değişiklikler her listede aynı olurdu.
'''

# endregion

# region listelerden eleman silme

'''
yöntem 1 -> silinecek elemanın indexini bildiğimiz durum,
pop()
'''

kirtasiye = [
    'kalem', 'defter', 'silgi', 'çanta'
]
"""
silinen = kirtasiye.pop(2)
print(silinen)
print(kirtasiye)
"""
"""
kirtasiye.pop() # son elemanı siler
print(kirtasiye)
"""

'''
Silinen elemana ihtiyaç yoksa
del
'''
"""
del kirtasiye[2]
print(kirtasiye)
"""
# tek seferde birden fazla eleman silmek

dizi = [
    'a', 'b', 'c', 'd', 'e', 'f'
]
"""
del dizi[1:4]
print(dizi)
"""

# silinecek eleman biliniyorsa  (value) -> remove

dizi.remove('a')
"""
print(dizi)
"""
''' olmayan bir eleman yazılırsa valueError verir.'''

# endregion

# region listler ve stringler

isim = 'Batuhan'
"""
print(list(isim)) # ['B', 'a', 't', 'u', 'h', 'a', 'n']
"""
metin = 'Şampiyon Beşiktaş'
kelimeler = metin.split()
# print(kelimeler)
harfler = list(metin)
# print(harfler)

slogan = ['Şampiyon', 'Beşiktaş']
cümle = ' '.join(slogan)
# print(cümle)

# endregion

# region range ile liste oluşturmak

sayiAraligi = range(2, 101, 2)
ciftSayiler = list(sayiAraligi)
# print(ciftSayiler)

# endregion

# region is ifadesi

'''
a == b değer kontrolü yapar
id(a) == id(b) nesne kontrolü yapar
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(a is b)  # False
# print(id(a) == id(b))  # False
# print(a == b)  # True

k1 = 128
k2 = 128

# print(k1 is k2)  # True

''' is aslında id() kontrolüdür. '''

# endregion

# region matris operasyonları

uceUcMatris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(uceUcMatris[0])
print(uceUcMatris[0][2])  # 3

uceUcMatris2 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

toplamMatris = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(uceUcMatris)):

    for j in range(len(uceUcMatris2)):

        toplamMatris[i][j] = uceUcMatris[i][j] + uceUcMatris2[i][j]

print(toplamMatris)

# endregion
