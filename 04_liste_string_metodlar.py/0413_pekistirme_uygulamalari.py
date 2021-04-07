"""
ogrenci1 = ["Alp", "Besi", 90,	90,1997]
ogrenci2 = ["Batu", "Koçhan", 10, 90,1998]
ogrenci3 = ["Emir", "Besi", 100, 90,2008]
ogrenci4 = ["Umut", "Ahmet", 95, 80,2000]
ogrenci5 = ["Aziz", "Bektaş", 15, 10,1980]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]
i = 1
for item in ogrenciler:
    
    if (item[2]+item[3])/2<50:
        print(f"{i} {(2021-(item[-1]))} {item[0]} {item[1]} → KALDI")
    else:
        print(f"{i} {(2021-(item[-1]))} {item[0]} {item[1]} → GEÇTİ")
    i += 1
"""