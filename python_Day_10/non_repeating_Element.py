a=int(input("Enter the size of the list : "))
b=[]
 
for i in range(a):
    b.append(input("Enter a value "))
for i in range(a):
    count =0
    for j in range (a):
        if b[i]==b[j]:
            count +=1
    if count <=1 :
        print(b[i],"It is the First Non Repeative element "
