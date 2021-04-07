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
haftanın birinci gğnğ pazartesi 
'''
"""
haftaninGunleri = ["","pzts","sl","çrş","prsb","cm","cmts","pzr"]
liste =[f"Hafanın {i}. günü {haftaninGunleri[i]}" for i in range(1,8)] 
print(liste)
"""
#endregion

#region
"""
''' favori ayı sor
çıkmak için -1
'''
favoriAy = []
 while True:
     favAy = input('''
     Favori aylarınızı yazınız.
     favori ay : 
     ''')
     if favAy == '-1':
         break
    for i in favoriAy:
        if favoriAy not in favoriAy:
            favoriAy.append(favAy)
    print(favoriAy)
"""
#endregion

#region 

