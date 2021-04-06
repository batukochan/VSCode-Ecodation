#region yer değiştirme
"""
listem = [1,2,3,4,5,6]
listem[2] = listem[3] #3 4 oldu
listem[3] = listem[2] # 4 de 4 oldu
print(listem)

"""
"""
listem = [1,2,3,4,5,6]
temp = listem[2]
listem[2] = listem[3] #3 4 oldu
listem[3] = temp # 4 de 3 oldu
print(listem)
"""
'''En basit hali'''
"""
listem = [1,2,3,4,5,6]
listem[2],listem[3] = listem[3],listem[2]
print(listem)
"""
#endregion

#region slice
'''
listedeki elemanların belli bir kısmını geri çağırmak için kullanırız.
'''
"""
liste = ["a1","a2","a3"]
print("www.azizbektas.com"[-3:])
ad="batuhan" #iterable
print(ad[1])
"""
"""
print("www.azizbektas.com"[0:3])
print("www.azizbektas.com"[0:8])
print("www.azizbektas.com"[-3:])
print("www.azizbektas.com"[:]) #tüm listeyi verir
print("www.azizbektas.com"[0:3:2])
"""
#endregion

#region slice örnek 
'''
url = input("LÜtfen site adı giriniz: ")
if url[-3:] != "com" or not url[1:3]:
    print("""
    format hatası
    (www.buformatta.com)
    """)
else:
    print(f"İnternet adresi -> {url}")
'''
#endregion

#region örnek




