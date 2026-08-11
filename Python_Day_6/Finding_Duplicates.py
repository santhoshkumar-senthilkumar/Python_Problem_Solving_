a=int(input("Enter a range : "))
b=[]
for i in range (a) :
    num = int(input("Enter a Number : "))
    b.append(num)
c=[]
for i in range(a):
    for j in range(i+1,a):
        if b[i]==b[j] and b[i]not in c :
            c.append(b[i])
print("The Duplicates in the List is ",c)
            
