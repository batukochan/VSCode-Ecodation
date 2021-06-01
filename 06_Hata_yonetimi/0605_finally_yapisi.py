# region

def bolme(x, y):

    try:
        result = x/y

    except ZeroDivisionError as z:
        print(z)
    else:
        print(result)
    finally:
        print("işlem tamamlandı")


"""
bolme(5,0)
bolme(5,3)
"""


def dosyaAc1(file):

    try:
        dosya = open(file, encoding='utf-8')

    except Exception as ex:
        print(ex)

    else:
        print(dosya.read())
    finally:
        try:
            dosya.close()
        except:
            pass

# dosyaAc1('kelimeler.txt')