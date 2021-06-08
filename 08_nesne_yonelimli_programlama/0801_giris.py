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
print(i1.ad,i1.soyad)

