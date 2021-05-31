# region exception fırlatma

"""
Hata anında yapacağımız işlemdir.
"""

# örnek

def hataFirlat():
    girdi = input("Lütfen bir sayı giriniz")

    # eğer olası hatalar düşünülmezse program  -> crach

    if not girdi.isdigit():
        raise Exception("Lütfen nümerik sayı giriniz...")

    sayi = int(girdi)
    print(sayi)
"""
hataFirlat()
# ValueError: invalid literal for int() with base 10: 'as'
Exception: Lütfen nümerik sayı giriniz...
"""

def tanimliHata():

    girdi = input("Lütfen bir sayı giriniz")

    # eğer olası hatalar düşünülmezse program  -> crach

    if not girdi.isdigit():
        raise ValueError("Lütfen nümerik sayı giriniz...")

    sayi = int(girdi)
    print(sayi)
"""
tanimliHata()
# ValueError: Lütfen nümerik sayı giriniz...
"""

# assert

def girdiDogrula():

    girdi = input("Lütfen bir sayı giriniz")

    # eğer olası hatalar düşünülmezse program  -> crach

    assert int(girdi), ValueError("Lütfen sayı giriniz...")

    sayi = int(girdi)
    print(sayi)

"""
girdiDogrula()
    assert int(girdi), ValueError("Lütfen sayı giriniz...")
ValueError: invalid literal for int() with base 10: 'as'
"""

def bolme(a,b):
    assert b != 0, 'Sıfıra bölme yapılamaz!'
    print(a/b)
"""
bolme(10,0)
"""