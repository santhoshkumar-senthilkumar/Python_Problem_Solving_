a=int(input("Enter a number to form a right angle Traingle : "))
for i in range(a) :
    temp = 1
    for j in range(a) :
        if j<=i :
            print(temp,end="")
            temp = temp+1
        else :
            print (" ",end="")
    print()
