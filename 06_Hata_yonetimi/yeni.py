def listeToplami(liste):
    
    try: 
        toplam = 0
        for sayi in liste:
            toplam += sayi
        return toplam
        
    Except TypeError as typeError:
        raise typeError

liste = [1,2,3,4,5,6]

print(listeToplami(liste))