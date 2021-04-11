#region fonksiyonlar giriş
'''
    Proglamlarımızda belirli bir kod parçasını birden fazla yerde kullanma
durumunda olabiliriz. Bu tarz durumlarda kodlarımızı bir fomskiyon halinde 
hazırlayıp, gerekli yerlerde kullanabiliriz.
'''
'''
                            #GÖMÜLÜ FONSİYONLAR 
    Kullandığımız programlama dillerinde hali hazırda bulunan fonksiyonlar 
vardır. Sıklıkla kullanılan fonkiyonların başında print() fonksiyonu vardır.
Bu tarz fonksiyonlar programda bizim oluşturmadığımız ancak kullanabildiğimiz
gömülü fonksiyonlardır.
'''
#predefiend
'''
                            #ÖZEL FONKSİYONLAR
    Biz kullanılar tarafınfan oluşturulan fonksiyonlardır.
'''
#user-defined
#endregion

#region fonksiyon atama

'''
fonksiyonu oluştururken def ile başlarız.
def <---
daha sonra fonksiyonumuza bir isim veririz.
def yeniFonksiyon() <---
fonksiyon bloğunu : ile sonlandırırız.
def yeniFonksiyon(): <---
'''

#endregion

#region Geriye döndürülemeyen fonksiyon
"""
def fonksiyonlar():
    işlemler

fonksiyonlar()
"""
"""
def Welcome():
    print("ilk fonksiyon")

Welcome()
"""
"""
def Welcome():
    ad = input("adınız:\t")
    print("hi",ad)

Welcome()
"""
'''
    Fonksiyon içerisinde tanımlanan bir değişkeni fonksiyon dışında ramden 
silineceği için main kısmında gözükmeyecektir.
'''
"""
def Welcome():
    ad = input("adınız:\t")
    print("hi",ad)
    degisken = 15
    print('fonksiyondayız',degisken)
Welcome()
# print(degisken) hata verir
"""
""" 
def degistir():
    sayi = 100
    print("fonksiyondayız",sayi)

sayi = 50
degistir() #fonksiyona gider ve işlemleri yapar.
print("fonksiyonda değiliz",sayi)
"""
""" 
def degistir():
    global sayi #tavsiye edilmez.
    sayi = 100
    print("fonksiyondayız",sayi)

sayi = 50 #fonksiyondaki değişken global olduğu için sayi değişkeni 100 olarak alıacak.
degistir() #fonksiyona gider ve işlemleri yapar.
print("fonksiyonda değiliz",sayi)
"""
""" 
def ileriSay():
    for i in range(11):
        print(i,end=" ")
    print()


def geriSay():
    for i in range(10,-1,-1):
        print(i,end=" ")
    print()

ileriSay()
geriSay()
"""
""" 
def aylar():
    aylar = [
    "Ocak","Şubat","Mart",
    "Nisan","Mayıs","Haziran",
    "Temmuz","Ağustos","Eylül",
    "Ekim","Kasım","Aralık"
    ]
    for ay in aylar:
        print(ay,end=" | ")
    print()
aylar()
"""
#endregion

#region parametre alan değer döndürmeyen
"""
def alan(yaricap):
    sonuc = 3.14*(yaricap**2)
    print(sonuc)

alan(12)
"""
"""
def topla(sayi1,sayi2):
    sonuc = sayi1 + sayi2
    print(sonuc)

topla(12,13)
"""
"""
def karsila(ad,soyad):
    print("Hoş Geldin",ad,soyad)

ad=input("Adınız: ")
soyad=input("Soyadınız: ")
karsila(ad,soyad)
"""
""" 
def tekrarla(ad:str,tekrar:int):
    for i in range(1,tekrar+1):
        print(ad)

ad = input("Tekrar edecek sözcük veya cümleyi giriniz: ")
tekrar = int(input("Tekrar sayısını giriniz: "))
tekrarla(ad,tekrar)
"""
""" 
def Tekmiciftmi(sayi):
    if sayi % 2 == 0:
        print("çift sayı")
    else:
        print("tek sayı")

Tekmiciftmi(5)
"""
"""
def carpimTablosu(sayi):
    for i in range(1,11):
        print(f"{sayi}x{i}={(sayi*i):^3}")

carpimTablosu(8)
"""
#endregion

