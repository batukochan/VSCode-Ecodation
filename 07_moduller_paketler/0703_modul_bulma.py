# region python modulleri nasıl bulur ?

"""
3 şekilde arar
1 - Bu kodun çalıştığı klasörlerde arar. ( aynı seviyede )
2 - PYTHONPATH environment veriable -> tanımlı ( çok kullanılmaz )
3 - Python'un kurulu olduğu kendi klasörlerinde arar. (virtul env'lerde)

sys.path -> arama klasörlerini verir
"""

# search path

import sys

pythonSearchPath = sys.path
"""
for path in pythonSearchPath:
    print(path)
"""
"""
['C:\\Users\\batuh\\Desktop\\VSCode-Python Dersleri\\07_moduller_paketler', 'C:\\Users\\batuh\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\batuh\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\batuh\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\batuh\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\batuh\\AppData\\Roaming\\Python\\Python39\\site-packages', 'C:\\Users\\batuh\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']
PS C:\Users\batuh\Desktop\VSCode-Python Dersleri> py.exe .\07_moduller_paketler\0703_modul_bulma.py
C:\Users\batuh\Desktop\VSCode-Python Dersleri\07_moduller_paketler
C:\Users\batuh\AppData\Local\Programs\Python\Python39\python39.zip
C:\Users\batuh\AppData\Local\Programs\Python\Python39\DLLs
C:\Users\batuh\AppData\Local\Programs\Python\Python39\lib
C:\Users\batuh\AppData\Local\Programs\Python\Python39
C:\Users\batuh\AppData\Roaming\Python\Python39\site-packages
C:\Users\batuh\AppData\Local\Programs\Python\Python39\lib\site-packages
"""


