#region yaş fonksiyonu
"""
def yas(yas):
    print(f"Yaşınız: {2021-yas}")

yas(1998) #fonksiyonda kaç argüman varsa o kadar değişken ekleyebiliriz.
#endregion
"""
#region 
"""
def hataKodu100():
    print("sadece sayısal değer girin")
def hataKodu200():
    print("sadece pozitif değer girin")
    

yas = input("lütfen yaşınızı giriniz : ")
if yas.lstrip("-").isdigit():
    yas = int(yas)
    if yas<0 :
        hataKodu200()
    else:
        print(f"Yaşınız {yas}")
else:
    hataKodu100()

"""

#endregion

#region
"""
def selamla(arkadas):

    import datetime
    saat = datetime.datetime.now().hour
    if saat < 12:
        print(f"Günaydın {arkadas}")
    else:
        print(f"Merhaba {arkadas}")
    
selamla(input("Karşıdan gelen arkadaşınız: "))
"""
#endregion
