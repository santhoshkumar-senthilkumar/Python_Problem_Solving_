a=input("Enter a number to check it is amstrong or not : " )
c=len(a)
b=0
for i in a :
    b += int(i)**c
print(str(b)==a)
    
