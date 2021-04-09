def userName():
    harfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        kAdi = input('''
        Lütfen geçerli bir kullanıcı adı giriniz.
        (Sadece harflerden oluşmalı, max 8 karakter)
        Kullanıcı Adı: ''')
        a = 0
        boyut = len(kAdi) # print(boyut) örn: 7
        for harf in kAdi:
            if harf  in harfler:
                #geçerli bir kullanıcı adı
                a += 1
        if boyut == a and boyut <= 8:
            print('''
        Kullanıcı adı geçerli
            ''')
            break
    return kAdi



def password():
    rakamlar = "0123456789"
    while True:
        sifre = input('''
        Lütfen geçerli bir şifre giriniz.
        (Sadece rakamladan oluşmalı, min 6 karakter)
        şifre ''')
        a = 0
        boyut = len(sifre) # print(boyut) örn: 7
        for rakam in sifre:
            if rakam  in rakamlar:
                #geçerli bir SİFRE
                a += 1
        if boyut == a and boyut >= 6:
            print('''
        Şifreniz geçerli
            ''')
            break
    return sifre

    