#region örnek
'''
    klavyeden girilen kenar sayısına göre ;
    EŞKENAR,ÇEŞİTKENAR,İKİZKENAR,ÜÇGE kurallarına aykırı
KARE, DİKDÖRTGEN, EŞKENAR DÖRTGEN, PARALEL KENAR tespitleri 
yapıp ekrana yazdıran programı yazınız. Kullanıcı programı 
sonlandırmak istemediği müddetçe program çalışacak.
çeşitkenar--->tüm kenarlar eşitse
ikiztkenar--->tüm kenarlar farklıysa
eşitkenar--->tüm kenarlar eşitse
üçgenin herhangi iki kenarının uzunluğu 3. kenardan uzun olmalıdır.
tüm kenarlar eşit dereceler 90---> kare
tüm kenarlar eşit dereceler 90 değilse ---> eşkenar dörtgen
karşılıklı kenarlar eşit dereceler 90---> dikdörtgen
karşılıklı kenarlar eşit dereceler 90-değilse --> paralel kenar
'''
"""
def hesap(sekil):
    if len(sekil)==3: #üçgen
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        if (a+b)>c and (a+c)>b and (b+c) >a: #üçgen olma şartı
            if a==b or b==c or a==c: #ikizkenar
                print('''
                İkiz kenar üçgen''')
            elif a==b and b==c and a==c:
                print('''
                Eşkenar üçgen''')
            else:
                print('''
                çeşit kenar üçgen''')
        else:
            print("Üçgen olamaz!!!")
    elif len(sekil)==4: #dörgen
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if (a+b+c)>d and (a+c+d)>b and (a+b+d)>c \
            and (b+c+d)>a:
            if a==b and a==c and a==d:
                while True:
                    dikMi = input('''
                    tüm açılar dik mi ? 
                    (E,e/H,h) : ''')
                    if dikMi.lower() == "e":
                        print("kare")
                        break
                    elif dikMi.lower() == "h":
                        print("eikenar dörtgen")
                        break
                    else:
                        print("E/e,H/h giriniz...")
            elif a==b and c==d and a!=c  or \
                a==c and b==d and a!=b or \
                a==d and b==c and a!=b:
                while True:           
                    dikMi = input('''
                    tüm açılar dik mi ? 
                    (E,e/H,h) : ''')
                    if dikMi.lower() == "e":
                        print("dikdörtgen")
                        break
                    elif dikMi.lower() == "h":
                        print("paralel kanar")
                        break
                    else:
                        print("E/e,H/h giriniz...")
            else:
                print("çeşit kenar dörtgen")
        else:
            print("dörtgen olamaz")

while True:
    kenar = int(input('''
    kenar sayısı: 
    '''))
    if kenar == 3:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        hesap([a,b,c])
    elif kenar == 4:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = int(input("d: "))
        hesap([a,b,c,d])        
       
    else:
        print('''
        Programa üçgen ya da dörtgen ifadeleri giriniz...
        ''')
    cikis = input("Programdan öıkmak için çıkış yazınız.")
    if cikis.lower()=="çıkış": 
        break
"""
#endregion

#region parametre almayan değer döndüren
"""
def topla():
    a = int(input("1.sayı : "))
    b = int(input("2.sayı : "))
    sonuc = a+b
    return sonuc

sonuc = topla()
print(sonuc)
"""
#endregion

#region parametre alan değer döndüren

'''
***return***
'''

