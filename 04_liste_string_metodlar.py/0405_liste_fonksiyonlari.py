#region min max
"""
listeRakamlar = [2,5,6,1,9,7,5]
print(f"listenin en küçük değeri : {min(listeRakamlar)}")
print(min(3,9))
"ahmet","mehmet","deniz","derya","ada"
"""
#endregion

#region
'''
ogrenciListesi = []
while True:
    eklenecekOgrenci = input("""
    Listeye girecek öğrenci adı, çıkmak için -1
    Öğrenci Adı:
    """)
    if eklenecekOgrenci == "-1":
        print("program sonlandırılıyor...")
        break
    if eklenecekOgrenci != -1:
        ogrenciListesi.append(eklenecekOgrenci)
        continue
print("oluşturulan öğrenci listesi ->",ogrenciListesi)
'''
#endregion

#region isdigit 
"""
ogrenciListe = []
print('''

[1] ekle
[2] sil
[3] listele
[4] çık

''')
while True:
    secim = input("Seçiminiz: \t")
    if secim.isdigit() is True:
        secim = int(secim)
        if secim == 4:
            print('''
            Program sonlandırılıyor...
            ''')
            break
        elif secim == 1:
            eklenecek = input('''
            eklemek istediğiniz öğrencinin ismini giriniz.
            Öğrenci Adı: ''')
            ogrenciListe.append(eklenecek)
        elif secim == 2:
            silinecek = input('''
            Silmek istediğiniz öğrencinin adını giriniz.
            Öğrenci adı: ''')
            ogrenciListe.remove(silinecek)

        elif secim == 3:
            for i in ogrenciListe:
                print(f"Öğrenci Adı: {i}")

        else:
            print("Yanlış değer girdiniz.")
    else:
        print("Lütfen rakam giriniz...")
"""
#endregion

#region örnek - benzer
'''
isim-soyisim-vize-final
not ortalamalarına göre sıralama
'''
"""
ortalamalar = []
while True:
    ogrenciİsimSoyisim = input('''
    Lütfen isminizi ve soyisminizi giriniz, çıkmak için -1...
    [İsim Soyisim] : ''')
    if ogrenciİsimSoyisim == "-1":
        print('''
        Program sonlandırıldı...
        ''')
        break
    vize = int(input('''
    Vize Notunuz: '''))    
    final = int(input('''
    Final Notunuz: '''))
    ort = (vize+final)/2
    ortalamalar.append(ort)
for i in ortalamalar:
    print(i)
mini,maxi=999999999,0
for j in ortalamalar:
    if j>maxi:
        maxi=j
    if j<mini:
        mini=j
print(f"en düşük not {mini}, en yüksek not {maxi}")
"""
#endregion

#region iki bsamaklı sayıyı yazıya çevirme
"""
birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
sayi = 92
print(f"{onlar[sayi//10]} {birler[sayi%10]}")
"""
#endregion




