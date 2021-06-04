#region tek satırda for
"""

liste = []
for i in range(1,9):
    liste.append(i)
print(liste)

liste = [i for i in range(1,9)]
print(liste)

"""
#endregion

#region
'''
haftanın birinci günü pazartesi 
'''
"""
haftaninGunleri = ["","pzts","sl","çrş","prsb","cm","cmts","pzr"]
liste =[f"Hafanın {i}. günü {haftaninGunleri[i]}" for i in range(1,8)] 
print(liste)
"""
#endregion

#region 
"""
haftaninGunleri = ["","pzts","sl","çrş","prsb","cm","cmts","pzr"]
liste =[f"Hafanın {i}. günü {haftaninGunleri[i]}" for i in range(1,8) if i>3] 
print(liste)
"""
#endregion

#region
"""
'''
Sonsuz döngü içinde: favori aylar girilecek
daha önce ekledi isek uyaracak
'''
favoriAylar = []
while True:
    fav = input("favori ayınız, çıkmak için -1: ")
    if fav=="-1":
        break
    if fav in favoriAylar:
        print("daha önce ekledi")
        continue
    favoriAylar.append(fav)
print(favoriAylar)
"""
#endregion
