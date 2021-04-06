#region 0-9999 arası sayıları yazıya çevirme
"""
degerler =[
["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"],
["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"],
["","yüz","iki yüz","üç yüz","dört yüz","beş yüz","altı yüz","yedi yüz","sekiz yüz","dokuz yüz"],
["","bin","iki bin","üç bin","dört bin","beş bin","altı bin","yedi bin","sekiz bin","dokuz bin"]
]
kullanicidenAlinanSayi = input("0-999 arası bir sayı giriniz: ") #427
donusturulenSayi= list(kullanicidenAlinanSayi) # [4,2,7] [0,1,2](index)
i ,j= -1,int(len(donusturulenSayi)) #3
for basamak in range(int(len(donusturulenSayi)-1),-1,-1): #2,1,0
    i += 1 # donüştürülen sayının indexini bulmak için kullanıldı.
    j -= 1 # değerler listesin içindeki listeye erişmek için kullanıldı.
    for deger in degerler : #degerler listesinde dolaşacak
        print(f"{degerler[j][int(donusturulenSayi[i])]}",end=" ")
        break
""" 
#endregion 