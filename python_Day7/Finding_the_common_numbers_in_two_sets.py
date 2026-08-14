a=int(input("Enter the range of Set : "))
b=set()
c=set()
for i in range(a):
    d=input("Enter a value to add in set 1 : ")
    b.add(d)
for i in range(a):
    d=input("Enter a value to add in set 2 :")
    c.add(d)
print(b&c)
