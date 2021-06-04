#region Listelere giriş
"""
isimler = ["taha","çagtay","çağrı","musa","serap","mehmet","hande"]
print(isimler) #listeyi olduğu gibi yazdırır -> ["taha","çagtay","çağrı","musa","serap","mehmet","hande"]
print(isimler[3]) #index üzerinden eleman çağırabiliriz.
print(isimler[-1]) #isimleri sondan başlayarak da çağırabiliriz.
'''
index baştan sona -> 0,1,2,3,4,5,6....
index sondan başa -> -1,-2,-3,-4,-5,-6,-7....
'''
print(isimler[2:4]) # 2. ve 3. indexi bastıır.
print(isimler[2:5]) # 2. , 3. ve 4. indexi bastırır.
'''
!!! BU İŞLEMLER ORJİNAL LİSTEYİ DEĞİŞTİRMEZ !!!
'''
print(isimler[1:6:2]) #1. 3. 5. indexleri bastırır. yani çağtay musa mehmet
print(isimler[6:0:-2]) #6. 4. 2. indexleri bastırır. yani hande serap çağrı
"""
"""
isimler = ["taha","çagtay","çağrı","musa","serap","mehmet","hande"]
isimler[1] = "sezen" # 1. indexte bulunnan "çagtay" yerine "sezen" elemanını yerleştirir.
print(isimler)
print(isimler[::2]) #3. argüman adım sayısıdır. ikişer ikişer artar.
print(isimler[::-2]) #sondan başlayarak azalır
print(isimler[4:0:-2]) 
"""
#endregion

#region iki boyutlu listeler
"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][0]) #1.listede (indexi 0) 1.eleman(indexi 0)
"""
"""
for row in matrix:
    for item in row:
        print(item,end=" ")
    print()
"""
#endregion

#region append işlemi
"""
sayilar = [7,11,65,2,9,43,8,7,12,11]
sayilar.append(34) #listenin sonuna ekler.
print(sayilar)
sayilar.append("batu") #diğer programlama dillerinde olan bir özellik değil
"""
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f'''
listemizdeki meyveler : 
{meyveler}''')
meyveler.append("karpuz")
print(f'''
listemizdeki meyveler son hali: 
{meyveler}
''')
"""
#endregion

#region insert
'''
istediğimiz bir indexe eleman ekler
'''
'''
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f"listemizdeki meyveler : {meyveler}")
meyveler.insert(2,"portakal") #2. indexe elemanı ekler diğer elemanları kaydırır.
#insert(int,eleman)
rint(f"listemizdeki meyveler : {meyveler}")
'''
"""
sayilar = [7,11,65,2,9,43,8,7,12,11]
print(f'''
listenin ,ilk hali
{sayilar}''')
sayilar.insert(2,"dokuz")
sayilar.insert(3,9)
'''
listenin 2. indexine "dokuz"
listenin 3. indexine 9 eklenir.
'''
print(f'''
listenin ,son hali
{sayilar}''')
"""
#endregion

#region remove
'''
listeden içine yazılan elemanı siler.
listede olmayan bir eleman değeri girersek hata alırız.
'''
"""
meyveler = ["elma","armut","muz","ayva,","üzüm"]
print(f'''
listemizdeki meyveler ilk hal:
 {meyveler}
 ''')
meyveler.remove("muz") #listede olmayan bir eleman girersek hata verir.
print(f'''
listemizdeki meyveler son hal: 
{meyveler}
''')
"""
"""
sayilar = [1,5,67,4,23,98,12,67]
sayilar.remove(67) #ilk bulduğu 67 değerini siler
print(sayilar)
sayilar.append(67) #slistenin sonuna ekler
print(sayilar)
sayilar.remove(5) #5 elemanını siler.
print(sayilar)
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

#region count
'''
count(x) listemizde x değerinden kaç adet olduğunu bize döndürür.
'''
"""
listeRakamlar = [2,5,6,1,9,7,5]
arananEleman = 5
elemanAdedi = listeRakamlar.count(5)
print(f"listemizde {arananEleman} sayısından  {elemanAdedi} adet var.")
"""
#endregion

#region sort reverse
'''
sort küçükten büyüğe sıralar
reverse büyükten küçüğe sıralar
'''
"""
listeRakamlar = [2,5,6,1,9,7,5]
print(f"listenin ilk hali -> {listeRakamlar}")
listeRakamlar.sort()
print(f"listenin son hali -> {listeRakamlar}")
listeRakamlar.reverse()
print(f"listenin son hali -> {listeRakamlar}")
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
meyveler.append("ahududu")
print(meyveler) #ahududu eklenmiştin
print(meyveTabagi) #kopyada bir değişiklik olmamıştır.
print(type(meyveTabagi))
del meyveler
print(meyveTabagi)
"""
'''
Copy yerine direk liste olarak atama yaparsak steak heap konusu devreye girer.
eğer listenin karşısına copy yerine başka liste atasaydık aynı adrese kaydolacakları için ileride 
yapacağımız değişiklikler her iki isimdeki listeyi de etkileyecekti.
'''
#endregion

#region index
"""
listeRakamlar = [2,5,6,1,9,7,5]
print(f"listenin ilk hali -> {listeRakamlar}")
print(listeRakamlar.index(7)) #7. indexteki elelmanı döndürür.
print(f"listenin son hali -> {listeRakamlar}")
"""
#endregion

#region len
"""
liste = [1 , 2 , 3 , 4 , 5]
del liste[-1]
print(liste)
del liste[(len(liste)-1)]
print(liste)
"""
#endregion

#region örnek 1
"""
sayilar = []
while True:
    sayi = input("Lİsteye sayı ekleyiniz: ")
    if sayi == "":
        break
    sayilar.append(int(sayi))
print(sayilar)                        
if len(sayilar) > 1:
    temp = sayilar[0] # ilk elemanı temp değişkenine atar. 
    sayilar[0] = sayilar[-1] # son elemanı ilk elemanın indeksine atar.
    sayilar[-1] = temp #son elemana tempte sakladığımız ilk elemanın değerini atar.
    print(sayilar)                      
"""
#endregion

#region örnek artık yıl
"""
def artikYil(yıl) -> bool:
    if yıl % 4 == 0: 
        if yıl % 100 == 0: 
            if yıl % 400 == 0:
                return True
        else:
            return True
    return False

for yıl in range(2020,1900,-1):
    if artikYil(yıl):
        print(f"{yıl} artık yılı")
"""
#endregion
