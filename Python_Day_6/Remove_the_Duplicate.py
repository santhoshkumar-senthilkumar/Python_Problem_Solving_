a=int(input("Enter the range of  list : "))
b=[]
for i in range (a) :
    num = int(input("Enter the number : "))
    b.append(num)
unique =[]
for i in b :
    if i not in unique:
        unique.append(i)
        
print("The orginal list ",b ,"\n The duplicate removed list is ",unique)
