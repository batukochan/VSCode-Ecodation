#region invoke fonksiyon çağırmak
"""
Tırnak işaretlerini kullanarak kendimize yorum satırları hazırlayabiliriz.
"""
"""
print() #argüman kullanılmayan her print eylemi 1 satır boşluk bırakır.
print("Batuhan")
print()
print("Koçhan")
print()
print("***Yeni Üye***")
print("")  #3. blok ile 8. blok arasındaki kodlar uzun sürdü.
""" 
#endregion

#region escape 

''' açıklama için kullanılır. '''

print( "Batu\nKoçhan\nYeni Üye") # \n ifadesi kendinden sonra gelen yazıyı bir alt satıra alır.
print( "Batu\tKoçhan\tYeni Üye") # \t ifadesi kendinden sonra gelen yazıyı bir tab mesafesi öteler.
print("merhaba \"Batu Koçhan\" ")  
''' print ifadesine başlamış olduğumuz tırnak işaretini başka bir yerde kullanmak için 
\" ya da \' şeklinde kullanarak hataları önleriz.'''

print("İstanbulun'un") # print fonksiyonunda " " kullandığımız için ' hata vermez
print('İstanbu\'un') #hata almamak için kullandık.


#region print çeşitli escape örnekleri

print('merhaba Zeyep\'in dünyası')
print('Türkiye\'nin başkenti Ankara\'dır.')

print('''İstanbul'un en güzel semti "Beyoğlu" mu ? ''')

print("""İstanbul'un en güzel semti "Beyoğlu" mu ? """)

#endregion

