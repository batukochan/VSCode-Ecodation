'''
break-> dmöngüyü sonlandırır
continue-> tepeye geri döner
'''

#region break continue
"""
i=1
print("a")
while i<11:
    if i%4==0:
        break
    print(f"{i}. döngüdeyim.")
    i+=1
print("b")
"""
#endregion

#region continue
"""
i=1
print("a")
while i<100:
    if i%7==0:
        i+=1
        continue
    elif i%15==0:
        break
    print(f"{i}. döngüdeyim.")
    i+=1
print("b")
"""
#endregion

#region örnek
"""
eb = 0
say=0
while True:
    sayi=int(input("Lütfen bir sayı giriniz, çıkmak için -1: "))
    if sayi==-1 and say==0:
        print("hiçbir sayı girmediniz")
        continue
    elif sayi==-1:
        break
    elif sayi>eb:
        eb=sayi
    say=say+1
print(f"listedeki en büyük sayı: {eb}")
"""
#endregion







