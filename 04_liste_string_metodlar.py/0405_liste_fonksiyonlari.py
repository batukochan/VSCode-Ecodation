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

#region sonra bak
"""
ogrenciListe = []
while True:
    secim = int(input("Seçiminiz: \t"))
    if secim == 4:
        break
    elif secim == 1:
        eklenecek = input("eklemek istediğiniz öğrencinin ismini giriniz.")
        ogrenciListe.append(eklenecek)
        

    elif secim == 2:
        silinecek = input("Silmek istediğiniz öğrencinin adını giriniz.")
        ogrenciListe.remove(silinecek)

    elif secim == 3:
        for i in ogrenciListe:
            print(f"Öğrenci Adı: {i}")

    else:
        print("Yanlış değer girdiniz.")
"""
#endregion