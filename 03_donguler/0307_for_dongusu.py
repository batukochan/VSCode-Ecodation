'''
while döngüsünden farkı adım sayısının ne kadar döneceği bellidir.
'''
# region for döngüsü
"""
for i in range(10):
    print(i)
"""
# endregion

# region range
"""
sayiDizisi=list(range(10))
print(sayiDizisi)
sayiDizisi=list(range(9,-1,-1))
print(sayiDizisi)
sayiDizisi=list(range(15,5,-2))
print(sayiDizisi)
'''
default başlangıç 0 
default artış 1
iki argüman girirsek başlangıç ve bitiş yazılır artış miktarı yazmazsak
artış +1 kabul edilir. Alçalma istiyorsak artış miktarını değiştirmeliyiz.
'''
"""
# endregion

# region
"""
for i in range(1,11):
    if i!=5:
        print(f"{i}. öğrenci")
"""
# endregion

# region iç içe for
"""
for i in range(1,6):
    for j in range(1,6):
        print(" * ",end="")
    print()
"""
# endregion

# region
"""
for i in range(1,6):
    for j in range(1,6):
        print(f"[{i:^2}x{j:^2}= {(i*j):^3}]",end=" ")
    print()
"""
# endregion

# region örnek2
"""
a = int(input("Lütfen bir sayı giriniz:\nSayı: "))
for i in range(1, a+1):
    if a % i == 0:
        print(f"{a} sayısı, {i} sayısına tam bölünür")
"""
# endregion

# region

"""
a=int(input("lsg:""))
say=0
for i in range(1,a+1):
    if a%i==0:
        say+=1
if a%say==0:
    print("sayı TAU sayısıdır.")
else:
    print("TAU değildir.")    
"""
# endregion

# region
'''
mükemmel sayı
    Mükemmel sayı, sayılar teorisinde, kendisi hariç pozitif 
tam bölenlerinin toplamı kendisine eşit olan sayı. Diğer bir 
ifadeyle, bir mükemmel sayı, bütün pozitif tam bölenlerinin 
toplamının yarısına eşittir.
'''
"""
Pozitif tam bölenleri bul
bu değerleri topla sayının kendisiyle karşılaştır.
karşılaştırma sonucu doğruysa → Mükemmel sayı
karşılaştırma sonucu doğru değilse → Mükemmel sayı değil
"""
a = int(input("lütfen sayı girin: "))
toplam = 0
for i in range(1, a):
    if a % i == 0:
        toplam += i
if toplam == a:
    print(f"{a} sayısı, mükemmel sayıdır.")
else:
    print(f"{a} sayısı, mükemmel sayı değildir.")

# endregion

# region

'''
obeb 
ortak bölenler
'''
"""
s1=int(input("lütfen sayı giriniz: "))
s2=int(input("Lütfen sayı giriniz: "))
for i in range(1,min(s1,s2)+1): #güzel
    if s1%i==0 and s2%i==0:
        obeb=i
print(obeb)
"""

# endregion
