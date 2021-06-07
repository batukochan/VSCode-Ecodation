def tamSayiAl():
    """         
    Kullanıcıdan tam sayı alana kadar devam eder.
    """
    while True:
        try:
            girdi = girdiİste("tam sayı")
            sayi = int(girdi)
        except ValueError:
            continue
        else:
            return sayi