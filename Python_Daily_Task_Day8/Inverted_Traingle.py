a=int(input("Enter a number to form a right angle Traingle : "))
for i in range(a,0,-1) :
     for j in range(a):
         if j>=i :
            print("*",end ="")
         else :
             print(" ",end="")
     print()
