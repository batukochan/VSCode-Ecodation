# region standart moduller

"""
Moduler Programlama:
- Kod tekrarını önler.
- Organizasyon (web, db, api...)
- Yönetim ve bakım kolaylığı
"""

"""
Modul: .py ile biten Python dosyasıdır.
Paket: Birçok modulü şçeren Python klasörleridir.
"""

"""
'import' edilerek kullanılır.
"""

# import işlemi bize dosyayı çağırır.

# endregion

# region Örnek random modul

import random

olasilik = random.random() # 0-1 arasında olasılık verir.
# print(olasilik)

# 10 ile 50 arasında olasılıkları alalım

rastgeleSayi = random.randint(10,51)
# print(rastgeleSayi)

# Listeden rastgele elman alma

liste = [1,2,3,4,5,6,7,8,9]

eleman = random.choice(liste)
# print(eleman)

# örneklem almak

orneklem = random.sample(liste, 4)
# print(orneklem)

# endregion

# region platform modul

import platform

a = platform
# print(a)

# platform türü

# print(platform.platform()) # Windows-10-10.0.19041-SP0

# platform mimarisi

# print(platform.architecture()) # ('64bit', 'WindowsPE')

# makine tipi

# print(platform.machine()) # AMD64

# işletim sistemi

# print(platform.system()) #windows

# endregion

# region sys

import sys

# path

# print(sys.path)

yollar = sys.path
"""
for yol in yollar:
    print(yol)
"""
# sys.path Python'un modul aradığı dosya yollarıdır.

"""
Modul import ederken adını değiştirmek isteyebiliriz.
"""

"""
import random as rnd
Alise
"""

# bir modulün bir parçasını çağırmak

"""
from <modulAdi> import <modulParcasi>
"""

"""
from sys import modules

print(f"hazır moduller: {modules}")
"""

"""
from math import sqrt as karekok

print(karekok(4))
"""

# endregion
