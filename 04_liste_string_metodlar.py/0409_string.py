#region giriş
"""
ad = "batuhan"
print(ad[0]) #0. indexte yer alan b harfini bastırır.
"""
#endregion 

# region string_iterable_giris
"""
ad = "BATUHAN"
print(ad[2]) #T
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
print(meyveler[3]) #ayva
kurum = "Flux"
print(kurum[3]) #x
"""
# endregion

#region sesli sessiz harf
""" 
meyveler = ["elma","armut","muz","ayva","üzüm","elma"]
print(meyveler[1])
"""
"""
ad = "batuhan"
sesliHarf = ['a','e','o','u','ö','ü','ı','i']
for i in range(0,len(ad)):
    if ad[i] not in sesliHarf:
        print(ad[i],end="")
"""
#endregion

# region ismi_tersten_yazma_ornegi
"""
ad = "BATUHAN"
for i in range(len(ad)-1, -1, -1):
    print(ad[i], end= " ")
"""
# endregion