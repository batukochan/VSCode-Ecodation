''' 
Steak ve heap Ram'in ilgili alanıdır.
Liste yapılarında atama yaptıktan sonra atama yapılan 
listenin ve değişen listenin adresi aynı adrese kaydedilir.
List tipi aslında referans tipidir ve bundan kaynaklı adres ile işlem yapılır.
Aşağıdaki örnekte bu konuya açıklık getirebiliriz.
'''
list1=[1,2] 
list2=[3,4]
list1=list2
list2[0]=2
print(list1)

'''
------------------------------------------------------------------------------------------------
|                                        STEAK & HEAP                                          |
------------------------------------------------------------------------------------------------
|            Sayısal Veri Tipler               |                Object Veri Tipleri            |
------------------------------------------------------------------------------------------------                                 
| +int, float, boolean, valueType              | + List, string,object                         |
|                                              | + Referans tipleri                            |
------------------------------------------------------------------------------------------------
|                   STEAK                     LIST                  HEAP                       |
------------------------------------------------------------------------------------------------
    Adresler steak kısmında değerler heap kısmında saklanır.Bu durumda 8. ve 9. satırda işlenen 
kodların steak ve heap kısmındaki karşılığını 28-29. kod satırlarında betimlemeye çalışabiliriz.
------------------------------------------------------------------------------------------------
| list1 = 0XA1                                 | [1,2] 0XA1                                    |
| list2 = 0XA2                                 | [3,4] 0XA2                                    |
------------------------------------------------------------------------------------------------
|                                       list1=list2 Adımı                                      |
------------------------------------------------------------------------------------------------
    Bu adım ile birlikte list2'nin adresini list1'e atanır. Bu değerlerdeki değişimler aynı adres
 üzerinde kaydedilir.
------------------------------------------------------------------------------------------------
| list1 = 0XA2                                 |                                               |
| list2 = 0XA2                                 |                                               |
------------------------------------------------------------------------------------------------
|                                          list2[0]=2                                          |
------------------------------------------------------------------------------------------------
|                                              | list2 = [2,4] 0XA2                            |
------------------------------------------------------------------------------------------------
    list2'de yapılan değişiklik 0XA2 adresinde yapıldığı için otomatik olarak list1'in de değeri
[2,4] olur. Aynı adreste bulundukları için yapılan değişimler birbirlerini etkiler. print(list1)
ifadesi döndürülürken 0XA2 adresine gidilir ve buradaki değer ekrana yazdırılır.
------------------------------------------------------------------------------------------------
garbage collector, [1,2] 0XA1 ifadesini silecektir.
'''