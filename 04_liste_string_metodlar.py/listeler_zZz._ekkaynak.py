#region 
"""
isimListesi = []

while True:
    isim = input("Lütfen listeye isim ekleyiniz: ")
    if isim in isimListesi:
        print("Farklı bir isim giriniz.")
        continue
    if isim not in isimListesi:
        isimListesi.append(isim)
        if int(len(isimListesi)) == 5:
            break
print(isimListesi)
"""
#endregion

#region kitap ekle
'''
[1] [    Kitap ekle    ]
[2] [ Kitapları Listele]
[3] [       Çıkış      ]
menüdeki işlemleri yapan program
'''
"""
print('''
    [1] [    Kitap ekle    ]
    [2] [ Kitapları Listele]
    [3] [       Çıkış      ]
''')
kitaplar = []
while True:
    islem = int(input("Menüden bir işlem seçiniz: "))
    if islem == 3:
        print("program skapatılıyor...")
        break
    elif islem == 1:
        eserAdi = str(input('''
        Eser Adı: 
        '''))
        kitaplar.append(eserAdi)
        print(f'''
        {eserAdi} isimli kitap listeye eklendi
        ''')
        continue
    elif islem == 2:
        print(f'''Okunan kitaplar = 
        {kitaplar}''')
        break
"""
#endregion

#region kitap ekle fonksiyonlarla
"""
kitaplar = []
anaMenü = '''
    [1] [    Kitap ekle    ]
    [2] [ Kitapları Listele]
    [3] [       Çıkış      ]
'''
def kitapEkle(kitap,liste):
    liste += [kitap]
    print("kitap eklendi")
    input("Ana menüye dönmek için 'Enter' tuşuna basınız.")
    return liste
def listele(liste):
    for i in liste:
        print(f"Kitap adı {i}")
    input("Ana menüye dönmek için 'enter' tuşuna basınız.")
def cik():
    exit()

while True:
    print(anaMenü)
    secim = input('''
    LÜtfen menüden bir işlem seçin
    İşlem : 
    ''')
    if secim == "1":
        eserAdi = input('''
        Lİsteye eklemek istediğiniz eseri yazınız...
        Eser adı : 
        ''')
        kitaplar = kitapEkle(eserAdi,kitaplar)
    elif secim == "2":
        listele(kitaplar)
    elif secim == "3":
        cik()
    else:
        print("hatalı seçim yaptınız...")
        input('''
        Ana menğye dönmek içim 'enter' tuşuna basınız.
        ''')
"""
#endregion

#region metot

'''pythonda bir veritipinin uğrayacağı işleme kısaca metot diyebiliriz.
bu işlem aslında o veritipinin işlenme bir metodudur.'''
"""
print(dir(list)) 
"""
'''
dir veri yapısının hangi metotlarla işlenebileceğini biz kullanıcılar 
geri döndürür.
'''
#endregion

#region çift altyazı bulunmayan metodlar
"""
for i in dir(list):
    if "__" not in i:
        print(i,end=" | ")
"""
'''append | clear | copy | count | extend | index | insert | pop | remove | reverse | sort | '''
"""
liste = [1,2,3,4,5,6]
print("liste elemanları:",liste)
liste.append(8)
print("liste elemanları:",liste)
"""
"""
liste = []

for i in range(21):
    if i % 2 == 0:
        liste.append(i)
print(liste)
"""
'''
Klavyeden kaç sayı gireceksiniz ? şeklinde çıkan mesaja cevap vererek sayıları
bir listeye gönderen, giren sayıları tek ve çift olarak ayıarak;
a.girilen sayı adedi
b.tek sayıların toplamı
c.çift sayılarıun toplamı
ayrı ayrı ekrana yazdıran program
'''
"""
liste = []
tekSayilarToplami = 0
ciftSayilarToplami = 0
sayiAdedi = int(input("Klavyeden kaç sayı gireceksiniz ?"))
for sayi in range(sayiAdedi):
    girilenSayi = int(input(f'''
    {(sayi+1)}. sayıyı girin
    {(sayi+1)}. sayı:
    '''))
    liste.append(girilenSayi)
    if liste[sayi] % 2 == 0:
        ciftSayilarToplami += liste[sayi]
    else:
        tekSayilarToplami += liste[sayi]
print(f'''
Girilen sayı adedi     : {(sayiAdedi):^5}
Tek sayıların toplamı  : {(tekSayilarToplami):^5}
Çift sayıların toplamı : {(ciftSayilarToplami):^5}
''')
"""
#endregion

