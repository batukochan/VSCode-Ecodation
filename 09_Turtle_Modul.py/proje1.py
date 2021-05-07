import turtle 

kaplumbaga = turtle.Turtle()
turtle.mainloop() #aksiyon bekler...

def kaplumbagaYarat():
    tospik = turtle.Turtle()
    return tospik

tospik = kaplumbagaYarat()
turtle.mainloop() #kodun son satırı olmak zorunda
#turtle.fd(n) Kaplumbağayı ileri hareket ettirir. (n) pixel kadar
#turtle.bk(n) Kaplumbağayı geri hareket ettirir. (n) pixel kadar
#turtle.lt(d) Kaplumbağayı sola hareket ettirir. (d) açısı kadar
#turtle.lt(d) Kaplumbağayı sağa hareket ettirir. (d) açısı kadar

#bir kaplumbağa yarat

tospik = kaplumbagaYarat()
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)
turtle.mainloop()
