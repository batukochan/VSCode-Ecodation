#region nesne
"""
print(id(1001))
print(id(1001))
print(id("ahmet"))
print(id("ahmet"))
a = 10
b = 10
print(id(a))
print(id(b))
"""
'''
aynı nesnelerin idleri kimlikleri aynıdır. Pythonda değerler bir nesne sayılıyor ve değşkenler de 
bu nesneleri ifade etmek için kullanılan araçlar olarak düşünülebilir.
'''

'''
None içi boş demektir ve içeriğinde bir şey yok anlamına gelmektedir.
'''
"""
ornekDeger = None
if ornekDeger is None :
    print("değişken değersizdir.")
"""
#endregion

#region
"""
def greetUser(isim: str, soyisim: str, mesaj: str="Eve Hoş Geldin!"):
    print(f"Merhaba {isim} {soyisim}")
    if mesaj is not None: #mesaj none değilse işleme gir!
        print({mesaj})
greetUser("batu","koçhan",None)
"""
'''
is
is  not gibi ifadeler kimlikleri karşılaştırır.
'''
#endregion

#region kapsama alanı
"""
def greet(name): 
    message = "a" #lokal değişkenler
'''
print(message) 
nameError hatası verir
'''
"""

#--------------------------------

""" 
message = "c" #globaldir
def greet(name):
    message = "a"

def greet(name):
    message = "b" 

print(message) # c global değer olduğu için çıktımız c olur.
'''
   Eğer global değişkenini fonksiyon içinde tanımlasaydık (tavsiye edilmez.)
donksiyonun içindeki değişken değeri diğer kod satılarını da etkileyecektir.
'''
"""
#endregion

#region import
"""
from random import choice, randint
karakter = "abcdefghijklmnoprstu0123456789"
parola = ""
for i in range(randint(4,12)):
    parola += choice(karakter)
print(parola)
"""
#endregion





















