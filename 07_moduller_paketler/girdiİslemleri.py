"""
Kullanıcıdan girdi ister.
İstenilen sonuç tipi ne ise ona göre sonuç döner.
"""

def girdiİste(tip='metin'):
    return input(f'Lütfen bir {tip} giriniz: ')


def stringAl():

    """
    Kullanıcıdan metin alır ve o metni döner
    str
    """        
    girdi = girdiİste()
    return girdi

def tamSayiAl():
    """         
    Kullanıcıdan tam sayı alana kadar devam eder.
    """
    while True:
        try:
            girdi = girdiİste("tam sayı")
            sayi = int(girdi)
        except ValueError:
            continue
        else:
            return sayi
            

def ondalikSayiİste():
    """         
    Kullanıcıdan tam sayı alana kadar devam eder.
    """
    while True:
        try:
            girdi = girdiİste("ondalık sayı")
            sayi = float(girdi)
        except ValueError:
            continue
        else:
            return sayi
            