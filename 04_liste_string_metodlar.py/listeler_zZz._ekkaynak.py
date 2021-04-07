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