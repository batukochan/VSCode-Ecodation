# for-while

#region in operatörü
"""
print(5 in  [1,2,3,4,5])
print(5 in (1,2,3,4))
print(5 in (1,2,3,4,5))
"""
#endregion

#region for eleman in veritipi
"""
liste=[1,2,3,4,5,6,7]
toplam=0
for eleman in liste:
    print("eleman",eleman)
    toplam+=eleman
print(toplam)
"""
#endregion

#region (i,j,k)
"""
liste=[(2,3),(3,5),(5,2),(3,5)]

for (i,j) in liste:
    print(f"i={i},j={j}")
"""
#endregion

#region Sözlüklerde dolaşmak
"""
sozluk={"bir":1,"iki":2,"üç":3,"dört":4}
for i in sozluk:
    print(i)

sozluk={"bir":1,"iki":2,"üç":3,"dört":4}
for i in sozluk.keys():
    print(i)

sozluk={"bir":1,"iki":2,"üç":3,"dört":4}
for i in sozluk.values():
    print(i)

sozluk={"bir":1,"iki":2,"üç":3,"dört":4}
for i,j in sozluk.items():
    print(i,j)
"""
#endregion

#region While döngüsü
"""
i=0
while i<10:
    print("i sayısının değeri",i)
    i+=1

liste=[1,2,3,4,5]
i=0
while i<len(liste):
    print("i",i)
    i+=1
"""
#endregion

#region range
"""
print(*range(0,20))
print(*range(20))
print(*range(0,20,2))
print(*range(100,0,-4))
print(*range(20,0,1)) #bir şey yazmaz
print(*range(20,0)) #bir şey yazmaz

for i in range(0,10):
    print(i)

for i in range(1,10):
    print("."*i)
    
"""

#endregion

#region list Comprehension

''' Listelerdeki append methodu'''
"""
liste=[1,2,3,4,5,6]
liste.append(7) #son indexe 7yi ekler.
print(liste)


liste1=[1,2,3,4,5]
liste2=list()

for i in liste1:
    liste2.append(i)
print(liste2)


liste=[1,2,3,4,5]
liste2=[i for i in liste]
print(liste2)


liste=[1,2,3]
liste2=[i*2 for i in liste]
print(liste2)

liste=[(1,2),(3,2),(4,5)]
liste2=[(i,k) for i,k in liste]
print(liste2)

liste=[(1,2),(3,2),(4,5)]
liste2=[(i*k) for i,k in liste]
print(liste2)

s = "Python"
liste=[i*3 for i in s]
print(liste)

liste=[(1,2,4),(1,4,6),(7,8,11,14,45)]
liste1=[x for i in liste for x in i]
print(liste1)

liste=[(1,2,4),(1,4,6),(7,8,11,14,45)]
liste1=list()

for i in liste:
    for x in i:
        liste1.append(x)
print(liste1)

"""

#kullanıcı bilgisi doğruysa 
#kullanıcı bilgisi 3 kere hatalı girildiyse programı sonlandır.
"""

kAdi="Batukochan"
parol="1234"
girisHakki=3
while 0<girisHakki<=3:
    kullaniciAdi=str(input("Kullanıcı adı : "))
    parola=str(input("Parola : "))
    if kullaniciAdi==kAdi and parola==parol:
        print(f"Merhaba {kullaniciAdi}, sitemize hoş geldiniz.")
        break
    elif kullaniciAdi!=kAdi or parola!=parol and 0<girisHakki<=3:
        girisHakki-=1
else:
    print("Kullanıcı adı ve şifresini 3 kere hatalı girdiniz...")
"""     
#endregion

#region ATM örneği

