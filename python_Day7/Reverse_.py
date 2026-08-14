a = int(input("Enter the Number of ranges "))
b=[]
for i in range(a) :
    b.append(int(input("Enter a number")))
c=[]
j=a-1
for i in range(0,a):
    c.append(b[j])
    j -=1
print(c)
