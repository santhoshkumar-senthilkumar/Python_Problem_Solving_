a=int(input("Enter the size of the List : "))
b=int(input("Enter a K position to rotate the List : "))
c=[]
for i in range(a):
    c.append(int(input("Enter a Number : ")))
for i in range(b):
    for j in range(i+1,a):
        temp = c[j]
        c[j]=c[i]
        c[i]=temp
print(c)
