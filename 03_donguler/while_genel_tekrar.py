#region while döngüsü
"""
while True:
    print("buradayım")
    #sonsuz döngü
"""
"""
for i in range(5):
    print(f"{i+1} - buradayım")
"""
#bailangıç
#bitiş
#artış miktarı
"""
i=0
while i<3:
    i += 1
    print("Süper Hızlı")
"""
#endregion

#region örnek 1
"""
i=1
while i<= 10:
    print(i,"Öğrenci", sep=".")
    i += 1
print("Listede başka öğrenci bulunmamaktadır.")
"""
#endregion

#region örnek 2
"""
i=int(input("Öğrenci sayısını giriniz : "))
while i>0:
    print(i,"Öğrenci",sep=".")
    i -= 1
print("başka öğrenci bulunmamaktadır.")
"""
#endregion

#region örnek 3
#50-75
"""
i=50
while i<=75:
    print(i,end=" ")
    i += 1
"""
#endregion

#region örnek 4
"""
döngü içinde kullanıcıdan 3 adet sayı girilmesi istenir
Ekrana doğru formatta çıktı verilerek, sayıların toplamı yazılır.
çıktı
girilen .... adet sayının toplamı ...


j=1
toplam=0
while j<=3:
    i=int(input("Lütfen {}. sayıyı giriniz : ".format(j)))
    j= j+1
    toplam+=i
    
print(f"Girilen {j-1} adet sayının toplamı {toplam}")
"""
#endregion

#region örnek 5


"""
j=1
toplam=0
while j>=1:
    i=int(input("Lütfen {}. sayıyı giriniz : ".format(j)))
    j= j+1
    toplam+=i
    
print(f"Girilen {j-1} adet sayının toplamı {toplam}")
"""
#endregion

#region örnek 6
#kullanıcılar toplanacak sayıları girer 
#girdiği tüm değerleri toplamak için ekrana 0 yazdırır 
#çıktı ; girilen ... sayının toplamı ...
"""
toplam, say = 0 , 0
while True:
    i=int(input("Lütfen bir sayı giriniz : "))
    if i!=0:
        say += 1
        toplam+=i
    else:
        break
print("SGirilen {} adet sayının toplamı : {}".format(say,toplam))
"""

#endregion

#region örnek 7
"""
i=0
deger=""
while i<10:
    i+=1
    deger+="* "
print(deger)
"""

#endregion

#region örnek 8
"""
i,j=0,0
deger=""
while i<4:
    i+=1
    while j<i:
        j+=1
        deger+="* "
    print(deger)
    j=0
    deger=""
   
"""
#endregion

#region örnek 8
"""
toplam=0
sayi=1
while sayi!=0:
    sayi=int(input("lütfen bir sayı giriniz : "))
    toplam+=sayi
print(toplam)
 """
 #endregion   

#region örnek 9
'''
secim=1
toplam=0
while secim!=0:
    print("-"*75)
    a=int(input("Lütfen sayı giriniz : "))
    b=int(input("Lütfen sayı giriniz : "))
    toplam=a+b
    print("-"*75)
    print("Girilen sayıların toplamı",toplam)
    print("-"*75)
    secim=int(input("Bitirmek için 0 , devam için 1 yazdırın : "))
    if secim==1 or secim==0:
        pass
    else:
        print("""
Hatlı Seçim
Devam etmek için 1
Programı sonlandırmak için 0
        """)
        secim=int(input("Bitirmek için 0 , devam için 1 yazdırın : "))

print("-"*75)
print("""       
            Program Sonlandı
Bizi tercih ettiğiniz için teşekkür ederiz...
""")
print("-"*75)
'''
#endregion

#region örnek 10
"""
a=int(input("Lütfen bir sayı giriniz : "))
toplam,i=0,0
while i<=a:
    toplam+=i
    i+=1
print(f"0'dan {a} sayısına kadar olan sayıların toplamı : {toplam}")
"""   
#endregion

#region örnek 11
#sayı girecek faktoriyelini hesaplayacak
"""
a=int(input("Lütfen bir sayı giriniz : "))
i=1
fak=1
while i<=a:
    fak*=i
    i+=1
print(f"{a}! = {fak}")
"""
#endregion

#region While içinde if
"""
i=1
while i<=10:
    print(i,end="-")
    if i==5:
        break
    i+=1
"""
#endregion

#region if içinde while

'''
secim=input("Tek mi çift mi ?(T,t/Ç,ç) : ")
i=0 
if secim.lower()=="ç":
    while i<=20:
        print(i,end=" ")
        i+=2
elif secim.lower()=="t":
    while i<=19:
        print(i+1,end=" ")
        i+=2
else:
    print("""
Tek sayılar için -> T/t
Çift sayılar için -> Ç/ç
""")
'''
#endregion    

#region Fibonacci serisi

"""
deger=int(input("Febonacci serisi kaç adım devam etsin : "))
i,a,b=0,1,0
while i<=deger:
    c=a+b
    a,b=b,c
    print(c,end=" ")
    i+=1
"""
#endregion