#15yaş altına ve 65 yaş üstüne ½15 indirimli bilet satılacaktır
#üniversite öğrencisiyseniz ½10 indirimli bilet alacaksınız
#çıktı merhaba batuhan koçhan öğrenci indirimi kazandınız bilet fiyatı 25 tl, indirimli fiyat 22.5 tl
print("***Uygun Film Sitesine Hoşgeldiniz***")
kAdi=str(input("Lütfen kullanıcı adınızı giriniz : "))
yas=int(input("Lütfen yaşınızı giriniz :"))
biletFiyati=int(25)
ogrindirim= float(biletFiyati-(biletFiyati*0.1))
yasindirim= float(biletFiyati-(biletFiyati*0.15))
if yas<=15 or yas>=65 :
    print(f"Merhaba {kAdi} ½15 indirim kazandınız.\n\tÖdenecek Tutar : {yasindirim} TL\nBiletinizi satış noktalarımızdan temin edebilirsiniz...")
else:
    ogrMi=int(input("Öğrenciyseniz 1 değilseniz 0 giriniz : "))
    if ogrMi==1:
        print(f"Merhaba {kAdi} ½10 indirim kazandınız.\n\tÖdenecek Tutar : {ogrindirim} TL\nBiletinizi satış noktalarımızdan temin edebilirsiniz...")
    else:
        print("Merhaba",kAdi,"\nÖdenecek Tutar : {} TL\nBiletinizi satış noktalarımızdan temin edebilirsiniz...".format(biletFiyati))