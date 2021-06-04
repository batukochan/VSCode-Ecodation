#region asal 
"""
while True:
    s1 = input("Lütfen bir sayı giriniz: ")
    s2 = input("Lütfen bir sayı giriniz: ")
    if s1.isdigit() and s2.isdigit():
        s1, s2 = int(s1),int(s2)
        for i in range(min(s1,s2),max(s1,s2)+1):
            if i>1:
                for j in range(2,i):
                    if i % j ==0:
                        break
                else:
                    print(i,end=" | ")
        break    
    else:
        print("Lütfen sayısal değerler giriniz.")
"""
#endregion