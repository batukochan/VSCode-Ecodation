#region değişken kavramı

hastaAdi = input("Lütfen adınızı ve soyadınızı giriniz : ")

kg = int(input("Lütfen kilonuzu giriniz : "))

boy = float(input('''
Lütfen boyunuzu metre cinsinden giriniz, ör. '1.84'
Boyunuz:
'''))

vki=kg/(boy**2)

print(f'''
Hastanız {hastaAdi}
Kilosu {kg} kg
Boyu {boy} mt.
Girilen bilgilere göre vücut kitle indeksi : {round(vki,2)}
''')

#endregion

#region atama_operatoru
"""
name = "Jhon"
print(name)
"""
#endregion

#region round
"""
s = 1.838983121212
print(round(s, 3))

kg = 80
mt = 1.60
vki = kg/mt**2
print(round(vki, 2))
"""
#endregion

#region sonucu_yine_kendi_degerine_atama
"""
i = 1
print(i)
i = i + 1
print(i)
sayi = 10
sayi = sayi - 1
sayi = sayi * 2
x=10
x = x + 1
print(sayi)
print(x)
"""
#endregion

#region az_sayida_degisken_kullanma
"""
sayi = 5
toplam = 0
toplam = toplam + sayi
sayi = 10
sayi = sayi + 1
toplam = toplam + sayi
"""
#endregion


print(round(123.243426325)) # sayıyı yuvarlar.
# çıktımız → 123
print(round(123.243426325,3)) # virgülden sonra 3 haneyi  alır
# çıktımız → 123.243
print(round(123.243426325,2)) # virgülden sonra 2 haneyi  alır
# çıktımız → 123.24
