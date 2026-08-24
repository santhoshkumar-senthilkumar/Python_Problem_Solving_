a=input("Enter the input : ")
b=a.split(" ")
d={}
for i in b:
    if "." in i or "," in i:
        i = i.strip(",.")
    if i.istitle() and i not in d:
        d[i]=1
    elif i.istitle() and i in d:
        d[i] += 1
print(d)
