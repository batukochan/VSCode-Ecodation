# region bool fonksiyonlar
'''
def ciftMi(x):
    """fonksiyon içerisinde verilen sayının
    tek ya da çift olma durumuna göre boolean 
    bir değer döndürür."""
    if x % 2 == 0:
        return True
    return False

deger = ciftMi(11)
a = ciftMi
print(a(12)) # True → a aslında ciftMi fonksiyonu olmuştur. Yeniden adlandırma!
print(deger) # False
print(a) # function ciftMi at adress
print(type(a)) # class <function>
'''
# endregion

# region *args
'''
Fonksiyonumuzun alacağı parametreleri bilemediğimiz 
durumda '*args' parametresini alır.
'''
"""
def topla(*args):
    return sum(args)
    
print(topla(2,3,4,5,6,7,8,9))
"""
# endregion

# region lambda
