#region
"""
def topla(a,b,c):
    print(f"{a} + {b} + {c} = {a+b+c}")

topla(12,13,14)
topla(b=1,c=22,a=12)
"""

'''
fonksiyon gelen değerleri liste elemanı olarak işler
for döngüsü içinde istediğim algoritmayı yürütürüm
'''

"""
def topla(*args):
    toplam = 0
    for i in args:
        toplam += i
    print(toplam)

topla(22,13,14,15,17) 
"""

"""
def topla(*args):
    return sum(args)

print(topla(2,3,4,5,6,7))

"""

"""
def ortalama(*eleman):
    print(sum(eleman)/len(eleman))

ortalama(4,5,6,7,8)
"""
#endregion

#region

'''
tekil liste(3,5,7,10,12,5,7)
output()
'''

"""
def tekilListe(*elemanlar):
    yeniListem = []
    for i in elemanlar:
        if i not in yeniListem:
            yeniListem.append(i)
    print(yeniListem)

tekilListe(3, 5, 7, 10, 12, 5, 7)
"""

#endregion