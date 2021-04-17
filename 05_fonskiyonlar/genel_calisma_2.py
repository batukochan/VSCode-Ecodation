#region lamda fonksiyonu
'''
Pythonda Lambda Fonksiyonu
Pythonda isimsiz olarak tanımladığımız fonksiyonlara lambda fonksiyonları denir. 
'''
"""
karesi = lambda a: a**2
print(karesi(4)) 

a = lambda a, b, c : a + b + c
print(a(12, 34, 4))
"""
#endregion

#region Lambda Fonksiyonu Neden Kullanılır?
'''

                    Lambda Fonksiyonu Neden Kullanılır?
    Lambda fonksiyonu bir başka fonksiyon içinde kullanıldığında anlam kazanır. 

    Örneğin bir sayının karesini mi kübünü mü almak istediğinizden emin değilsiniz. Bu 
durumda bir fonksiyon içerisinde lambda tanımlaması yaparak istediğimiz bir aşamada geriye 
çalıştırılabilir bir fonksiyon döndürebilirsiniz.
-SADIK TURAN
'''
"""
def math(n):
  return lambda a : a ** n

square = math(2) # n = 2
cube = math(3) # n = 3

print(square(3)) # a = 3 | n = 2 | sonuç = 9 
print(cube(3))   # a = 3 | n = 3 | sonuç = 27
"""
#endregion

#region Python Map Fonksiyonu

'''
                            Python Map Fonksiyonu
    Pythonda map fonksiyonu aracılığıyla referansı belirtilen bir fonksiyona 
belirtilen bir listenin tüm elemanları sırayla gönderilip liste üzerinde istenilen
yapılandırılma yapılır.
'''

"""
sayilar = [1,3,5,7,11]

def karesi(a):
    return a**2

sonHali = list(map(karesi,sayilar))
print(sonHali)
"""

"""
sayilar = [1,3,5,7,11]
sonHali = list(map(lambda a:a**2,sayilar))
print(sonHali)
"""

#endregion

#region Filter fonksiyonu

'''
    Map fonksiyonunda liste içerisindeki her bir sayı fonksiyona gönderilip 
bir işlem görüyor ve geriye gönderiliyor ancak filter metodu ile geriye dönecek 
bir filtre uygulayabiliriz
Sadık Turan
'''
"""
sayilar = [1,3,4,5,7,8,11,14]
sonHali = list(filter(lambda a: a%2 == 0,sayilar))
print(sonHali)
"""