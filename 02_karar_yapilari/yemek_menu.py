#region restorant
'''
print("""
1-Adana Kebap    27.5   TL
2-Beyti Kebap    27.5   TL
3-Salata         12     TL
4-Çorba          7.5    TL
5-İçecek         8      TL
6-Ödeme sayfası 
""")
a1,a2,a3,a4,a5="Adana Kebap","Beyti Kebap","Salata","Çorba","İçecek"
alinanUrun=""
secim,toplam=0,0
while secim!=6:
    secim=int(input("Sipariş etmek istediğiniz ürünleri seçiniz : "))
    if secim==1:
        toplam+=27.5
        alinanUrun+=a1+","
        print("Şuanki hesap",toplam,"TL")
    elif secim==2:
        toplam+=27.5
        alinanUrun+=a2+","
        print("Şuanki hesap",toplam,"TL")
    elif secim==3:
        toplam+=12
        alinanUrun+=a3+","
        print("Şuanki hesap",toplam,"TL")
    elif secim==4:
        toplam+=7.5
        alinanUrun+=a4+","
        print("Şuanki hesap",toplam,"TL")
    elif secim==5:
        toplam+=8
        alinanUrun+=a5+","
        print("Şuanki hesap",toplam,"TL")
    elif secim==6:
        print("Hesabınız tamamlandı.")
    else:
        print("1-6 arasında seçim yapınız")
print(f"""
Toplam Hesap : {toplam} TL
Alınan Ürünler : {alinanUrun} AFİYET OLSUN
""")
'''
#endregion