#region liste metodları
"""
liste = [1 , 2 , 3 , 4 , 5]
del liste[-1]
print(liste)
del liste[(len(liste)-1)]
print(liste)
"""
"""
liste = [1 , 2 , 3 , 4 , 5]
liste.pop()
print(liste)
"""
#endregion

#region .append
'''
listeye yeni bir eleman ekler
'''
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f"listemizdeki meyveler : {meyveler}")
meyveler.append("karpuz")
print(meyveler)
"""
#endregion

#region insert
'''
istediğimiz bir indexe eleman ekler
'''
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f"listemizdeki meyveler : {meyveler}")
meyveler.insert(2,"portakal") #2. indexe elemanı ekler diğer elemanları kaydırır.
'''
insert(int,eleman)
'''
print(f"listemizdeki meyveler : {meyveler}")
"""
#endregion 

#region remove
'''
listeden içine yazılan elemanı siler.
'''
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f"listemizdeki meyveler ilk hal: {meyveler}")
meyveler.remove("muz") #listede olmayan bir eleman girersek hata verir.
print(f"listemizdeki meyveler son hal: {meyveler}")
"""
#endregion

#region pop 
'''
Listedeki son elemanı siler.
'''
#last in first out :)
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f"listemizdeki meyveler ilk hal: {meyveler}")
meyveler.pop()
print(f"listemizdeki meyveler son hal: {meyveler}")
"""
'''
sebzeler = []
sebzeler.pop()
print(sebzeler)
IndexError: pop from empty list
'''
#endregion

#region clear
'''
listenin tüm elemanlarını siler
'''
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f"listemizdeki meyveler ilk hal: {meyveler}")
meyveler.clear() #içine parametre yazılmaz.
print(f"listemizdeki meyveler son hal: {meyveler}")
"""
#endregion

#region copy
'''
bir isim belirleriz ve eşitliğin sol tarafında kopyalamak istediğimiz listeninyanın .copy()
şeklinde yazarız.
meyveTabagi = meyveler.copy() -> meyveTabagına meyveler listesinin elemanlarını kaydeder.
'''
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
meyveTabagi = meyveler.copy()
del meyveler
print(meyveTabagi)
print(type(meyveTabagi))
"""
#endregion

#region count
"""
listeRakamlar = [2,5,6,1,9,7,5]
arananEleman = 0
elemanAdedi = listeRakamlar.count(0)
print(f"listemizde {arananEleman} adedi {elemanAdedi} ")
"""
#endregion

#region örnek 1
"""

meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
arananMeyve = "karpuz"
elemanAdedi = meyveler.count(arananMeyve)
if elemanAdedi: # !=0
    print(f"aradığınız {arananMeyve} listede yer almaktadır.")
else:
    print(f"Aradığınız {arananMeyve} listede yer almamaktadır.")

"""
#endregion

#region sort reverse
"""
listeRakamlar = [2,5,6,1,9,7,5]
print(f"listenin ilk hali -> {listeRakamlar}")
listeRakamlar.sort()
print(f"listenin son hali -> {listeRakamlar}")
listeRakamlar.reverse()
print(f"listenin son hali -> {listeRakamlar}")
"""
#endregion

#region index
"""
listeRakamlar = [2,5,6,1,9,7,5]
print(f"listenin ilk hali -> {listeRakamlar}")
print(listeRakamlar.index(7)) #7. indexteki elelmanı döndürür.
print(f"listenin son hali -> {listeRakamlar}")
"""
#endregion