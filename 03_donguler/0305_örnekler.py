# region örnek 1
"""
i,say=-1,0
while range(i,99):
    i+=2
    say+=i
print(say,end="\t")
"""
# endregion

# region örnek 2 çarpım
"""
a=int(input("Lütfen bir sayı giriniz: "))
i=0
while i<10:
    i+=1
    print(f"{a} x {i} = {a*(i)}")
"""
# endregion

# region örnek 3 susam
"""
print('''
açıl ..... açıl!
''')
while True :
    a=str(input("Boşluğu doldurunuz : "))
    if a.lower()=="susam":
        print("Açıl susam açıl")
        break     
    else:
        print("açamadın mı?")
"""
# endregion

# region örnek 4
"""
i=0
while i<100:
    i+=1
    if i%7==0:
        print(i,end=" ") 
"""
# endregion

# region örnek 5

"""
a=int(input("Faktoriyeli alınacak değer: "))
i,fakt=1,1
while i<a:
    i+=1
    fakt*=i
print(f"{a}! = {fakt}")
"""

# endregion

# region örnek 6
"""
i = 1
res = 1
while i <= 5:
    res *= i
    print(f"{i} sayısının faktöriyeli = {res}")
    i += 1
"""
# endregion

# region örnek 7

# sıfır girdiğinde çıkacak, ortalama
"""
a=int(input("sayı giriniz: "))
i,toplam=0,0
while a!=0:
    toplam+=a
    i+=1
    a=int(input("sayı giriniz: "))   
print(f"girilen {i} adet sayının ortalaması : {round((toplam/i),2)}")
"""
# endregion

# region örnek 8
"""
'''
100-999 arası seri ancak, hane sayısına eşit olanları ekrana yazalım
102
111
120
'''
i=100
haneToplamı=0
while i<1000:
    kalan=i%10
    birler=kalan//1
    kalan=i%100
    onlar=kalan//10
    kalan=i%1000
    yuzler=kalan//100
    hanelerT=birler+onlar+yuzler
    
    if hanelerT==3 or hanelerT==2 or hanelerT==1:
        print(f"{i} (3) haneli, haneler toplamı : {hanelerT}" )
    i+=1
"""

# endregion

# region
"""
i,j,b=2,5,-1
while 1<=i<=2:
    i-=1
    b+=1
    while 5>=j:
        print(" "*b,"*"*j)  
        j-=1
"""
"""
i, j = 0, 4
b = 0
while i<4:
    while b>0:
        print("   ", end= "")
        b -=1
    while j>0:
        print(" * ", end="")
        j -=1
    i +=1
    b = i
    j = 4-i
    print()

i,j=0,0
while i<10:
    
    while j<=i:
        print("*",end="")
        j+=1
    j=0
    i+=1
    print()

    
i,j=0,10
while i<10:
    while j>0:
        print(" * ",end="")
        j-=i
    i+=1
    print()
"""
# endregion

# region
'''
rastgele sayı üret
1-99
kullanıcı 3 kere sayı girecek
en yakın tahmin ekrana yazılacak
'''
"""
import random
a=random.randint(1,99)
tahminSayisi=3
ek=999999999999
tahmin=0
tahmin!=a
while tahmin!=a:
    tahmin=int(input("tahmininiz : "))
    tahminSayisi-=1
    fark=a-tahmin
    if a<0:
        fark*=-1
    if fark<ek:
        ek=fark
"""
# endregion