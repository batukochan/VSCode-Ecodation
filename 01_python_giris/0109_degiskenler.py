#region variable - değişkenler
"""
skor = 12
print(skor)
name = "mehmet"
print(name)
"""
#endregion

#region notation

#camelCase
"""
okulNumarasi = 1243
ad = "ahmet"
soyad = "talan"
sinavNotu = 97
print(okulNumarasi, ad, soyad, sinavNotu)
''' çıktı → 1243 ahmet talan 97 '''
"""
#Snake_case 
"""
okul_numarasi = 1234
ad = "mehmet"
soyad = "yalı"
sinav_notu = 32
print(okul_numarasi, ad, soyad, sinav_notu)
''' çıktı → 1234 mehmet yalı 32 '''
"""
#endregion

#region degisken_isimlendirme_kurallari
"""
Değişken İsimlendirme Kuralları
1- harf veya alt çizgi ile başlamalıdır
2- rakam ile başlayamaz
3- ilk harf dışındakiler, harf, sayı, alt çizgi olabilir
4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
5- case sensitive
6- anahtar kelimeler if, pass, while, def bunlar kullanılamaz
7- türkçe karakter kullanmamaya özen gösterelim
"""


#1- harf veya alt çizgi ile başlamalıdır
"""
okul = "istanbul üniv."
birinci = "izmir"
_birinci = "izmir"
"""
#2- rakam ile başlayamaz
"""
_34istanbul = "en güzel şehir"
"""
#3- ilk harf dışındakiler, harf, sayı, alt çizgi olabilir
"""
plaka34 = "istanbul"
print(plaka34)
"""
#4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
"""
plaka&34 = "ist"
"""
#5- case sensitive
"""
ad = "ali"
print(Ad)
"""

#6- anahtar kelimeler if, pass, while, def, for bunlar kullanılamaz
"""
def = "definiton"
"""
#7- türkçe karakter kullanmamaya özen gösterelim
"""
öğrenci = "Ali"
ogrenci = "ezgi"
print(ogrenci)
"""
#endregion

