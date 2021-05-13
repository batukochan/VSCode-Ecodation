# region işlemler
'''
open()
    →r:read
    →a:append
    →w:write
    →x:crate
'''
# endregion

# region

# region
"""
file = open('C:\\Users\\batuh\\Downloads\\sozcukler.txt', 'r+')
for index,line in enumerate(file):
    if index <= 20:
        kelime = line.split()
        print(kelime)
    else:
        break
"""
# endregion

# region
"""
file = open('C:\\Users\\batuh\\Downloads\\sozcukler.txt', 'r+')

for satir in file:
    kelime = satir.split()
    sozcuk = kelime[0]
    if len(sozcuk) >= 10:
        print(sozcuk)
"""
# endregion

# region içinde sesli harf olmayan kelimler


def sesliHarfVarMi(sozcuk):
    sesliHarf = ['a', 'e', 'i', 'o', 'u']
    sayac = 0
    for i in sesliHarf:
        if i in sozcuk:
            sayac += 1
            if sayac > 0:
                return True
            else:
                return False


"""
file = open('C:\\Users\\batuh\\Downloads\\sozcukler.txt', 'r+')
sesliHarf = ['a', 'e', 'i', 'o', 'u']
tekrarsiz = []
for satir in file:
    kelime = satir.split()
    sozcuk = kelime[0]
    if sesliHarfVarMi(sozcuk):
        continue 
    else:
        print(sozcuk)
"""
# endregion

# region yasak harf fonksiyonu


def yasakHarfVarMi(metin, yasakHarf):
    for i in metin:
        if i in yasakHarf:
            return True  # yasak harf var
    else:
        return False  # yasak harf yok


"""
metin = "Ben bir yazılım geliştiricisi olmak istiyorum."
yasakHarf = "ç"
varMi = yasakHarfVarMi(metin,yasakHarf)
print(varMi)
"""

# endregion

# region 

def sadeceSunlariKullanir(metin, harfler):
    for harf in metin:
        if harf.isalpha() and not harf in harfler: 
            return False
    else:
        return True
"""
metin = 'okyanus ordusu'
harfler = 'okyanusrd' #sadece bu harfleri barındırır
a = sadeceSunlariKullanir(metin,harfler)
print(a)
print(set(metin))
"""
# endregion

# region


def loremBuHarfleriMiKullanir(harler):
    file = open('C:\\Users\\batuh\\Downloads\\sozcukler.txt')

    for satir in file:
        kelime = satir.split()
        sozcuk = kelime[0]
        if sadeceSunlariKullanir(sozcuk,harfler):
            print(kelime)

    
harfler = 'ens'
a = loremBuHarfleriMiKullanir(harfler)
print(a)