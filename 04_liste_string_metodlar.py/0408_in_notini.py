# region python_arama_metodları
"""
→ List index metodu: Liste elemanlarında arama yapar. 
Bulduğu anda index’i geriye döndürür. Ancak bulamadığı anda value error fırlatılır. 

→ List count medodu: Tam olarak arama özelinde bir metod değildir. 
Parametre ile gönderilen değerin, listede kaç adet olduğunu geriye döndürdüğü için 

dolaylı şekilde arama sürecine dahil edilebilir. Geriye sıfır döndüğünde bulamadığı anlaşılır.
→ In / Not In : bir diğer arama metodudur. Kullanımı oldukça basittir.
"""
# endregion

# region index
"""
kurumAdi="Flux"
print(kurumAdi.index("u")) #u karakteri 2. indexte
"""

# endregion

# region index_ornek
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz: ")
if  meyveler.index(arananMeyve) >= 0:
    print(f'''
Aradığınız {arananMeyve}, listenizde yer almaktaadır.
    ''')
"""
# endregion

# region count
"""
kurum= "Flux"
print(kurum.count("F")) # 1 ADET  VAR
"""
# endregion

# region count_ornek
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz: ")
if meyveler.count(arananMeyve)!=0:
    print(f'''
Aradığınız {arananMeyve}, listenizde yer almaktaadır.
    ''')
else:
    print(f'''
Aradığınız {arananMeyve}, listenizde yoktur.
    ''')
"""
# endregion

# region in_notin
"""
kurum= "Flux Architecture"
if "e" in kurum:
    print("var")
else:
    print("yok")
"""
# endregion

# region in_notin_ornek
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz: ")
if arananMeyve in meyveler:
    print(f"{arananMeyve} liste elemanları içinde mevcut")
else:
    print(f"{arananMeyve} liste elemanları içinde yok")
"""
# endregion

# region tekrarsiz_liste
"""
listede tekrar eden elemanlar var. tekrarsız liste oluşturan pratik yapalım
meyveler = ["elma", "armut", "üzüm", "muz", "ayva", "üzüm", "elma"]
yeniListe = []
for i in meyveler:
    if i not in yeniListe:
        yeniListe.append(i)
print(yeniListe)
"""
# endregion
