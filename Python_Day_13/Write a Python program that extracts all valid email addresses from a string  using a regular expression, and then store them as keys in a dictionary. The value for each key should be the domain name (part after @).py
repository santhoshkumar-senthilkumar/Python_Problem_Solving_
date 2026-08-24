a = input("Enter the paragraph : ")
b = a.split(" ")
d={}
for i in b:
    if '@' in i:
        c=i.split('@')
        d[i]=c[1]
print(d)
