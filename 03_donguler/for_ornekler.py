#region
'''
1 1 2 3 5 8 13 21 34 55 89
'''
"""
a,b=1,1
fibonacci=[a,b]
for i in range(20):
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)
"""
#endregion

#region mükemmel sayı
"""
kullanicidenAlinanSayi=int(input("Lütfen bir sayı giriniz: "))
toplam=0
for i in range(1,kullanicidenAlinanSayi):
    if kullanicidenAlinanSayi%i==0:
        toplam+=i
if kullanicidenAlinanSayi==toplam:
    print("sayı müko")
"""
#endregion

#region armstrong sayısı
"""
sayi = input("Sayı:")
üs = len(sayi)
sayi = int(sayi)
basamak,toplam=0,0
bölümdenSonraKalanSayi = sayi
while (bölümdenSonraKalanSayi > 0):
    basamak = bölümdenSonraKalanSayi % 10
    toplam += basamak**üs
    bölümdenSonraKalanSayi //= 10
if (toplam == sayi):
    print(sayi,"bir armstrong sayısıdır.")
else:
    print(sayi,"bir armstrong sayısı değildir.")
"""
#endregion

#region çarpım tablosu
"""
for i in range(1,11):
    for j in range(1,11):
        print(f"{i:^2}x{j:^2}={(i*j):^3}",end="|||")
    print()
"""
#endregion

#region infinite
"""
toplam=0
while True:
    sayi=input("Lütfen bir sayı giriniz: ")
    if (sayi == "q") :
        break
    sayi=int(sayi)
    toplam+=sayi
print(f"Girilen sayıların toplamı {toplam}")
"""
#endregion

#region list
"""
liste=[]
for i in range(1,100):
    if i%3==0:
        liste.append(i)
print(liste)
"""
"""
liste=[]
for i in range(1,100):
    if i%3!=0:
        continue
    else:
        liste.append(i)
print(liste)
"""
#endregion

#region
"""
liste=[]
for i in range(1,101):
    if i%2==0:
        liste.append(i)
print(liste)
"""
#endregion

"""
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d " %(count))
"""
"""
# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
"""
"""
sayi=int(input("Sayı gir geri bas: "))
sayac=0
for i in range(2,sayi):
    if sayi%i==0:
        sayac+=1
        break
if sayac!=0:
    print("asal değil")
else:
    print("asal sayı")
"""
"""
sayi=int(input("lsg: "))
i,a=2,0
while i<sayi:
    if sayi%i==0:
        a+=1
        break
    i+=1
if a!=0:
    print("asal değil")
else:
    print("asal")
"""
"""
kullaniciAdi,sifre="memed","mehmut"
hak=3
for i in range(hak,0,-1):
    a=input("kullanıcı adı:")
    b=input("şifre:")
    if kullaniciAdi==a and sifre==b:
        print(f"Merhaba {a}, sitemize hoş geldin!!")
        break
    else:
        print("kullanıcı adı ya da şifrenizi yanlış girdiniz.")
        print(f"Kalan giriş hakkı {i-1}")
"""
"""
for sayi in range(1,4,1):
    kadi=input("kadi: ")
    sifre=input("sifre: ")
    if kadi=="samsun" and sifre=="55":
        print("{} kerede doğru giriş yaptınız.".format(sayi))
        break
    if sayi==3:
        print("{} kere parolanızı yanlış girdiniz.".format(sayi))
        print("giriş hakkın kalmadı")
"""
"""
hafta=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
for i in hafta:
    if i=="Perşembe":
        continue
    print(i)
"""
"""
for i in range(1,11):
    for j in range(1,11):
        print(f"{i:^2}x{j:^2}={i*j:^3}",end="||")
    print()
"""
""" 
a=int(input("Dikdörtgenin kısa kenarını gir: "))
b=int(input("Dikdörtgenin uzun kenarını gir: "))
if a>b:
    print("doğru gir lan yavşak")
    a=int(input("Dikdörtgenin kısa kenarını gir: "))
    b=int(input("Dikdörtgenin uzun kenarını gir: "))
else:
    pass
for i in range(1,b+1):
    for j in range(1,a+1):
        if i==1 or i==b:
            print("*",end="")
        elif j==1 or j==a:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
"""
'''
*
* *
* * *
* * * *
'''
"""
for i in range(1,5):
    print("* "*i)
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""


'''
*****
****
***
**
*
'''
"""
for i in range(6,0,-1):
    print("*"*i)
"""
"""
for i in range(1,6):
    for j in range(1,7-i):
        print("*",end="")
    print()
"""
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""

#region for
"""
y=0
for x in range(1,11):
    y+=x
print(y,end=" ")

"""
'''
a=int(input("Lütfen bir sayı giriniz: "))
eb=a
ek=a
if a==0:
    print("program kapatıldı.")
else:
    for i in range(2,11):
        a=int(input("Lütfen bir sayı giriniz: "))
        if a==0:
            print("...program kapatılıyor...")
            break
        elif a>eb:
            eb=a
        elif a<ek and a!=0:
            ek=a
    print(f"""
en büyük sayı {eb}
en küçük sayı {ek}
""")
'''
#endregion

#region örnekler
'''
girilecekSayi=int(input("Lütfen girilecek sayı adedini belirleyiniz: "))
tekSayiAdedi,ciftSayiAdedi=0,0
ciftToplam,tekToplam=0,0
for i in range(girilecekSayi):
    a=int(input("Lütfen bir sayı giriniz: "))
    if a%2==0:
        ciftSayiAdedi+=1
        ciftToplam+=a
    else:
        tekSayiAdedi+=1
        tekToplam+=a
if ciftSayiAdedi!=0:
    print(f"""
girilen {ciftSayiAdedi} adet çift sayının ortalaması: {round((ciftToplam/ciftSayiAdedi),2)}
""")
if tekSayiAdedi!=0:
    print(f"""
girilen {tekSayiAdedi} adet tek sayının ortalaması: {round((tekToplam/tekSayiAdedi),2)}
""")
'''
#endregion

#region continue kullanımı 

'''
program döngünün başına döner ve bir sonraki yinelemeyle devam eder.
'''
'''
hafta=['pazartesi','salı','çarşamba','preşembe','cuma','cumartesi','pazar']
for i in hafta:
    if i == 'cuma':
        continue
    print(i)
'''
#endregion

#region içiçe for 
"""
for i in range(1,11):
    for j in range(1,11):
        print(f"{i:^2}*{j:^2}={(i*j):^3}",end="||")
    print()
"""
'''
genişliği ve yüksekliğini kullanıcıdan aldığımız içi boş dikdörtgen çizimi
'''
"""
a=int(input("Kenar uzunluğu veriniz: ")) #4
b=int(input("Kenar uzunluğu veriniz: ")) #6
for i in range(1,a+1):
    for j in range(1,b+1):
        if i == 1 or i == a:
            print("*",end="")
        elif j == 1 or j == b:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
******
*    *
*    *
******    
'''
"""
"""
for i in range(1,11,2):
    print(f"{('*'*i ):^9}")

for i in range(7,0,-2):
    print(f"{('*'*i ):^9}")
"""
"""
for i in range(1,10):    
    for j in range(i,9):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
        print(" ",end="")
    print()
         
"""