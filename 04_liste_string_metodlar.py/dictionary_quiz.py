# region quiz

def kelimelerSozlugu():
    MINKARAKTERUZUNLUGU = 19
    # boş sözlük yaratıyoruz
    sozluk = dict()
    dosya = open('C:\\Users\\batuh\\Downloads\\kelime.txt')
    for i,satir in enumerate(dosya):
        #satır içerisindeki \n karakterleri silmeliyiz
        satirDizisi = satir.split()
        kelime = satirDizisi[0]
        if len(kelime)>= MINKARAKTERUZUNLUGU:
            #print(kelime)       
            if not kelime in sozluk:
                sozluk[kelime] = len(kelime)
    return sozluk

print(kelimelerSozlugu())

#devam edeceğim
