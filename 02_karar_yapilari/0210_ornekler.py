#region örnek 1
"""
a=int(input("Lütfen axb formatında olan dörtgenin a kenarını yazınız : "))
b=int(input("Lütfen axb formatında olan dörtgenin b kenarını yazınız : "))

if a==b:
    print(f"Kenar uzunuğu {a} olan karenin alanı {a*b} metrekaredir.")
else:
    print(f"Kenar uzunlukları {a} m ve {b} m olan dikdörtgenin alanı {a*b} metrekaredir.")
"""
#endregion

#region örnek 2
"""
a=int(input("Lütfen uzun kenarını yazınız : "))
b=int(input("Lütfen kısa kenarını yazınız : "))

if a>b:
    print(f"kısa kenarı {a} uzun kenarı {b} olan dörtgenin alanı : {a*b} metrekaredir.")
elif a==b:
    print("Kare istemedik.")
else:
    print(f"a kenarı b kenarından küçük olamaz")
"""
#endregion

#region örnek 3
"""
a=int(input("Lütfen bir sayı giriniz : "))
b=int(input("Lütfen bir sayı giriniz : "))

if a%b==0:
    print(f"{æ} sayısı {b} sayısına tam bölünür")
else:
    print(f"{a} sayısı {b} sayısına Tam bölünmez")
"""
#endregion

#region örnek 4
"""
a=int(input("Lütfen vize notunuzu giriniz : "))
b=int(input("Lütfen final notunuzu giriniz : "))
ort=(a+b)/2
if 60>=ort>=50:
    print("C ALDINIZ")
elif 70>=ort>60:
    print("B ALDINIZ")
elif 80>=ort>70:
    print("B ALDINIZ")
elif 100>ort>80:
    print("A ALDINIZ")
else:
    print("kaldınız")
"""
#endregion

#region örnek 5
"""
a=int(input("Lütfen bir sayı giriniz : "))
b=int(input("Lütfen bir sayı giriniz : "))

if a>b:
    print(f"{a} sayısı {b} sayısından büyüktür.")
elif a<b:
    print(f"{b} sayısı {a} sayısından büyüktür.")
else:
    print("sayılar birbirine eşittir.")
"""
#endregion

#region örnek 6
"""
kullaniciAdi=str(input("Kullanıcı adı : "))
parola=str(input("Parola : "))
if kullaniciAdi=="batukochan" and parola=="123":
    print(f"Merhaba {kullaniciAdi}, sitemize hoş geldiniz.")
else:
    print("**Kullanıcı adı veya parola hatası***")
"""
#endregion

#region örnek 7

a=int(input("Lütfen bir sayı giriniz : "))
b=int(input("Lütfen bir sayı giriniz : "))
c=int(input("Lütfen bir sayı giriniz : "))

if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b
print(f"{a}>{b}>{c}")

#endregion
