# region tuple yaratmak
"""
tuple1 = 'a', 'b', 'c', 'd'
print(tuple1)
print(type(tuple1))

tuple2 = ('a', 'b', 'c', 'd', '3', '23')
print(isinstance(tuple2, tuple))  # True

# tek elemanlı tuple

tuple3 = 'a',
'''
a = 'x' # str
b = ('x') # str
'''
print(isinstance(tuple3, tuple))  # True

tuple4 = tuple()

print(isinstance(tuple4, tuple))  # True

dil = tuple('Python')
# print(dil,type(dil)) # ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'>

print(dil[3])  # h, index ile kullanılabilir.

'''
tuple, değiştirilemez.
'''
print(dil[::])
print(dil[::-1])  # tersten yazabiliriz.

# tuple karşılaştırma

print((0, 1, 2) < (3, 4, 5))

print((5, 40, 200) < (6, 3, 5)) # ilk önce 5 ile 6yı karşılaştırır gerisine bakmaz.

print(('abcd2',) < ('abcd3',))
"""

# endregion

# region tuple atama
"""
a = 99
b = 1
a, b = b, a
print('a:', a)
print('b:', b)
'''
değişken sayısı eşit olmalıdır.
a, b = 300, 400, 500
'''
"""

"""
a = (32, 74, 23)
b = (10, 20, 30)
a, b = b, a
# print(a,b)
c = (22, 23, 24, 25)
a, c = c, a
print(a, c)
"""
"""
a, b, c, d, e = ['her', 'şey', 'çok', 'güzel', 'olacak']
print(a,type(a)) #str
print(b)
print(c)
print(d)
print(e)
"""
# endregion