'''
    Aldığpı kısa ve uzun kenarların değerlerine göre dikdörtgenin 
alanını hesaplayan, fonksiyon tanımlayıp çağıran program
'''
"""
def dikdortgenAlan(kKenar,uKenar):
    if uKenar >= kKenar:
        dAlan = (kKenar*uKenar)
        return kKenar*uKenar
    else:
        return "Kısa kenar uzun kenardan büyük değer alamaz"
kKenar = float(input("kısa kenarı giriniz.."))
uKenar = float(input("uzun kenarı giriniz.."))
alan = dikdortgenAlan(kKenar,uKenar)
print(alan)
"""
""" 
def topla(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

print('''
[1]---TOPLA
[2]---ÇIKAR
[3]---ÇARP
[4]---BÖL
[Q]---ÇIKIŞ
''')
while True:
    secim = input("işlem seç")
    if str(secim.lower()) == "q":
        print("Program sonlandırılıyor...")
        break
    secim=int(secim)
    a = int(input(""))
    b = int(input(""))
    if secim == 1:
        print(topla(a,b))
    elif secim == 2:
        print(cikarma(a,b))
    elif secim == 3:
        print(carpma(a,b))
    elif secim == 4:
        print(bolme(a,b))
    else:
        print("yanlış tercih")
"""
""" 
def mutlakDeger(a):
    if a<0:
        return a*-1

print(mutlakDeger(-3))
"""
#endregion

#region türkçe karakter içeriyor mu ?
"""
turkceKarakter = ["ğ","Ğ","ç","Ç","ş","Ş","ü","Ü","ö","Ö","ı","İ"]
def kontrol(kelime: str):
    for i in turkceKarakter:
        if i in kelime:
            return True

kelime = str(input('''
    Sorgulamak istediğiniz kelimeyi giriniz...
    Kelime: '''))
if kontrol(kelime):
    print(f'''
    {kelime}, türkçe karakter içeriyor''')
else:
    print(f'''
    {kelime}, türkçe karakter içermiyor''')

"""
#endregion

#region tek cift ortalama
'''
klavyeden girilen başlangıç ve bitiş aralığındaki sayıların 
çift ve tek olanların ayrı ayrı oralamasını alıp ekrena yazan
program
not: tek, çift sayı kontrollü fonksiyonb içinde yapılacaktır
'''
"""
def Tekcifttop(baslangic,bitis,artis):
    ciftToplam,tekToplam = 0,0
    tekSay,ciftSay=0,0
    for i in range(baslangic,bitis+1,artis):
        if i % 2 == 0:
            ciftToplam += i
            ciftSay += 1
        else:
            tekToplam +=i
            tekSay += 1
    return f'''
    Tek sayıların ortalaması {tekToplam/tekSay} 
    Çift sayıların ortalaması {ciftToplam/ciftSay}
    '''
print(Tekcifttop(1,100,5))
"""
#endregion

#region tam bölünen

'''
klavyeden girilen satının tam bölenlerini bulup ekrana yazdıran program
NOt: Sayının tam bölenlerini bulma işlemi klavyeden yapılacak.
'''
"""
def tambolenler(sayi):
    tambolenler = []
    for i in range(1,sayi+1):
        if sayi % i == 0:
            tambolenler.append(i)
    return tambolenler
print(tambolenler(12))
"""

#endregion

#region varsayılan değer atama
"""
def calisanlar(ad:str,soyad:str,sehir="bilgi yok",deneyim="bilgi yok"):
    print(f'''
    Kayıt yapılıyor...
    İsim: {ad}
    Soyad: {soyad}
    sehir: {sehir}
    deneyim: {deneyim}
    ''')
calisanlar("batu","koçhan")
#varsayılan değer ataması yapılacak parametreler sonda bırakılmalıdır.
"""
#endregion

#region Yerel (local) değişken

