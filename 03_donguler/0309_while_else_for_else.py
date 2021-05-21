'''
while döngüsü break satırı çalışmadan biterse, else içerisine girer.
Eğer break satırı çalışarak girerse, else içerisine girmez.
'''
#region while else
"""
i=1
while i<=10:
    print(i,end=" ")
    if i==2:
        pass
    i += 1 
else:
    print("Şuan else içerisine girdim.")
print("While döngüsü bitti")
"""
#endregion

#region for else

'''
for döngüsü break satırı çalışmadan biterse, else içerisine girer.
Eğer break satırı çalışarak girerse, else içerisine girmez.
'''

for i in range(10,0,-1):
    print(i,end=" ")
    
    if i==9:
        continue #break kullanırsak else bloğuna girmez
else:
    print()
    print("şuan for else yapısındayım")
    
print("buradayım")


#endregion

#region orderId
"""
searchId = 11069 # örnek olarak -1 girseydik else bloğuna girecekti.
for orderId in range(1,100000):
    if orderId == searchId:
        print(f"{orderId} nolu sipariş için detay listesi")
        break
else:
    print(f"{orderId} nolu sipariş için kayıt bulunamadı")
"""
#endregion

