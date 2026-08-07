a=int(input("Enter the starting range to find first number divisble ny 7 and 11 : "))
b=int(input("Enter the last range : "))
for i in range(a,b+1) :
    if i % 7 ==0 and i % 11 ==0 :
        print(i)
        break
    
