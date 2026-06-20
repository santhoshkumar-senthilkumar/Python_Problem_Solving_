a=int(input("Enter a number to find sum of odd numbers"))
b=0
for i in range(1,a+1):
    if i%2!=0:
     b=b+i
print ("Sum of the odd number of ",a," is ",b)