#region clear metodu
'''
listedeki öğeleri silmemizi sağlar, kısacası boş liste döndürür.
'''
"""
liste = ["C++","Python","JavaScript","CSS3","HTML5"]
print("Listenin ilk hali ->",liste)
liste.clear()
print("Listenin son hali ->",liste)
"""
#endregion

#region copy metodu
'''
Bir listeyinin elemanları kopyalamamıza yarar.
'''
"""
ilkListe = ["su","maden suyu","meyve suyu"]
ikinciListe = ["hamburger","pizza","salata","biftek"]
print("ilkListe ilk hali",ilkListe)
print("ikinciListe ilk hali",ikinciListe)
ikinciListe = ilkListe.copy()
print("ilkListe son hali",ilkListe)
print("ikinciListe son hali",ikinciListe)
"""
#endregion

#region  count metodu
'''
listenin içinde, istediğimiz herhangi bir elemanın kaç adet olduğunu
bize döndürür.
'''
"""
listem = ["rock","blues","jazz","rock"]
sarkiSayisi = [123,234,12,1234]
print(listem.count("rock"))
print(sarkiSayisi.count(22))
"""
#endregion

#region extend()
'''
listeleri genişletmek amacıyla kullanabşlşrz.Append fonksiyonundan temel farklı
for döngüsüne gerek kalmadan birden fazla elemanı listeye tek seferde ekleyebiliyor
olmamızdır.
'''
"""
listem = ["rock","blues","jazz","rock"]
print(listem)
listem.extend(["pop","dance","ragge"])
print(listem)
"""
"""
marmaraBolgesi = ["istanbul","bursa","balıkesir","kocaeli","tekirdağ",]
egeBolgesi = ["izmir","aydın","manisa","uşak"]
egeMarmaraBolgesi = []
marmaraBolgesi.extend(egeBolgesi)
print(egeMarmaraBolgesi)
egeMarmaraBolgesi.extend(marmaraBolgesi)
print(egeMarmaraBolgesi)
"""
"""
egeBolgesi = ["izmir","aydın","manisa","uşak"]
egeBolgesi2 = ["denizli","afyon","manisa","balıkesir"]
print(egeBolgesi)
print(egeBolgesi2)
egeBolgesi2 += (egeBolgesi)
print(egeBolgesi2)
"""
#endregion

#region index metodu

'''
Lİsteden bir elemana erişebilmek için index bilgisine ihtiyaç duyabiliriz.
'''
"""
yazAylari = ["Haziran","Temmuz","Ağustos"]
print("Haziran ayının index numarası",yazAylari.index("Haziran"))
print("Haziran ayının index numarası",yazAylari.index("Temmuz"))
print("Haziran ayının index numarası",yazAylari.index("Ağustos"))
"""

#endregion

#region insert metodu

'''
atadığımız index numarasına yazdığımız bir değeri ekler.
'''
"""
notlarım = ["Vize : 97","İkinci Vize : 45","Final : 67"]
print(notlarım)
notlarım.insert(1,"lab : 77")
print(notlarım)
"""

#endregion

#region pop metodu
'''
son elemanı siler
'''
"""
sayilar = [1,2,3,4,5,6]
print("ilk hal",sayilar)
print("silinen değer",sayilar.pop())
print(sayilar)
"""
'''
parametre alırsa aldığı indexteki elemanı siler.
'''
"""
sayilar = [1,2,3,4,5,6]
print("ilk hal",sayilar)
print("silinen değer",sayilar.pop(3))
print(sayilar)
"""
#endregion

#region remove()
"""
sayilar = [1,2,3,4,5,6]
print("ilk hal",sayilar)
sayilar.remove(2) #2 elemanını sildi.
print("son hal",sayilar)
listem = ["rock","blues","jazz","rock"]
listem.remove("jazz")
print(listem)
""" 
#endregion

#region reverse() sort()
"""
sayilar = [1,2,3,4,5,6]
print("ilk hal",sayilar)
sayilar.reverse()
print(sayilar)
isimler = ["rock","metal","anadolur ock","pop","r&b","rap"]
isimler.sort()
print(isimler)
"""
#endregion