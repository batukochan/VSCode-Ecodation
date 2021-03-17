#region break-point
"""
kAdi = input('Kullanici Adi Giriniz: ')
print("a")
if kAdi!= "admin":
    print(f"{kAdi} yetkisi ile admin paneline giremezsiniz...")
    print("b")
print("c")
"""
"""
sinavNot=int(input("sınav notunuzu giriniz : "))
sinavNot2=int(input("sınav notunuzu giriniz : "))
sinavNot3=int(input("sınav notunuzu giriniz : "))
ort=(sinavNot+sinavNot2+sinavNot3)/3
if ort>=50:
    print(f"Tebrikler {round(ort,2)} ortalama ile dersi geçtiniz...")
else:
    print(f'''{round(ort,2)} ortalama ile kaldınız..
Daha fazla çalışmalısınız..''')
"""
"""
a=int(input("lütfen 1. sayıyı giriniz : "))
b=int(input("Lütfen 2. sayıyı giriniz : "))
if a>b:
    print(f"{a} > {b}")
"""
"""
a=int(input("Lütfen bir sayı giriniz : "))
mutlak=a*(-1)
if a<0:
    print(f"{a} sayının mutlak değeri",mutlak)
else: 
    print(f"{a} sayısının mutlak değeri {a}")
"""
"""
a = int(input('Lutfen Bir Sayi Giriniz\t: '))
b=a
if a < 0:
    a *= -1
print(f'{b}, sayisinin mutlak degeri, {a}')
"""
"""
transfeEdilecekPara=int(input("EFT yapılacak miktar : "))
bankaKodu=1
bakiye=5000
transferKodu=int(input("Transfer kodu : "))
güncelBakiye=(bakiye-transfeEdilecekPara)
kesinti=0

if transferKodu==bankaKodu:
    kesinti=(transfeEdilecekPara*0.05)
    print(f"{transferKodu} kodlu bankaya {transfeEdilecekPara} TL yoladınız.")
    print(f"Kesinti {kesinti}")
    print(f"Güncel bakiyeniz {güncelBakiye-kesinti} TL")
"""
"""
bakiye = 5000

bankaKodu = int(input("Banka kodu giriniz."))
transferUcret = float(input("transfer etmek istediğiniz ücreti giriniz."))
kesinti = 0

if bankaKodu != 101:
    kesinti = (transferUcret*5)/100
    
print(f"Güncel bakiye:  {bakiye-transferUcret-kesinti}")
"""
"""
biletFiyati=int(input("Bilet fiyatını giriniz : "))
yurticiMi=True
bavulAgirligi=float(input("Lütfen bavul ağırlığını giriniz : "))
if bavulAgirligi>15:
    fark=((bavulAgirligi-15)*5)
    biletFiyati+=fark
    print(f"{bavulAgirligi-15} ekstra ağırlık için {fark} TL ödediniz.")
print("Ödenecek olan tutar : ",biletFiyati*1.18,"TL")
"""
#üç sayı girilecek en büyüğü ekrana yazılacak
"""

a=int(input("lütfen bir sayı giriniz : "))
eb=0
if a>eb:
    eb=a
a=int(input("lütfen bir sayı giriniz : "))
if a>eb:
    eb=a
a=int(input("lütfen bir sayı giriniz : "))
if a>eb:
    eb=a
print(f"girilen sayıların en büyüğü {eb}")

"""
#endregion

