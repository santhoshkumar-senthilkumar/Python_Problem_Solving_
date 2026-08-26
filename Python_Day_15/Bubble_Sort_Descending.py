a=int(input("Size of the list : "))
b=[]
for i in range(a):
    b.append(int(input("Enter a Numbers : ")))
for i in range(a):
    print(b[i])
    for j in range(a-1):
        print(b[i], i)
        if b[j]<b[j+1]:
            temp=b[j]
            b[j]=b[j+1]
            b[j+1]=temp
            print(b)
print(b)
