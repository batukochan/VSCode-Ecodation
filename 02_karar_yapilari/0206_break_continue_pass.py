#region break
"""
harfler = ["a","b","c","d","e"]
for index,harf in enumerate(harfler):
    if harf == "c":
        print(f"{harf} harfi  {index} numaralı indexte")
        break
"""
#endregion

#region continue
"""
for sayi in range(1,15):
    if sayi % 2 == 0:
        continue
    print(sayi,end="  ")
"""
"""
for sayi in range(1,15):
    if sayi % 2 != 0:
        print(sayi,end="  ")
"""
#endregion

#region pass
"""
sayi=7
if sayi < 5 :
    pass
else:
    print("hey")
"""