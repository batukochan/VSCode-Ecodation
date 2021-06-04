'''Örnek 1: Python ile bir liste içinde 3’ün
katları olan sayıları listeleme.'''

def sayiListesi():
    sayiListem = []
    import random
    for i in range(30):
        sayi = random.randint(1,100)
        if sayi not in sayiListem:
            sayiListem.append(sayi)
    return sayiListem

a = sayiListesi()
uceBolunenler = []
for i in a:
    if i % 3 == 0:
        uceBolunenler.append(i)
print((uceBolunenler))