'''
    Python'da fonksiyonlarda tanımlanan değişkenler yerel değişkenlerdir.Bir fonksiyon 
bloğunda oluşturulan bir değişken varsa o değişken o fonksiyona özeldir.Yani o değişen 
fonksiyon dışında kullanılmaya kalkılırsa, program değişkeni bulamaz.Bunun sebebi program 
fonksiyondan çıktıktan sonra garbage collector tarafından o değişkeninRAM'den siliniyor 
olmasıdır.
'''
"""
sayi = 12
def fonksiyon():
    sayi = 24
    print(sayi)

fonksiyon() # 24 
print(sayi) # 12 yazdırılır çünkü fonksiyon içindeki sayi değişkeni silinir.
"""
"""
sayi = 12
def fonksiyon():
    print(sayi)

def fonksiyon2():
    print(sayi)

fonksiyon()
fonksiyon2()
print(sayi)
'''
    a değişkeni 12 atanmıştır ve her yerde kullanılmıştır. Fonksiyonlar içinde 
farklı bir değerde a değişkeni atansaydı, bir önceki örnekteki gibi bir çıktı 
alacaktık.
'''
"""
#endregion

#region Global değişken
"""
sayi = 12
def fonk():
    global sayi
    sayi = 34
    print(sayi)
fonk()
print(sayi)
'''
    fonksiyondaki sayi değeri global olduğu için diğer sayi parametresinin de adresi 
aynı oldu.Bu sebeple ikisin de değeri fonksiyonun içindeki global değişken değerine 
eşitlendi.
'''
"""
#endregion

#region Lambda
"""
topla = lambda a,b:a+b
print(topla(2,4))
"""
"""
kalan = lambda bolunen,bolen: bolunen % bolen
print( kalan(18,4))
"""
#endregion

#region taban üs son 3 basamak
"""
def hesapla(taban,us):
    sonuc = taban**us
    son = int(input("Son kaç basamak: "))
    print(str(sonuc)[-son:])
x=int(input("Taban: "))
y=int(input("üs: "))
hesapla(x,y)
"""
#endregion

#region 
'''
iki parametreli bir fon oluşturulacak
iki ifade alınacak ve bu ifadeler birleştirilecek
birleştirilen iki iadenin baş harfleri büyük olacak
örn ahmtet mehmet
    Ahmet Mehmet
'''
"""
def birlestir(st1,st2):
    return f'''
{(st1.capitalize())}-{(st2.capitalize())}
    '''

st = birlestir(input("İfade 1 : "), input("İfade 2: "))
print(st)
"""
#endregion

#region ortak karakter
"""
def degerGetir():
    d1 = input("Değer 1: ")
    d2 = input("Değer 2: ")
    return d1,d2

def kontrolEt(ifade1,ifade2):
    sayac = 0
    kontroListesi = []
    for i in ifade1:
        for j in ifade2:
            if i not in kontroListesi:
                if j == i:
                    kontroListesi.append(j)
                    sayac += 1
    print(sayac)

d1,d2= degerGetir()
kontrolEt(d1,d2)
"""
#endregion

#region ortalama
"""
def ortalama(a,b,c):
    return (a+b+c)/3

print(ortalama(1,2,3))
"""
#endregion

#region değişken uzunluğunda parametre gönderme
"""
def ortalama(*liste):
    return sum(liste)/ len(liste)

print(ortalama(1,2,3,8,1231,233,-32))
"""
#endregion

#region
"""
def karesi(*liste):
    donusLİstesi = []
    for i in liste:
        donusLİstesi.append(i**2)
    return donusLİstesi

print(karesi(2,4,8))
"""
#endregion

#region dec to bin
"""
def dectobin(arg):
    kalan , bin =0 , ""
    while arg > 1:
        kalan = arg % 2 
        arg =  arg // 2
        bin = str(kalan) + bin
    print(str(arg) + bin)

dec = int(input("Lütfen dec-bin dönüşümü için bir değer giriniz: "))
dectobin(dec)
"""
#endregion

#region rekursive fonksiyon
"""
def topla(n):
    if n<=0:
        return "Pozitif değer olmalı"
    if n<=1:
        return n
    return n + topla(n-1)

print(topla(5))
"""
#endregion