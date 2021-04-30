# region nested if örnek 1
"""
para = True
vakit = True
if para == True:
    if vakit == True:
        print("Sinemaya gidebilirsiniz.")
    else:
        print("Online alışveriş yapabilirsin")
else:
    if vakit == True:
        print("Televizyon izleyebilirsin")
    else:
        print("Moralini yüksek tutmaya çalış, her şey güzel olacak!")
"""
# endregion

# region örnek 2
"""
a=int(input("Lütfen bir sayı giriniz : "))
if 100>=a>0:
    print(f"{a} sayısı 0 ile 100 arasındadır.")
else:
    print("Lütfen 0-100 arası bir değer giriniz.")
"""
# endregion

# region örnek
"""
a = int(input("a: "))
b = int(input("b: "))
if a == b:
    print("a ve b birbirine eşittir")
else:
    if a < b:
        print("a, b'den küçüktür")
    else:
        print("a, b'den büyüktür")
"""
# endregion

# region basit örnek

a = int(input("lütfen sayı giriniz... \nSayı : "))
if a > 0:
    if a < 100:
        print(f"{a} sayı 100 den küçüktür, pozitif")
    else:
        print(f"{a} sayı 100 den büyüktür, pozitif")
else:
    print("lütfen 0 ya da negatif değer girmeyin!")

# endregion
