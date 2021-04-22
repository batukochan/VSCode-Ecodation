"""
n = 5
f = 1
while n>0:
    f *= n
    n -= 1
print(f)
"""

"""
def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n*faktoriyel(n-1)

print(faktoriyel(5))
"""

"""
def topla(n):
    if n<=1:
        return 1
    return pow(n,n) + topla(n-1)

print(topla(5))
"""

"""
parolaUret()
10 karakterli olacak 
random
"""

"""
sayiListesi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
buyukHarf = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'İ', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
kucukHarf = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j",
             "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]

parola = ""


def parolaUret():

    global parola
    import random
    sayiUret = random.randint(1, 3)
    if sayiUret == 1:
        parola += str(random.choice(sayiListesi))
    
    elif sayiUret == 2:
        parola += random.choice(buyukHarf)

    elif sayiListesi == 3:
        parola += random.choice(kucukHarf)

for i in range(10):
    parolaUret()
print(parola)
"""


def kartBilgiVer(k):
    return f"{k['ad']} {k['soyad']} {k['para']}"


def atmBilgiVer(a):
    return f"{a['ad']},{a['para']}"


def ayniMi(k, a):
    if kart['bankaAdi'] == atm['ad']:
        return True
    else:
        return False


def paraYatir(k, a, miktar):
    k['para'] += miktar
    a['para'] += miktar
    if not ayniMi(k, a):
        k['para'] -= miktar*0.03
        a['para'] += miktar*0.03
    print(f"{miktar} para yatırıldı. Atm'de {a['para']}")


def paraCek(k, a, miktar):
    if a['para'] >= miktar:
        if k['para'] >= miktar:
            k['para'] -= miktar
            a['para'] -= miktar
            if not ayniMi(k, a):
                k['para'] -= miktar*0.03
                a['para'] += miktar*0.03
                print(f"{miktar*0.03} tl alındı.")
            print(f"{miktar} tl çekildi. Atm'de kalan para {a['para']}")

        else:
            print(f"{k['para']} çekebilirsiniz.")
        pass
    else:
        print(f"{a['para']} kadar para çekebilirsiniz.")


kart = {
    "ad": "Batuhan",
    "soyad": "Koçhan",
    "bankaAdi": "ziraat",
    "para": 1000
}

atm = {
    "ad": "halk",
    "para": 3500
}

print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraYatir(kart, atm, 1000)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraCek(kart, atm, 100)
