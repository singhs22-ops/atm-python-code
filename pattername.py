name = ["abc","xyz","tvf"]

k=0
for i in range(3):
    print("*",end="")
    print(name[i])
    for j in range(i+1):
        if j<2:
           print("*",end="")
        else:
            print()
   # print()

