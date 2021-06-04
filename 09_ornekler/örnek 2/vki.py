
kilo=float(input("Kilonuzu giriniz: "))
boy=float(input("Boyunuz(m): "))
idealkilo = float(24.5*(boy**2))
vki=kilo/boy**2
fark = round((kilo-idealkilo),2)
print(f"Vücut kitle index'iniz {(round(vki,2))}")
print("Vki analiz ediliyor...")
if vki <=18.5:
    print(f'''
    Sağlığınız için {(-fark)} kilo almanız gerekiyor''')
elif vki <=24.9:
    print("İdeal kilodasınız.")
else:
    print(f'''
    Sağlığınız için {(fark)} kilo vermeniz gerekiyor''')
