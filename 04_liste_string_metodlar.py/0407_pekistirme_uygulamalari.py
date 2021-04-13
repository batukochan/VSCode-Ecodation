# region sıralamna
"""
listem = [7, 9, 5, 1, 3]
siraliMi = False
while not siraliMi:  # SIRALIMI TRUE DEĞİLSE
    siraliMi = True
    for i in range(len(listem)-1):
        if listem[i] > listem[i+1]:
            listem[i] , listem[i+1] = listem[i+1],listem[i]
            siraliMi = False
print(listem)
"""   
#endregion
 
#region
"""

birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","60","yetmiş","seksen","doksan"]
yuzler = ["","yüz","iki yüz","üç yüz","dört yüz","beş yüz","altı yüz","yedi yüz","sekiz yüz","dokuz yüz"]

kullanicidenAlinanSayi = int(input("3 basamaklı bir sayı giriniz: "))
donusturulenSayi= str(kullanicidenAlinanSayi)

print(f"{yuzler[int(donusturulenSayi[-3])]} {onlar[int(donusturulenSayi[-2])]} {birler[int(donusturulenSayi[-1])]}")
"""
"""
birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","60","yetmiş","seksen","doksan"]
yuzler = ["","yüz","iki yüz","üç yüz","dört yüz","beş yüz","altı yüz","yedi yüz","sekiz yüz","dokuz yüz"]

# 123 -> 1 2 3 
"""
#endregion

#Rregion sıralama
"""
listem = [9, 7, 5, 1, 3, 4, 2, 6, 8]
while True:
    sirali = True
    for i in range(len(listem)-1):
        if listem[i]>listem[i+1]:
            listem[i], listem[i+1] = listem[i+1], listem[i]
            sirali = False
    if sirali:
        break
print(listem)
"""
"""
listem = [9, 7, 5, 1, 3, 4, 2, 6, 8]
listem.sort()
print(listem)
listem.sort(reverse = True)
print(listem)
"""
#endregion