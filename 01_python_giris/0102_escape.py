#region invoke fonksiyon çağırmak
"""
Tırnak işaretlerini kullanarak kendimize yorum satırları hazırlayabiliriz.
"""
""" """ 
print() #argüman kullanılmayan her print eylemi 1 satır boşluk bırakır.
print("Python")
print()
print("Eğitimi")
print()
print("***Yeni Üye***")
print("")  

#6. satır ile 12. satır arasındaki kodları tek seferde kısaca yazabiliriz.

print('''

Python

Eğitimi

***Yeni Üye***

''')

# ''' tek tırnak yapısı arasında rahatça yazılar yazabiliriz. ''' 
# """ Çift tırnakları da benzer şekilde kullanabiliriz."""

#endregion

#region escape 

''' açıklama için kullanılır. '''

print( "Python\nEğitimi\nYeni Üye") # \n ifadesi kendinden sonra gelen yazıyı bir alt satıra alır.
print( "Python\tEğitimi\tYeni Üye") # \t ifadesi kendinden sonra gelen yazıyı bir tab mesafesi öteler.
print("merhaba \"Değerli Okur\" ")  
''' print ifadesine başlamış olduğumuz tırnak işaretini başka bir yerde kullanmak için 
\" ya da \' şeklinde kullanarak hataları önleriz.
'''
print("İstanbulun'un") # print fonksiyonunda " " kullandığımız için ' hata vermez
print('İstanbu\'un') #hata almamak için kullandık.

#endregion

#region print çeşitli escape örnekleri

print('Progamlamada Python\'un yeri ayrıdır')

print('Türkiye\'nin başkenti Ankara\'dır.')

print('''İstanbul'un en güzel semti "Beyoğlu" mu ? ''')

print("""İstanbul'un en güzel semti "Beyoğlu" mu ? """)

#endregion

