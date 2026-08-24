a=int(input("Enter the size of list to store Celsius : "))
b=[]
c={}
for i in range(a):
    b.append(int(input()))
    d=(b[i] * 9/5) + 32
    c[b[i]]= d
print(c)
