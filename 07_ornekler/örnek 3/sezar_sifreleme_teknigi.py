#region sezar şifre
metin = "Python"
parola = ""
for i in metin:
    print(ord(i)) #ASCII kodlarını döndürür.,
    print(i," => ",chr(ord(i)+5))
    parola = parola + chr(ord(i)+5)
print(metin,parola)
#endregion