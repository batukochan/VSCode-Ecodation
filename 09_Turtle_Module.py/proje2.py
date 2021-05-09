import turtle
"""
def kaplumbagaYarat():
    t = turtle.Turtle()
    return t

kaplumbagaYarat()
turtle.mainloop()
"""
# region kare çiz
"""
t = turtle.Turtle()

def kareCizimi():
    for i in range(4):
        t.fd(100)
        t.lt(90)
    
kareCizimi()
turtle.mainloop()
"""
# endregion

# region kare ( parametre alan )

t = turtle.Turtle()

def kareCizimi(t,n):
    """
    Kaplumbağa ile kare çizme fonksiyonu.
    Parametreler: 
        * t: kaplumbağa tipinde nesne, mesafe 
        * uzunluk: int tipinde yürüme miktarı (pixel)
"""
    for i in range(4):
        t.fd(n)
        t.lt(90)
'''    
kareCizimi(t,35)
turtle.mainloop()
'''
# endregion

#region 100,200,350 pixel kare çağır, 200-250 arasını 10 pixel arayla doldur.
"""
def doldur():
    '''
    fark doldurmak istediğimiz pixel sayısı
    '''
    for i in range(1,11):
        kareCizimi(t,200 + i*5)

kareCizimi(t,100)
kareCizimi(t,200)
kareCizimi(t,350)
doldur()
turtle.mainloop()
"""
#endregion

#region poligon
'''
def poligon(t, n, uzunluk):
    """
        Kaplumbağa ile poligon çizme fonksiyonu.
        Parametreler: 
            * t: kaplumbağa tipinde nesne, mesafe             
            * n: int tipinde kenar sayısı
            * uzunluk: int tipinde yürüme miktarı (pixel)
"""
'''
"""
def poligon(t, uzunluk, n):
    aci = 360/n
    for i in range(n):
        t.fd(uzunluk)
        t.lt(aci)

poligon(t,70,7)
turtle.mainloop()
"""
#endregion