'''
ATM makinesine Hoş Geldiniz...
1.bakiye sorgu
2.para yatırma
3.para çekme
programdan çıkmak için 0 a basın

'''
'''

parola=input("Lütfen kartınızı yerleştirin ve parolanızı giriniz...")
tercih=0
bakiye=3456.34
if parola=="1889":
    print("Batu Banka Hoş Geldiniz.")
    print("*"*40)
    print("""
            BATU BANK ATM
        ****************

        1-BAKİYE SORGULAMA
        2-PARA YATIRMA
        1-BAŞKA BANKAYA 
        2-BATU BANK KULLANICISINA
        3-PARA ÇEKME
        Kart iadesi için 9'a basınız...
    """)
    print("*"*40)
    tercih=int(input("Yapacağınız işlemi seçiniz: "))
    if tercih==1:
        print("Güncel bakiyeniz : ",bakiye," TL")
    elif tercih==2:
        tercih2=int(input("""
    Batu Bank Hesabı 1
    Başka Bankaya 2   
    Giriş yapınız : """))
        if tercih2==1:
            tutar=int(input("Yatırılacak tutar : "))
            if tutar%5!=0:
                print("Lütfen 5 TL ve katı olan bir tutar yatırınız.")
            else:
                print(f"Güncel Bakiyeniz : {bakiye+tutar} TL")
        if tercih2==2:
            tutar=int(input("""
Yatırılacak tutar : """))
            if tutar%5!=0:
                print("Lütfen 5 TL ve katı olan bir tutar yatırınız.")
            else:
                kesinti=tutar*0.01
                print(f"""
    Güncel Bakiyeniz : {round(((bakiye+tutar)-kesinti),2)} TL
    Kesintiye uğrayan tutar : {round(kesinti,2)} TL
                """)
    elif tercih==3:
        çekme=int(input("""
Tutar : """))          
        if çekme%5!=0:
            print("Lütfen 5 TL ve onun katı olan tutarlar giriniz...")
        else:
            print(f"""
Çekilen tutar : {çekme} TL
Güncel bakiye : {bakiye-çekme} TL
""")
'''
#endregion

#region must atm


'''
print("*"*40)
print("""
BATU BANK ATM
****************

1-BAKİYE SORGULAMA
2-PARA YATIRMA
    1-BAŞKA BANKAYA 
    2-BATU BANK KULLANICISINA
3-PARA ÇEKME
Kart iadesi için 9'a basınız...
""")
print("*"*40)
tercih,bakiye,secim=5,1000,5   
while True:
    tercih=int(input("Yapmak istediğiniz işlemi seçiniz: "))
    if tercih==9:
        break
    elif tercih==1:
        print(f"Güncel bakiyeniz {bakiye}")
    elif tercih==2:
        secim=int(input("Yapmak istediğiniz işlemi seçiniz: "))
        if secim==1:
            tutar=int(input("Yatırılacak tutarı giriniz: "))
            print(f"""
            Gönderilen tutar : {tutar} TL
            Kesilen tutar    : {tutar*0.02} TL
            Güncel bakiye    : {bakiye-(tutar*1.02)} TL
            """)
        elif secim==2:
            tutar=int(input("Yatırılacak tutarı giriniz: "))
            print(f"""
            Gönderilen tutar  : {tutar} TL
            Güncel bakiye     : {bakiye-tutar} TL
            """)
        else:
            print("Farklı bir seçim yaptınız...")
            
    elif tercih==3:
        çtutar=int(input("Çekmek istediğiniz tutarı giriniz: "))
        print(f"Güncel bakiye: {bakiye-çtutar}")
    else:
        print("Farklı bir seçim yaptınız...")
'''       

#endregion

#region faktoriyel
"""
i,fak=1,1
a=int(input("Lütfen x! işleminde x değerini giriniz: "))
while i<a:
    i+=1
    fak*=i
print(f"{a}! = {fak}")
"""
#endregion

#region faktoriyel must
"""
while True:
    a=int(input("x!, x değerini giriniz: "))
    if a<0:
        a=int(a)
        print("Program sonlandı...")
        break

    elif a>=0:
        a=int(a)
        fak=1
        for i in range(2,a+1):
            fak*=i
        print(f"{a}! = {fak}")    
    else :
        print("Program sonlandı...")
        break
""" 
#endregion