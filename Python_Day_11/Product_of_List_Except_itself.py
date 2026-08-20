a=int(input("Enter the size of the array"))
b=[]
for i in range(a):
    b.append(int(input("Enter the number : ")))
c=[]
 
for i in range(a):
    d=1
    for j in range(a):
        if i!=j:
            d *=b[j]
    c.append(d)
print(c)
