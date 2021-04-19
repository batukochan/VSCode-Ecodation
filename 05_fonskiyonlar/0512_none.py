#print(None)
"""
def ciftMi(n):
    if n % 2 == 0:
        return True

print(ciftMi(7))
"""

"""
    if s1>s2:
        return s1-s2
    elif s2>s1:
        return s2+s1
    else:
        return f"{s1}={s2}"
s1>s2 ise çıkarma
s1<s2 ise toplama
s1=s2 ise işitlik
"""
"""
def sonuc():
    s1= int(input("sayı1: "))
    s2= int(input("sayı2: "))
    if s1>s2:
        return s1-s2
    elif s2>s1:
        return s2+s1
    else:
        return f"{s1}={s2}"
print(sonuc())
"""

"""
def birlestir(a,b):
    return f"{a.title()} {b.title()}"

ad= input("İsim: ")
soyad= input("Soyisim: ")
print(birlestir(ad,soyad))
"""

"""
yazıTura()
 yazıTura()
. random değere göre → 'yazı' - 'tura' return edeceğiz
. while True içinde sonsuz döngü için de yazı için 'y', tura için 't', çıkmak için 'ç'
. 5 kez kazanan oyunu bitirir.
. her döngü de skor ekrana yazılacak

"""

"""
import random

def yaziTura():
    if random.randint(1,2) == 1 :
        return 'yazı'
    else:
        return 'tura'

def skorYaz():
    print(f'''
    Skorunuz : {skor}
    Pc Skoru : {pcSkor}
    '''
    )

skor, pcSkor=3,0
while True:
    skorYaz()
    if skor == 5 or pcSkor ==5:
        print("Oyun bitti")
        if skor>pcSkor:
            print("Kazandınız")
        else:
            print("BEN KAZANDIM")
        break
    tahmin= input("yazı için 'y', tura için 't', çıkmak için 'ç'")
    if tahmin.lower() == 'ç' :
        break
    if tahmin.lower() == 'y' :
        if yaziTura() is 'yazı':
            skor += 1
        else:
            pcSkor += 1
    elif tahmin.lower() == 't' :
        if yaziTura() is 'tura':
            skor += 1
        else:
            pcSkor += 1
    else:
        print("Lütfen 'yazı','tura' ya da 'ç' giriniz...")
"""