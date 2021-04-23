#region Ktü harf notu hesaplama
"""
45<not60    DC
60<not<70   CC
70<not<75   CB
75<not<80   BB
80<not<90   BA
90<not<100  AA
"""
print("***KTÜ HARF NOTU SİTESİNE HOŞGELDİNİZ***")
vizeNotu=int(input("Lütfen vize notunuzu giriniz :\t "))
finalNotu=int(input("Lütfen final notunuzu giriniz :\t "))
ort= vizeNotu*0.4 + finalNotu*0.6
if finalNotu<45:
    print("Ortlamanız : {} Bütünleme sınavında başarılar dileriz...".format(round(ort,2)))
else:
    pass
    if 45<=ort<60:
        print("Tebrikler Vize-Final ortalamanız : {}\nHarf notunuz : DC\n\"Dönem ortalamanız 2.0'ın üzerindeyse şartlı geçtiniz...\"".format(ort))
    elif 60<=ort<70:
        print("Vize-Final ortalamanız : {}\nHarf notunuz : CC".format(round(ort,2)))
    elif ort<45:
        print("Ortlamanız : {}, Bütünleme sınavında başarılar dileriz...".format(round(ort,2)))
    elif 70<=ort<75:
        print("Vize-Final ortalamanız : {}\nHarf notunuz : CB".format(round(ort,2)))
    elif 75<=ort<80:
        print("Vize-Final ortalamanız : {}\nHarf notunuz : BB".format(round(ort,2)))
    elif 80<=ort<90:
        print("Vize-Final ortalamanız : {}\nHarf notunuz : BA".format(round(ort,2)))
    elif 90<=ort<100:
        print("Vize-Final ortalamanız : {}\nHarf notunuz : AA".format(round(ort,2)))
    else:
        pass

#endregion