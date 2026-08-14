b=(1,2,3,4,4,2,1,10,11)
c={}
for i in b:
    if i not in c:
        c[i]=1
    elif i in c :
        c[i] += 1
print(c)
