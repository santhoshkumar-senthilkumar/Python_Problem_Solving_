a=int(input("Enter the range : "))
b=[]
for i in range (a) :
    num = int(input("Enter a number : "))
    b.append(num)
large = b[0]
sec = b[1]
for i in range(2,len(b)) :
        if b[i]>large :
            sec=large
            large = b[i]
        if b[i]>sec and b[i]<large :
            sec = b[i]
print("The Second Largest Number in List is : ",sec,large)
