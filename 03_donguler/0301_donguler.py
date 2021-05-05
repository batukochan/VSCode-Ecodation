# region giriş
# loop
'''
loop ne zaman kullanılır ?
loop -> sürekli tekrarlayan bir yapı varsa 
'''
"""
i=0
while i<5:
    print("sponsorlu ürün")
    i+=1
"""
# endregion

# region dikkat

''' 
sonsuz döngüye girersen ctrl+c ile kesebilirsin.
başlangıç
bitiş
artış miktrına dikkat et
'''
# endregion

# region başlangıç
'''
i=0
while i<3:
    i+=1
    print("selamlar")
'''
# endregion

# region örnek 1
'''
i = 1
print("a")
while i<5:
    print("b")
    i += 1
print("c")

'''
"""
i = 1
print("a")
while i<=3:
    print("b")
    if i==2:
        print("elif")
    i += 1
print("c")
"""
# endregion

# region örnek 2
'''
i=5
while i!=0: # i: deyazsaydık olurdu
    print(i)
    i-=1
'''
# endregion

# region örnek 3
"""
sayac = 5
devamMi = True
while devamMi==True: 
    print(sayac)
    if sayac==2:
        devamMi=False
    sayac -= 1
"""
# endregion
