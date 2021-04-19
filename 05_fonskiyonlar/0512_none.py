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

def birlestir(a,b):
    return f"{a.title()} {b.title()}"

ad= input("İsim: ")
soyad= input("Soyisim: ")
print(birlestir(ad,soyad))

