'''
Palidrom nedir ? 
- Palindrom, normal okunuşu ile tersten okunuşu aynı olan sözcük ve sayılara denilmektedir
örnek: nazan ,radar, 696
'''
"""
def palidromMu(sozcuk: str) -> bool:
    tersSozcuk = sozcuk[::-1]
    if sozcuk == tersSozcuk:
        print("Palidrom")
    else:
        print("palidrom değil")

palidromMu("ahmet")
"""