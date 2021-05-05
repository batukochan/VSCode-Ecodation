#region
"""
eb=-9999999
sayi=int(input("Sayı giriniz, çıkmak için -1 : "))
while sayi!=-1:
    if sayi>eb:
        eb=sayi
    sayi=int(input("Sayı giriniz, çıkmak için -1 : "))
print(f"Girilen sayıların en büyüğü {eb}")
"""
#endregion

#region

''' teklerin adedi çiftlerin adedi'''
'''çıkmak için 0'''
"""
sayi=int(input("lsg: "))
tek,cift=0,0
while sayi!=0:
    sayi=int(input("lsg: "))
    if sayi%2==0:
        cift+=1
    else:
        tek+=1
print(f"girilen sayılardan {tek} tanesi tek , {cift} tanesi çift sayıdır.")
"""
#endregion

#region 
'''
sayi=1
tek,cift=0,0
print("çıkmak için 0 giriniz...")
while sayi!=0:
    sayi=int(input("Lütfen sayı giriniz, : "))
    if sayi%2==0:
        cift+=sayi
    else:
        tek+=sayi
print(f"teklerin toplamı {tek}  ,çiftlerin toplamı {cift} ")
'''
#endregion