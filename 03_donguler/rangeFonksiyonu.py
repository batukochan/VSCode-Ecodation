# region for yapısı
'''
for degiskenAdi in degisken:
    #yapılacak işlem
'''
# örnek
"""
takim = 'BEŞİKTAŞ'
for harf in takim:
    print(harf, end=' ♥ ')
"""
# endregion


# 1
for i in range(10):
    print(i, end=' ')
print()
'''
    Fonksiyona tek bir değer verdiğiniz durumda 
fonksiyon '0' ile başlar ve verdiğiniz değerden 
bir eksik değere kadar sayar.
çıktı → 0 1 2 3 4 5 6 7 8 9 
'''

# 2
for sayı in range(1,10):
    print(sayı, end=' ')
print()
'''
    Fonksiyona iki değer verildiği durumda ise
değerlerden ilkini başlangıç noktası ikincisini 
varış noktası kabul eder ve artış miktarını '1' 
kabul eder.
çıktı → 1 2 3 4 5 6 7 8 9
'''

# 3
for kalem in range(1,11,2):
    print(kalem, end=' ')
print()
'''
    Fonksiyona tüm değerlerini verdiğiniz durumda
(başlangıç,bitiş,artış) şeklinde yorumlar.
çıktı → 1 3 5 7 9
'''

# 4
for ters in range(10,-1,-1):
    print(ters, end=' ')
print()
'''
    Artış miktarını negatif olarak da kullanabiliriz.
çıktı → 10 9 8 7 6 5 4 3 2 1 0
'''

# 5
for ters in range(-10,5,1):
    print(ters, end=' ')
print()
'''
   Negatif değerden pozitif artış miktarı ile ilerleyebiliriz.
çıktı → -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 
'''
