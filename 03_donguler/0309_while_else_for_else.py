'''
while döngüsü break satırı çalışmadan biterse, else içerisine girer.
Eğer break satırı çalışarak girerse, else içerisine girmez.
'''
#region while else
"""
i=1
while i<=10:
    print(i)
    i+=1
    if i==2:
        continue
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
"""
for i in range(10,0,-1):
    print(i,end=" ")
    if i==9:
        pass #break kullanırsak else bloğuna girmez
else:
    print("şuan for else yapısındayım")
print("buradayım")
"""

#endregion

