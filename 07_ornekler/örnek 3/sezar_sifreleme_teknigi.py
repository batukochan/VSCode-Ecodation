#region sezar şifre
"""
metin = "Merhaba Dünya""
parola = ""
for i in metin:
    print(ord(i)) #ASCII kodlarını döndürür.,
    print(i," => ",chr(ord(i)+5))
    parola = parola + chr(ord(i)+5)
print(metin,parola)
"""
#endregion

#region sezar şifreyi çözme
"""
metin = ""
parola ="Rjwmfgf%Iās~f" 
for i in parola:
    print(ord(i)) #ASCII kodlarını döndürür.,
    print(i," => ",chr(ord(i)-5))
    metin = metin + chr(ord(i)-5)
print(parola,metin)
"""
#endregion