# region kare çıktısı veren fonksiyon
"""
def yildizKareFor(n=3):
    '''
    n x n formatında kare yazdırır.
    '''
    for i in range(n):
        for a in range(n):
            print(" * ",end="")
        print()

yildizKareFor()
"""
"""
def yildizWhile(n=3):
    i,j = 0,0
    while i != n:
        i += 1
        while j != n:
            print(" * ",end="")
            j += 1
        print()
        j = 0

yildizWhile(12)
"""
# endregion

# region üçgen
"""
def ucgenWhile(n=5):
    i=1
    while i != n:
        print(" *"*i)
        i += 1
ucgenWhile(12)
"""
# endregion

# region ters üçgen
"""
def tersUcgenWhile(n=5):
    i=n
    while i != 0:
        print(" *"*i)
        i -= 1
tersUcgenWhile()
"""
"""
def tersUcgenFor(n=3):

    for i in range(n,0,-1):
        print(" *"*i)

tersUcgenFor(12)
"""
# endregion

# region
"""
def tersUcgenFor(n=3):
    for i in range(1,n+1,1):
        print(" *"*i)
        if i == n:
            for i in range(n-1,1,-1):
                print(" *"*i)  
            break 

tersUcgenFor(12)
"""
# endregion

# region
""""
isim = input('Lütfen adınızı girin...\nAdınız: ')

i = 0
while i<10:
    i += 1
    print(f'{i}. {isim[0]}') 
"""
# ismin ilk harfini alma şekline birkaç ders sonra değineceğim.

# for döngüsü ile

isim = input('Lütfen adınızı girin...\nAdınız: ')
"""
for i in range(1,11):
    print(f'{i}. {isim[0]}') 
"""
# endregion