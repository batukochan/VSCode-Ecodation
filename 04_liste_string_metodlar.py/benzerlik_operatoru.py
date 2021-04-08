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

def greetUser(isim: str, soyisim: str, mesaj: str="Eve Hoş Geldin!"):
    print(f"Merhaba {isim} {soyisim}")
    if mesaj is not None: #mesaj none değilse işleme gir!
        print({mesaj})
greetUser("batu","koçhan",None)

'''
is
is  not gibi ifadeler kimlikleri karşılaştırır.
'''