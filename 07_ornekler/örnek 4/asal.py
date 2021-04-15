#region asal
'''
    Asal sayılar, sadece iki pozitif tam sayı böleni olan doğal sayılardır. 
Sadece kendisine ve 1 sayısına kalansız bölünebilen 1'den büyük pozitif tam 
sayılardır. En küçük asal sayı 2'dir.
'''
"""
def AsalMi(sayi):
    for i in range(2,sayi):
        if sayi % i == 0: 
            return False #asal değil
    return True
sayi = int(input('''
Sorugulayacağınız sayıyı giriniz...
Sayı: '''))
if AsalMi(sayi):
    print(f'''
    {sayi}, asal sayıdır.''')
else:
    print(f'''
    {sayi}, asal sayı değildir.
    ''')
"""
#endregion

#region asal çarpanlar
"""
def asalbolenler(a):
    asalcarpan =[]
    for sayi in range(1,a + 1):  #sayı değeri 1den a değerine kadar değer alır.
        if sayi > 1:  #sayı değeri 1den büyükse bloğun içine girer.
            for i in range(2,sayi):  # i değeri 2(dahil) ile sayı değeri arasında olan olan değerleri alır.
                if (sayi % i) == 0:  #sayi iye tam bölünüyorsa asal değil!
                    break  
            else:  #bölünmüyorsa asaldır ve listeye eklenir.
                asalcarpan.append(sayi) #listeye eklendi.
    for j in asalcarpan[::-1]: #j değeri asalcarpan listesindeki değerleri sırayla alır.
        if a % j !=0: #fonksiyon içindeki sayı bu değerlere bölünmezse listeden çıkartılır.
            asalcarpan.remove(j) #listeden çıktı
    print(asalcarpan)#sayının asal çarpanları veren liste bastırılır.

asalbolenler(78)
"""
#endregion
