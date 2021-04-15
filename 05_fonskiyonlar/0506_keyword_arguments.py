#region sıralı argümanlar
"""
def hastaKart(ad,soyad):
    print(f"Sağlıklı günler dileriz {ad} {soyad}")

hastaKart("mehmet","ali")
hastaKart(soyad="ali",ad="mehemt")
"""
#endregion

#region 
"""
def urunSatistaMi(urunKodu,urunAdi,fiyat,satistaMi):
    if satistaMi is True:
        print(f'''
        Ürün Kodu: {urunKodu} 
        Ürün adı: {urunAdi}
        Ürün satışta, mağazamızdan satın alabilirsiniz.
        fiyat:  {fiyat}
        ''')
    else:
        print("Ürün satışa kapalı")

urunSatistaMi("010231","Apple Macbook Pro","14.999",True)
urunSatistaMi(satistaMi=False,urunAdi="Apple Macbook Pro",urunKodu="020201",fiyat="14.999")
"""
#endregion
