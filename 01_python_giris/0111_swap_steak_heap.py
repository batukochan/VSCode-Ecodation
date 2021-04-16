#region Using a temporary variable
"""
a = 12
b = 34 
temp = a
# a = 12 | b = 34 | temp = 12 
a = b # a = 34
b = temp # b = 12

print(a,b)
# Çıktımız → 34 12
"""
#endregion

#region 
"""
deger1 = 45
deger2 = 38
deger1, deger2 = deger2, deger1

print("değer1 = ",deger1," değer2 = ",deger2)
# Çıktımız → değer1 =  38  değer2 =  45
"""
#endregion

#region
"""
isim1 = "Şule"
isim2 = "Deniz"
isim1,isim2 = isim2, isim1
print("isim1 = ",isim1," isim2 = ",isim2)
# Çıktımız →  isim1 =  Deniz  isim2 =  Şule
"""
#endregion
  
#region ram_steak_heap
"""
a = 5
b = 10
a = b
b = 5
print("a = ",a," b = ",b)
# Çıktımız → a =  10  b =  5
"""
#endregion
