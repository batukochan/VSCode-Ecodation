#region format
"""
#ekrana output formatlarken ilk yöntem .format yöntemidir.
rakam=int(input("Lütfen 0-9 arası bir rakam giriniz :\t"))
print("Girdiğiniz sayı : {} ".format(rakam))
print("-"*40)
print("Girdiğiniz sayının bir fazlası : {} ".format(rakam+1))
"""
#endregion

#region fstring
"""
rakam=int(input("Lütfen 0-9 arası bir rakam giriniz :\t"))
print("Girdiğiniz sayı : {} ".format(rakam))
print("-"*40)
print("Girdiğiniz sayının bir fazlası : {} ".format(rakam+1))
print(f"Girdiğiniz sayının bir fazlası : {rakam+1}")
"""
"""
s1=int(input("lsg :"))
s2=int(input("lsg :"))
print(f"girdiğiniz birinci sayı olan {s1} ile ikinci sayı olan {s2} sayılarının toplamı {s1+s2} olarak hesaplandı")
"""

#endregion

#region örnek1

"""kullanıcı bir sayı girecek , 2. sayı 3. sayı çıktı a b c sayılarının ortlaması"""
"""
a=int(input("Lütfen bir sayı giriniz : "))
b=int(input("Lütfen bir sayı giriniz : "))
c=int(input("Lütfen bir sayı giriniz : "))
ort=(a+b+c)/3
print(f"girilen {a},{b} ve {c} sayılarının ortalaması {round(ort,2)} olarak hesaplandı.")
print("-"*60)
print("\t\t\tYa da")
print("-"*60)
print(f"girilen {a},{b} ve {c} sayılarının ortalaması {round((a+b+c)/3,2)} olarak hesaplandı.")
"""
#endregion

#region örnek2

"""print("
leylek uygulamasına Hoşgeldiniz
    Sürüş Ücreti 59 Krş/dk
)
saat=int(input("Leylek ile geçirilen süre (saat) : "))
dakika=int(input("Leylek ile geçirilen süre (dakika ): "))
ücret=(saat*30)+(dakika*0.59)
print(F"LEYLEK ile geçirilen süre {saat} saat {dakika} dakikadır.")
print("-"*47)
print(f"Ödemeniz gereken ücret {round(ücret,3)} TL")
print("-"*47)
print("Bizleri tercih ettiğiniz için teşekkür ederiz!
                   LEYLEK)"""
#endregion

#region örnek3
"""
a=10
b=2
print(f"{a} sayısı ile {b} sayılarının farkı {a-b}")
print(f"{a} sayısı ile {b} sayılarının toplamı {a+b}")
print(f"{a} sayısı ile {b} sayılarının çarpımı {a*b}")
print(f"{a} sayısı ile {b} sayılarının bölümü {a/b}")
"""
#endregion

#region örnek4
"""d=float(input("Lütfen dönüştürülecek olan dereceyi giriniz :"))
pi=3.14
rad = d*pi/180
grad = d*200/180
print(f"Girilen derece {d} radyan cinsinden hali : {rad}, gradyan cinsinden hali : {grad} ")
"""
#endregion
print("github")
print("ilk önce ctrl+S ile dosyayı kaydediyoruz.")