import turtle
# region giriş
'''
def kaplumbagaYarat():
    tospik = turtle.Turtle()
    return tospik
"""
tospik = kaplumbagaYarat()
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
turtle.mainloop()"""
tospik = kaplumbagaYarat()
for i in range(4):
    tospik.fd(100)
    tospik.lt(90)
'''
# endregion

# region kare örneği
"""
def kare(t,uzunluk):
    '''
    kaplumbağa ile kare çizer.
    t: turtle tipinde nesne
    uzunluk : yürüme miktarı pixel(int)
    '''
    for i in range(4):
        t.fd(uzunluk)
        t.lt(90)

tospik = turtle.Turtle()
kare(tospik,100)
kare(tospik,200)
kare(tospik,250)

for i in range(10):
    kare(tospik,100+i*5)
"""
# endregion

# region harf
"""
def kaplumbagaYarat():
    tospik = turtle.Turtle()
    return tospik

tospik = kaplumbagaYarat()
tospik.lt(180)
tospik.fd(25)
tospik.rt(90)
tospik.fd(150)
tospik.rt(90)
tospik.fd(25)
tospik.rt(45)
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
tospik.rt(45)
tospik.fd(25)
tospik.rt(90)
tospik.fd(150)
tospik.rt(90)
tospik.fd(25)
tospik.rt(90)
tospik.fd(125)
tospik.lt(135)
tospik.fd(100)
tospik.rt(90)
tospik.fd(100)
tospik.lt(135)
tospik.fd(125)
turtle.mainloop()
"""
# endregion
