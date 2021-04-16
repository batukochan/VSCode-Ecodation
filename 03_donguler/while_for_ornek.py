adet = input('''
İsteenilen ürün adedi: ''')
urunListesi = []
if adet.isdigit():
    adet = int(adet)
    for i in range(1,adet+1):
        urun = input('''
İstenilen ürün : ''')
        if urun.isalpha() and urun not in urunListesi:
            urun = str(urun)
            urunListesi.append(urun)
            print(f'''
{i}. Ürününüz "{urun}"kaydedildi. 
''')
        else:
            print("Lütfen metinsel değer ya da önceden girilmemiş bir ürün giriniz...")
    print("İstenilen ürünler → ",urunListesi)
else:
    print("Lütfen sayısal bir değer giriniz...")
    