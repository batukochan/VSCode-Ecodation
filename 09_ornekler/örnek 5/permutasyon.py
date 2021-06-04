'''
    Soru: Permütasyon nesnelerin diziliş sayısını bulmamızı sağlar. 6 
arkadaştan 4’ü masaya oturucaktır. Bu 4 kişi kaç farklı şekilde masaya 
oturabilir. Sorunun çözümünü bulmak için permütasyon kullanırız. Aldığı 
sayılara göre permütasyon hesabı yapan kodu yazınız.
'''
'''
n → asıl kümedeki eleman sayısı
r → alt kümelerin eleman sayısı
P(6,4)
'''

def faktoriyel(a):
    for i in range(1,a):
        a *= i
    return a

def permutasyon(n,r):
    sonuc = faktoriyel(n)/faktoriyel(n-r)
    print(sonuc)

permutasyon(6,4)


