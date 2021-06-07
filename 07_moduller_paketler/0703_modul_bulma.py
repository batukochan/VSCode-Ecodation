# region python modulleri nasıl bulur ?

"""
3 şekilde arar
1 - Bu kodun çalıştığı klasörlerde arar. ( aynı seviyede )
2 - PYTHONPATH environment veriable -> tanımlı ( çok kullanılmaz )
3 - Python'un kurulu olduğu kendi klasörlerinde arar. (virtul env'lerde)

sys.path -> arama klasörlerini verir
"""

# search path
"""
import sys

pythonSearchPath = sys.path
"""
"""
for path in pythonSearchPath:
    print(path)
"""

"""
import moduller.girdiİslemleri as girdi

a = girdi.stringAl()
print(a)

bu yol tercih edilmez.
"""

# local erişim

# örnek

