#region aritmetik-operatorler
# aritmetik operatörler
"""
1→  +   toplama
2→  -   çıkarma
3→  *   çarpma
4→  /   bölme
5→  //  tam bölme
6→  **  üst alma
7→  %   mod alma
"""
#endregion

#region +/- binary
"""
print(3+3)
print(6-3)
print(3-6)
print(0.15 - 15)
print(.15 - 15)
"""
#endregion

#region +/- unary işaret
""" 
print(+2)
print(-2)
"""
#endregion

#region */ 
'''
print(4*4)
# → 16
print(.4*4)
# → 1.6
print(type(.4*4))
# → <class 'float'>
print(9/3)
# →3.0
print(9/2)
# → 4.5
print(type(9/2))
# → <class 'float'>
print(17/.4)
# → 42.5
'''
"""
print(10/0)
# → ZeroDivisionError: division by zero
"""

#endregion

#region ** üst alma
"""
print(2**4)
# → 16
print(3**3)
# → 27
print(16**0.5) #köklü ifade
# → 4.0
print(16**(1/2)) #köklü ifade
# → 4.0
print(type(16**0.5))
# → <class 'float'>
"""
#endregion

#region // - tam bölme
"""
print(12/7)
# → 1.7142857142857142
print(12//7)
# → 1
print(12//7.)
# → 1.0
print(-13/5)
# → -2.6
print(-12//5) # Önemli -2.4
# → -3
print(-13//5) # Önemli -2.6
# → -3
"""
#endregion

#region % - mod alma - kalanı bulma
"""
print(15%4)
# 15'in 4'e bölümünden kalan  → 3
print(15%2) #***
# 15'in 2'ye bölümünden kalan → 1
print(8%3)
# 8'in 3'e bölümünden kalan   → 1
"""
"""
print(15%0)
#ZeroDivisionError: integer division or modulo by zero
"""
#endregion

#region operator_oncelikleri
"""
1→  +, -        unary
2→  **          üst alma
3→  *, /, %     çarpma, bölme, mod alma
4→  +,-         toplama çıkarma
"""
""""""

#region

print(3+4*5)
# 1.İşlem → 4 * 5 = 20 | 2.İşlem → 3 + 20 = 23 || sonuç → 23

print(15%4*2)   # % left-side 
# 1.İşlem → 15 % 4 = 3 | 2.İşlem → 3 * 2 = 6   || sonuç → 6

print(15%4%2)   # % left-side binding
# 1.İşlem → 15 % 4 = 3 | 2.İşlem → 3 % 2 = 1   || sonuç → 1

print(2**2**3)  # ** right-side binding
# 1.İşlem → 2**3 = 8   | 2.İşlem → 2**8 = 256  | sonuç → 256

#endregion