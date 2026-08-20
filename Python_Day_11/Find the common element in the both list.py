a=int(input("Enter the size of the list : "))
b=[]
c=[]
common=[]
for i in range(a):
    b.append(int(input("Enter the digit List 1 : ")))
for i in range(a):
    c.append(int(input("Enter the digit List 2 : ")))
for i in range(a):
    if b[i] in c and b[i]not in common :
        common.append(b[i])
print("The Common Digit in the both list is ",common)
