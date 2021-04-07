#region in, not in --- CRUD 
"""
meyveler = ["elma","armut","muz","ayva","üzüm","elma"]
print(meyveler)
arananMeyve = input('''
Lütfen aradığınız meyve isimini giriniz
Aranılan meyve:
''')
if arananMeyve in meyveler:
    print(f"{arananMeyve} listede var.")
else:
    print(f"{arananMeyve} listede var.")
""" 
#endregion

#region arama index ile
"""
meyveler = ["elma","armut","muz","ayva","üzüm","elma"]
print(meyveler)
arananMeyve = input('''
Lütfen aradığınız meyve isimini giriniz
Aranılan meyve:
''')
print(meyveler.index(arananMeyve))
if meyveler.index(arananMeyve) >= 0:
    print("var")
else:
    print("yok")
"""

"""
meyveler = ["elma","armut","muz","ayva","üzüm","elma"]
print(meyveler)
arananMeyve = input('''
Lütfen aradığınız meyve isimini giriniz
Aranılan meyve:
''')
print(meyveler.count(arananMeyve))
if meyveler.count(arananMeyve) != 0:
    print("var")
else:
    print("yok")
"""
#endregion

#regipon 
'''
tekrarsız liste
'''
"""
meyveler = ["elma","armut","muz","ayva","üzüm","elma"]
tekrarsizListe = []
for i in meyveler:
    if i not in tekrarsizListe:
        tekrarsizListe.append(i)
print(tekrarsizListe)
"""    
#endregion
