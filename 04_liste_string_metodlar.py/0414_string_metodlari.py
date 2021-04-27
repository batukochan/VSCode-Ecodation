# region string_metodlari
"""
upper() lower() title() capatilize()
count() replace()   swapcase()
startswith()    endswith()
strip() lstrip()    rstrip()
isdigit()   isalpha()
isalphanum()    isspace()   istitle()   isidentifier()
split() index() format()
"""
# endregion

# region object
"""
#object
print(type(3))
kurum = "Flux Mimarlık "
boy = 184
"""
# endregion

# region upper
"""
'''her karakteri büyük harfe çevirir'''
kurum = "Flux Mimarlık"
print(kurum.upper())
"""
# endregion

# region lower
"""
küçük harfe çevirir
kurum = "Ecodation Eğitim Kurumları"
print(kurum.lower())
while True:
    yas = input("yaş giriniz, çıkmak için ç ")
    if yas.lower()=="ç":
        break
"""
# endregion

# region title
"""
'''tüm kelimelerin yalnızca ilk harfleri büyük yazılır.'''
kurum = "flux mimarlık ofisi"
print(kurum.title())
"""
# endregion

# region capitalize
"""
'''sadece ilk harf büyük, diğer tüm harfler küçük yazılır.'''
kurum = "Flux Mimarlık Ofisi"
print(kurum.capitalize())
"""
# endregion

# region count
"""
'''parametrede belirttiğim harf, kelime string içinde kaç tane geçtiğini bulur.'''
kurum = "Flux Mimarlık ofisi"
print(kurum.count(("z"))) #verinin tamamında 'z' arar.
# çıktımız → 0
print(kurum.count("a", 6, 8)) #6.-8. index arasında 'a' arar. 8 dahil değil
# çıktımız → 0
print(kurum.count("a", 6, 9)) #6.-8. index arasında 'a' arar. 9 dahil değil
# çıktımız → 1
"""
# endregion

# region replace

"""
'''bir metni, başka bir metin ile değiştirir.'''
url = "http://www.flux.com.tr"
url.replace("com.tr", "edu.tr") 
'''Ramde anlık olarak değişir ancak url değişkenini çağırırsak orjinal metin basılır'''
print(url) #orjinal halini basar
url = url.replace("com.tr", "edu.tr")
print(url)
yorum = "bu kelime sansürlenecek"
print(yorum.replace("sansürlenecek", "..."))
print(yorum)
"""

# endregion

# region swapcase
"""
'''
Büyük karakterler küçük, küçük karakterler büyük olacak.
'''
kurum  = "Türk Dil Kurumu"
print(kurum)
print(kurum.swapcase())
"""
# endregion

# region endswith
"""
'''
endswith; eğer parametre ile belirttiğiniz haliyle bitiyorsa True, 
aksi takdirde False değeri döndürür.
'''
url = "http://www.flux.com.tr"
print(url.endswith("com.tr"))
'''bu yapıyı karar işlemlerimizde kullanabilir'''
"""
# endregion

# region startswith
"""
'''startswith; eğer parametre ile belirttiğiniz haliyle başlıyorsa True, 
aksi takdirde False değeri döndürür.'''
url = "http://www.flux.com.tr"
print(url.startswith("http"))
print(url[0:4]=="http")
"""
# endregion

# region strip
"""
'''strip; ile başındaki sonundaki boşlukları almayı başaracağız.'''
kurum  = "        Flux Mimarlık Ofisi         "
print(kurum)
print(kurum.strip())
"""
# endregion

# region lstrip
"""
'''lstrip; string değerin başındaki boşlukları alır.'''
kurum  = "        Flux Mimarlık Ofisi"
print(kurum)
print(kurum.lstrip())
"""
# endregion

# region rstrip
"""
rstrip; string değerin sonundaki boşlukları alır.
kurum  = "Flux Mimarlık Ofisi       "
print(kurum)
print(kurum.rstrip())
"""
# endregion

# region isdigit
"""
'''rakam olup/olmadığını geriye döndürür. 
Eğer değer bir sayı ise, tüm rakamlarını kontrol ederek 
True/False geriye döndürecek.'''
deger = "1"
print(deger.isdigit())
deger = "1060"
deger = "_1060"
print(deger.isdigit())
sayi = int(input("lütfen s. giriniz: "))
"""
# endregion

# region isalpha
"""
'''hepsi harf ise True, değilse False döner. Girilen değerlerin harf olup olmadığını sorgular.'''
deger = "nciS3ınıf" #içerisinde sayısal değer barındırmamalı, barındırırsa false döner.
print(deger.isalpha())
"""
# endregion

# region isalnum
"""
'''alfanumerik ise True, değilse False döner.'''
deger = "12nciSınıf" #a-z,A-Z,0-9 içerebilir.
print(deger.isalnum())
"""
# endregion

# region isupper
"""
'''tamamı büyük karakterlerden mi oluşuyor? '''
kurum = "FLUX"
print(kurum.isupper())
"""
# endregion

# region islower
"""
'''tamamı küçük karakterlerden mi oluşuyor? '''
kurum = "fLuX"
print(kurum.islower())
"""
# endregion

# region isspace
"""
'''tamamı space mi doğrulamak için kullanılır.'''
kurum = "     "
print(kurum.isspace())
"""
# endregion

# region istitle
"""
'''ilk harfleri büyük mü doğrulamak için kullanılır. '''
deger = "Flux"
print(deger.istitle())
"""
# endregion

# region isidentifier
"""
'''parametre ile belirtilen değer, değişken ismi olur mu olmaz mı doğrulamak için kullanılır.'''
deger = "_1Sayi"
print(deger.isidentifier())
"""
# endregion

# region split
"""
kurum  = "Flux Mimarlık Ofisi"
print(kurum.split())
kurum1  = "Flux Mimarlık Ofisi ile Geleceğin Yapılarını Tasarla "
print(kurum1.split("."))
cumleSayisi = len(kurum1.split("."))
print(cumleSayisi)
kurum  = "Flux Mimarlık Ofisi ile Geleceğin Yapılarını Tasarla"
listem = [i for i in kurum.split(" ")]
listem = [i for i in kurum.split(".")]
print(listem)
"""
# endregion

# region ic_ice_kullanim
"""
kurum  = "Flux Mimarlık Ofisi"
print(len(kurum.lower().upper().title().replace("i", "ı")))
"""
# endregion

# region ornek
"""
kotuKelimeler = ["yuh", "tüh"]
yorum  = "Bu laptop'u geçtiğimiz aylarda aldım. Aldığıma bin pişmanım. Satıcıya yuh sana diyorum."
kelimeler =[i.rstrip(".") for i in yorum.split(" ")]
for item in kotuKelimeler:
    if item in kelimeler:
        yorum = yorum.replace(item, "...")
print(yorum)
"""
# endregion