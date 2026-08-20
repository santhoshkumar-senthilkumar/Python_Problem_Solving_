a=int(input("Enter the number : "))
b=[]
g=[]
for i in  range(a):
    b.append(int(input("Enter a digit : ")))
for i in range(a):
    greater = True
    for j in range(i+1,a):
        if b[i]<b[j]:
            greater = False
            break
    if greater:
        g.append(b[i])
print(g)
