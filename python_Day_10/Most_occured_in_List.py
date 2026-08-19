a=int(input("Enter a Size of the List : "))
b=[]
for i in range(a):
    b.append(int(input()))
c={}
high =0
for i in b :
    if i not in c:
        c[i]=1
    else :
        c[i] += 1
for i in c:
    if c[i]>high:
        high = c[i]
for i in c:
    if c[i]==high:
        print(i," occurred more time .And Its occurred" ,high," Times ")
