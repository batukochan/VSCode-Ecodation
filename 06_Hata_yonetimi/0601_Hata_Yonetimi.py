# region Exception ile syntax error farkı

"""
Bir python programı hata ile karşılaştığında durur.
Bu hata durdruma işleminin nasıl olacağına Exception Handling denir. (Hata Yönetim)
Python'da error iki türlü alınır.
1 - Syntax Error ( yazım hatası )
2 - Exception ( Uygulama Hatası )
"""

"""
Syntax Error ( Söz Dizimi Hatası )

Python Parser'ı (kod oluşturucu), yazım şekli python kurallarına uymadığı durumlarda
'SyntaxError' oluşturur.
"""

# Not : ctrl + ö yorumsatırı oluşturur.

"""
Exception, syntax'ı doğru olan ancak python interpreter'ın çalışırken (run time) anında
aldığı hatalardır.
"""

# örnek 1
"""
a = 7/0
# print(a)
# ZeroDivisionError: division by zero
"""

# örnek 2
"""
print(a)
NameError: name 'a' is not defined
"""

# örnek 3
"""
a = 10
b = 'b'
print(a + b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
# endregion
