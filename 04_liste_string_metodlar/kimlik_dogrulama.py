'''
1- 1. 3. 5. 7. 9. hanelerin toplamını  7 ile çarp
2- 1. işlemde çıkan sonucu, 2. 4. 6. 8. hanelerin toplamından çıkart
3. 2. işlemde çıkan sonuç 10a bölündüğünde  bize 10. haneyi veriyorsa 
bu tc doğrudur.
ayrıca;
4- 1den 10. hanneye kadar olan rakamların toplamının 10'a bölümü 
11. haneyi vermelidir.
'''
def tcdogrula(tckimliknumarasi: str) -> bool:
    tekhanelerintoplami = 0
    cifthanelerintoplami = 0
    sayilarinToplami = 0
    i=1
    for hane in tckimliknumarasi:
        sayilarinToplami += int(hane)
        if i >9:
            break
        if i % 2 == 0:
            cifthanelerintoplami += int(hane)
        else:
            tekhanelerintoplami += int(hane)
        i += 1
    if (tekhanelerintoplami*7 - cifthanelerintoplami) % 10 == int(tckimliknumarasi[9]) \
        and sayilarinToplami % 10 == int(tckimliknumarasi[10]):
        return True
    return False

kimlik = input("kimlik numarasını sorgulatın: ")
if  tcdogrula(kimlik) is True:
    print("Tc kimlik numarası doğru!")
else:
    print("Kimlik bulunamadı!!!")