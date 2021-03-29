#region örnek
"""
toplam=0
say=0
while True:
    a=int(input("lürfen sayı giriniz, çıkmak için -1 giriniz: "))
    if a==-1:
        break
    elif a%2==0:
        print("çift sayı girmeyiniz.")
        continue
    elif a%2!=0:
        toplam+=a
        say+=1   
ort=toplam/say
print(f"girilen {say} adet tek sayının ortalaması {ort}")
"""
#endregion

#region örnek1

'''
menü olacak 
seçim yapılacak
çıkmak için 3e basacağız
'''
'''
while True:
    secim=int(input("""
[1] km->mil
[2] mil->km
[3] çık
"""))
    if secim==1:
        km=float(input("Km: "))
        mil=km*0.62137
        print(f"{km:^5} km = {round((mil),2):^5} mil")
    elif secim==2:
        mil=float(input("mil: "))
        km=mil/0.62137
        print(f"{mil:^5} km = {round((km),2):^5} mil")
    elif secim==3:
        print("[program sonlandı...]")
        break
    else:
        print("hatalı seçim")
'''
#endregion