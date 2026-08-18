a=int(input("Enter the size of list to get the input"))
b=[]
for i in range (a):
    b.append(int(input("Enter a number : ")))
for i in range (a):
    for j in range(i+1,a):
        if b[i]==0 :
            if b[j]!=0 :
                temp = b[j]
                b[j]=b[i]
                b[i]=temp
print(b)
