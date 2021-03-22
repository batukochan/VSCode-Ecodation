#region
"""
i=0
while i<10:
    if i%2==0:
        print("*",end="")
    else:
        print("$",end="")
    i+=1
"""
#endregion

#region
"""
i,j=0,0
while i<10:
    while j<10:
        j+=1
        if i%2==0:
            print(" *",end="")
        else:
            print(" $",end="")
    print("")
    i+=1
    j=0
"""
#endregion
