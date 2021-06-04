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


"""
harfBilgisi()
"""
# endregion

# region

'''
index yapısı sayesinde elemanlarına erişilebilir.
'''
"""
elektronikAlet = 'bilgisayar'
harf = elektronikAlet[6]
print(harf)
"""
# endregion

# region string slicing
''' 
metinin bir parçasına slice (dilim) deriz.
metinden dilim seçmek için index kullanılır.
dizi[başlangıç=0:bitiş=(son index):artış=1]
'''
"""
metin = "Yazılım Öğreniyorum"
dilim = metin[0:7:1]
print(dilim) # Yazılım
print(metin[3:11:2]) # lı ğ
print(metin[:8]) # Yazılım
print(metin[8:]) # Öğreniyorum
print(metin[8:19]) # Öğreniyorum
"""
# endregion

# region tersten index
"""
rakamlar = "123456789"
print(rakamlar[-1]) # 9 
print(rakamlar[-1:-10:-1])
metin = "Yazılım Öğreniyorum"
print(metin[-1:-20:-1]) # Yazılım

print(len(metin)) # 19
print(metin[6]) # m
print(metin[-13]) # m
print(rakamlar[::-2])
print(rakamlar[-6:-3:1])
print(rakamlar[3:6:1])
"""
# endregion

