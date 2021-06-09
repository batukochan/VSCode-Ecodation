# region class - nesne kavramı

# class tanımlma

class a1:
    pass


class a2():
    pass


class a3(object):
    pass

# class tanımlama türleri
# ------class------
class Insan:
    ad = ""
    soyad = ""
# ------nesne------
i1 = Insan() 
i1.ad = "ali"
i1.soyad = "koç"
# print(i1.ad,i1.soyad)


# örnek

class Ogrenci:
    adSoyad = ""
    not1 = 0
    not2 = 0

o1 = Ogrenci()
o1.adSoyad = input("Öğrenci adı ve soyadı: ")
o1.not1 =int(input("Öğrenci not1: "))
o1.not2 =int(input("Öğrenci not2: "))

ortalama = (o1.not1 + o1.not2) / 2
print(ortalama)


