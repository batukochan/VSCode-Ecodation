#kullanıcı önce kare ya da dikdörtgen seçeneklerinden birini seçecek sonra da alan veya çevre hesabı yapabilecek

print("""
1-kare
2-Dikdörtgen
""")
tercih=int(input("kare için 1 dikdörtgen için 2 seçeneğini ekrana yazdırın : "))
if tercih==1:
    print("""
1-Alan
2-Çevre
""")
    tercih2=int(input("Alan hesaplamak için 1 , Çevre hesaplamak için 2 seçeneğini ekrana yazdırın : "))
    if tercih2==1:
        kisaKenar=float(input("Lütfen kenar uzunluğunu giriniz : "))
        print(f"{kisaKenar} metre kenar uzunluğuna sahip olan karenin alanı {kisaKenar*kisaKenar} metrekaredir.")
    elif tercih2==2:
        kisaKenar=float(input("Lütfen kenar uzunluğunu giriniz : "))
        print(f"{kisaKenar} metre kenar uzunluğuna sahip olan karenin çevresi {4*kisaKenar} metredir.")
    else:
        print("""geçersiz tercih yaptınız.
-Geçerli tercihler ;
-Alan hesabı için 1
-Çevre hesabı yapmak için 2
""")
if tercih==2:
    print("""
1-Alan
2-Çevre
""")
    tercih2=int(input("Alan hesaplamak için 1 , Çevre hesaplamak için 2 seçeneğini ekrana yazdırın : "))
    if tercih2==1:
        kisaKenar=float(input("Lütfen kısa kenar uzunluğunu giriniz : "))
        uzunKenar=float(input("Lütfen uzun kenar uzunluğunu giriniz : "))
        print(f""""
Kısa kenarı {kisaKenar} metre 
Uzun kenarı {uzunKenar} metre
Parametrelerine sahip dikdörtgenin alanı {kisaKenar*uzunKenar} metrekaredir.""")
    elif tercih2==2:
        kisaKenar=float(input("Lütfen kısa kenar uzunluğunu giriniz : "))
        uzunKenar=float(input("Lütfen uzun kenar uzunluğunu giriniz : "))
        print(f"""
Kısa kenarı {kisaKenar} metre 
Uzun kenarı {uzunKenar} metre 
Parametrelerine sahip dikdörtgenin çevresi {2*kisaKenar + 2*uzunKenar} metredir.""")
    else:
        print("""geçersiz tercih yaptınız""")