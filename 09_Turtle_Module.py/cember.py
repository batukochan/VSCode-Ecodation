import math
import turtle

t = turtle.Turtle()


def poligon(t, uzunluk, n):
    aci = 360/n
    for i in range(n):
        t.fd(uzunluk)
        t.lt(aci)


"""
def cember(t, r):
    cevre = 2*math.pi*r
    n = 50
    uzunluk = cevre/n
    poligon(t, n=n, uzunluk=uzunluk)
cember(t, 100)
"""


def cember(t, r):
    cevre = 2*math.pi*r
    n = int(cevre/3)
    uzunluk = cevre/n
    poligon(t, n=n, uzunluk=uzunluk)

cember(t,50)
turtle.mainloop()
