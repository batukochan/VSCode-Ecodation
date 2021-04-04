#region rastgele sayı

import random
i=0
sayi=random.randint(1,10)
while i<300:
    a=int(input("1 ile 10 arasındaki sayıyı tahmin ediniz : "))
    i+=1
    if a==sayi:
        print(f"Tebrikler {i}. denemede buldunuz.")
        tercih=int(input("Devam etmek için 1'e, uygulamadn çıkmak içim 2'ye dokunun : "))
        if tercih==1:
            pass
            i=0
            sayi=random.randint(1,10)
        else:
            print("Şanslı günler dileriz")
            break
        
#endregion