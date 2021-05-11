# region 1
""""
a = "mUSTAFA kEMAL aTatürk"
print(a.title()) # Mustafa Kemal Atatürk
"""
# endregion

# region 2

def harfSay(metin, harf):
    return metin.count(harf)
"""
metin = input("Lütfen bir cümle girin...\nMetin → ")
harf = input("Lütfen bir aradığınız harfi girin...\nHarf → ")
print(harfSay(metin,harf))
"""
# endregion

# region 

def harfBilgisi():
    metin = input("Lütfen bir cümle girin...\nMetin → ")
    yazilanHarfler = []
    for harf in metin:
        if harf == " ":
            continue
        adet = harfSay(metin, harf)
        if harf not in yazilanHarfler:
            print(f"{harf} harfi {adet} adet bulundu.")
            yazilanHarfler.append(harf)
harfBilgisi()

# endregion
